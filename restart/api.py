import json
from urllib import quote_plus
from urlparse import urljoin

import requests


METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']


class Method(object):

    def __init__(self, method, url, auth, serialize_payload, headers):
        self.method = getattr(requests, method.lower())
        self.url = url
        self.auth = auth
        self.serialize_payload = serialize_payload
        self.headers = headers

    def __call__(self, *args, **kwargs):
        if self.method in (requests.get, requests.options):
            kw = {'params': kwargs}
        else:
            # TODO: assertions for the payload
            data = args or kwargs
            if self.serialize_payload:
                data = json.dumps(data)
            kw = {'data': data}
        return self.method(
            self.url,
            auth=self.auth,
            headers=self.headers,
            **kw
        )


class EndPoint(object):

    def __init__(self, api, url):
        self.api = api
        self.url = url

    def __getitem__(self, item):
        url = self.url + '/' if not self.url.endswith('/') else self.url
        return EndPoint(
            self.api,
            urljoin(url, quote_plus(unicode(item))),
        )

    def __getattr__(self, attr):
        if attr in METHODS:
            return Method(
                method=attr,
                url=self.url,
                auth=self.api.auth,
                serialize_payload=self.api.serialize_payload,
                headers=self.api.headers,
            )
        return self[attr]


class Api(EndPoint):

    def __init__(self, base_url, auth=None, serialize_payload=True, headers=None):
        super(Api, self).__init__(self, base_url)
        self.auth = auth
        self.serialize_payload = serialize_payload
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        if headers:
            self.headers.update(headers)

    def __call__(self, url):
        return EndPoint(self, url)
