import restart


def test_supports_headers():
    """Test that headers are supported."""
    api = restart.Api(
        'http://0.0.0.0:9443',
        headers={'Referer': 'http://localhost:8000/index.html'},
    )
    response = api.OPTIONS()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'

    response = api.GET()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'

    response = api.POST()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'

    response = api.DELETE()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'

    response = api.PUT()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'


def test_supports_headers_with_auth():
    """Test that headers are supported when using auth."""
    api = restart.Api(
        'http://0.0.0.0:9443',
        auth=('api_key', 'api_secret'),
        headers={'Referer': 'http://localhost:8000/index.html'},
    )
    response = api.OPTIONS()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
    assert 'Authorization' in response.request.headers

    response = api.GET()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
    assert 'Authorization' in response.request.headers

    response = api.POST()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
    assert 'Authorization' in response.request.headers

    response = api.DELETE()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
    assert 'Authorization' in response.request.headers

    response = api.PUT()
    assert response.request.headers['Referer'] == 'http://localhost:8000/index.html'
    assert 'Authorization' in response.request.headers
