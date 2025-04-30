from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_exercicio_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/exercicio-html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={  # UserSchema
            'username': 'testmyuser',
            'password': 'password',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testmyuser',
        'email': 'test@test.com',
        'id': 1,
    }
