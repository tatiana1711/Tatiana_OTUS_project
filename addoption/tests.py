import requests


def test_url_code(base_url, status_code):
    response = requests.get(base_url)
    assert response.status_code == status_code

