import pytest
import requests


def test_api_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200


@pytest.mark.parametrize("brewery_type",
                         ['micro', 'nano', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor',
                          'closed'])
def test_search_by_type(base_url, brewery_type):
    r = requests.get(url=f'{base_url}/v1/breweries?by_type={brewery_type}')
    assert r.status_code == 200 and r.json()[0]["brewery_type"] == brewery_type


@pytest.mark.parametrize("id", ['5128df48-79fc-4f0f-8b52-d06be54d0cec', '9c5a66c8-cc13-416f-a5d9-0a769c87d318', 'ef970757-fe42-416f-931d-722451f1f59c'])
def test_id_list(base_url, id):
    url = requests.get(f"{base_url}/v1/breweries/{id}")
    assert url.status_code == 200
    response = url.json()
    assert response["id"] == id


@pytest.mark.parametrize("number", [0, 25, 50, 100])
def test_max_random_breweries(base_url, number):
    r = requests.get(url=f'{base_url}/v1/breweries/random?size={number}').json()
    assert len(r) <= 50


def test_search(base_url):
    response = requests.get(f"{base_url}/breweries/search?query=dog")
    assert response.status_code == 200
