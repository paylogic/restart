import restart


def test_root_uri():
    """Test that OPTIONS accepts query strings."""
    # change the port, if needed
    api = restart.Api('http://0.0.0.0:9443')
    assert api['/'].url == 'http://0.0.0.:9443/'
