from app import app

def test_index_route():
    client = app.test_client()
    response = client.get('/api/')
    assert response.status_code == 200
    assert b'Welcome a my mini app - Created by Gustavo Menezes!' in response.data