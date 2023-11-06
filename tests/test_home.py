from app import app

def test_index_route():
    client = app.test_client()
    response = client.get('/api/')
    assert response.status_code == 200
    assert b'Hello World' in response.data