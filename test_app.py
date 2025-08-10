from app import app

def test_home():
    client = app.test_client()  # create test client
    response = client.get("/")  # send GET request to "/"

    assert response.status_code == 200
    assert response.data == b"Hello World"
