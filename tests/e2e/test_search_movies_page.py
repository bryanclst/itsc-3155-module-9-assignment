# Feature 3 - Bryan
from flask.testing import FlaskClient
from app import movie_repository

def test_get_search_movie_page(test_app: FlaskClient) -> None:
    response = test_app.get('/movies/search')
    assert response.status_code == 200

def test_search_movie_invalid_title(test_app: FlaskClient) -> None:
    response = test_app.post('/movies/search', data={
        'title': None
    })
    assert response.status_code == 400

    response = test_app.post('/movies/search', data={
        'title': ""
    })
    assert response.status_code == 400

def test_search_movie_found(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    movie_repository.create_movie("test","test",1)

    response = test_app.post('/movies/search', data={
        'title': 'test'
    })
    data = response.data.decode()

    assert response.status_code == 200
    assert 'has a rating of' in data
    assert 'View Movie Page' in data
    assert "We couldn't find a movie with that title, please try again." not in data

def test_search_movie_not_found(test_app: FlaskClient) -> None:
    
    movie_repository.clear_db()
    movie_repository.create_movie("test","test",1)

    response = test_app.post('/movies/search', data={
        'title': 'asdfasdf'
    })
    data = response.data.decode()

    assert response.status_code == 200
    assert "has a rating of" not in data
    assert 'View Movie Page' not in data
    assert "We couldn't find a movie with that title, please try again." in data