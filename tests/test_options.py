import restart

def test_options_has_querystring():
    api = restart.API('http://0.0.0.0:8000')
    options_call = api.OPTIONS(key='foo')
    assert options_call.url.endswith('?key=foo')