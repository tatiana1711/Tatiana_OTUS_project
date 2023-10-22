import pytest
import requests


def test_json_ph_status_code(base_url):
    result = requests.get(base_url)
    assert result.status_code == 200


@pytest.mark.parametrize("post_number", ("1", "20", "100"))
def test_post_theme(base_url, post_number):
    result = requests.get(url=f'{base_url}posts/{post_number}')
    assert result.status_code == 200


@pytest.mark.parametrize("id, parametr, value", [('1', 'username', 'Bret'), ('2', 'email', 'Shanna@melissa.tv')])
def test_user_parametr(base_url, id, parametr, value):
    result = requests.get(url=f'{base_url}users/{id}')
    assert result.status_code == 200 and value == result.json()[parametr]


@pytest.mark.parametrize("post_number", (1,2))
def test_post_comments(base_url, post_number):
    result = requests.get(f'{base_url}posts/{post_number}/comments')
    assert result.status_code == 200 and len(result.json()) > 0


@pytest.mark.parametrize("title, body, user_id", [("title_1", "body_1", 1), ("title_2", "body_2", 2), ("title_3", "body_3", 33)])
def test_post(base_url, title, body, user_id):
    response = requests.post(url=f"{base_url}posts",
                             headers={"Content-type": "application/json; charset=UTF-8"},
                             json={"title": title, "body": body, "userId": user_id}
                             )
    assert response.status_code == 201


@pytest.mark.parametrize('id', [1, 2, 33])
def test_delete(base_url, id):
    r = requests.delete(f'{base_url}posts/{id}')
    assert r.status_code == 200



