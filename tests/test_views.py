import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_post_weather(client):
    response = client.post('/weather', json={
        'user_defined_id': 'test_id',
        'city_ids': [3439525, 3439781]
    })
    assert response.status_code == 202


def test_get_weather(client):
    response = client.get('/weather/test_id')
    assert response.status_code == 404
