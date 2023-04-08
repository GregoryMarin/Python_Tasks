import requests


from configuration import SERVICE_URL


def test_getting_post():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200, "Recived status code is not equal to expected."
    print(response.json())

# https://my-json-server.typicode.com/typicode/demo/poste