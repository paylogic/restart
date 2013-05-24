from urlparse import urljoin

import requests

METHODS = ['get', 'post', 'put', 'patch', 'delete', 'options']


class Method(object):

    def __init__(self, method, url, auth):
        self.method = getattr(requests, method)
        self.url = url
        self.auth = auth

    def __call__(self, **kwargs):
        result = self.method(self.url, data=kwargs)


class EndPoint(object):

    def __init__(self, api, url, auth=None):
        self.api = api
        self.url = url

    def __getitem__(self, item):
        return EndPoint(
            self.api,
            urljoin(self.url, unicode(item)),
        )

    def __getattr__(self, attr):
        if attr in METHODS:
            return Method(
                method=attr,
                url=self.url,
                auth=self.api.auth,
            )
        return self[attr]


class Api(EndPoint):

    def __init__(self, base_url, auth=None):
        super(Api, self).__init__(self, base_url, auth)

