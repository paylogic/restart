import restart


def test_options_has_querystring():
    """Test that OPTIONS accepts query strings."""
    # change the port, if needed
    api = restart.Api('http://0.0.0.0:9443')
    options_call = api.OPTIONS(key='foo')
    assert options_call.url.endswith('?key=foo')
