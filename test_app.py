import json

import pytest

from app import create_app


@pytest.fixture
def get_dev_by_id():
    flask_app = create_app()
    response = flask_app.test_client().get('desenvolvedores/<int:id>')
    return response


def test_get_page_post():
    flask_app = create_app()
    response = flask_app.test_client().post('/')
    assert response.status_code == 404


def test_get_page_get_not_found():
    flask_app = create_app()
    response = flask_app.test_client().get('/')
    assert response.status_code == 404


def test_get_page_get():
    flask_app = create_app()
    response = flask_app.test_client().get('/desenvolvedores')
    assert response.status_code == 200


def test_get_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().get('/desenvolvedores')
    assert json.loads(response.data)['desenvolvedores'][0] == {'nome': 'marcos paulo',
                                                               'skills': ['python', 'django', 'flask']}


def test_post_desenvolvedor():
    flask_app = create_app()
    response = flask_app.test_client().post('/desenvolvedores', )
    assert response.status_code == 200


def test_post_desenvolvedor_index():
    flask_app = create_app()
    response = flask_app.test_client().get('/desenvolvedores/0')
    assert response.status_code == 200


def test_post_desenvolvedor_index_delete():
    flask_app = create_app()
    response = flask_app.test_client().put('/degit senvolvedores/0')
    assert response.status_code == 200
