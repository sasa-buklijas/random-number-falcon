import falcon
from falcon import testing
import pytest
from random_number import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_is_it_working(client):
    return_json = {
        "higherLimit": 3,
        "lowerLimit": 3,
        "number": 3
    }

    # response = client.simulate_get('/random-number?min=3&max=3')
    # not allowed, must use query_string
    response = client.simulate_get('/random-number', query_string='min=3&max=3')

    assert response.json == return_json
    assert response.status == falcon.HTTP_OK


def test_max_must_be_int(client):
    return_json = {
        "description": "The \"text\" parameter is invalid. max must be number",
        "title": "Invalid parameter"
    }

    response = client.simulate_get('/random-number', query_string='min=3&max=text')

    assert response.json == return_json
    assert response.status == falcon.HTTP_BAD_REQUEST

# TODO:
    # more tests can be added
