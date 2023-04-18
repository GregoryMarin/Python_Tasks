import requests

from configuration import SERVICE_URL

from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA

from jsonschema import validate


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_CODE.value
    for item in received_posts:
        validate(received_posts)


# https://my-json-server.typicode.com/typicode/demo/posts