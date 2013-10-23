import restart


def test_options_supports_headers():
    """Test that 'restart' supports headers."""
    api = restart.Api('http://0.0.0.0:9443')
    response = api.OPTIONS(headers={'Referer': 'http://localhost:8000/index.html'})
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
