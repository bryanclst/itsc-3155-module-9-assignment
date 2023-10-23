# Feature 3 - Bryan
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository

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
    movies = get_movie_repository()
    movies.clear_db()
    movies.create_movie("test","test",1)

    response = test_app.post('/movies/search', data={
        'title': 'test'
    })
    data = response.data.decode()

    assert response.status_code == 200
    assert '</i> has a rating of <b>' in data

def test_search_movie_not_found(test_app: FlaskClient) -> None:
    
    movies = get_movie_repository()
    movies.clear_db()
    movies.create_movie("test","test",1)

    response = test_app.post('/movies/search', data={
        'title': 'asdfasdf'
    })
    data = response.data.decode()

    assert response.status_code == 200
    assert "<h3>We couldn't find a movie with that title, please try again.</h3>" in data