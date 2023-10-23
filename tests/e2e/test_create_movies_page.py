# TODO: Feature 2

#e2e test to make sure that the movies page is updated with a newly created movie

from app import movie_repository
from flask.testing import FlaskClient

def test_create_movie(test_app: FlaskClient):

    movie_repository.clear_db()
    
    
    response = test_app.post('/movies', data = {
        'mov_title': "Shin Kamen Rider",
        'mov_director': "Hideaki Anno",
        'mov_rating': 5}, follow_redirects = True)
    #tests to make sure the creation was successful
    assert response
    assert response.status_code == 200
    

    
    
def test_create_movie_bad(test_app: FlaskClient):
    movie_repository.clear_db()

    response2 = test_app.post('/movies', data = {
        'title': None,
        'director': None,
        'rating': None})
    assert response2.status_code == 400
    

