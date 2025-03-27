from http import HTTPStatus

from fastapi.testclient import TestClient  # type: ignore

from fast_zero.app import app


def test_read_root_deve_retornar_ok():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert (Afirma)
    assert response.json() == {'message': 'Olá mundo!'}
