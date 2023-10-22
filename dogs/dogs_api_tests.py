import pytest
import requests


def test_status_code_api(base_url):
    r = requests.get(url=base_url)
    assert r.status_code == 200


@pytest.mark.parametrize("number", [2, 10])
def test_image_status_code(base_url, number):
    result = requests.get(url=f'{base_url}/breeds/image/random/{number}').json()
    for b in result.get('message'):
        image_code = requests.get(url=b).status_code
        assert image_code == 200


@pytest.mark.parametrize("number", [1,20,50,100])
def test_max_random_images(base_url, number):
    result = requests.get(url=f'{base_url}/breeds/image/random/{number}').json()
    assert len(result) <= 50


@pytest.mark.parametrize('breed', ['cattledog/australian', 'briard'])
def test_breed_in_images(base_url, breed):
    result = requests.get(url=f'{base_url}/breed/{breed}/images').json()
    assert len(result.get('message')) > 0


@pytest.mark.parametrize("breed, subBreed", [('cattledog','australian'), ('bulldog', 'english')])
def test_breed_has_subbreed(base_url, breed, subBreed):
    result = requests.get(url=f'{base_url}/breed/{breed}/list').json()
    assert subBreed in result.get('message')

