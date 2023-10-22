# TODO: Feature 2

#e2e test to make sure that the movies page is updated with a newly created movie

from app import movie_repository
from flask.testing import FlaskClient

def test_create_movie(test_app: FlaskClient):
    movie_repository.create_movie('Shin Kamen Rider','Hideaki Anno','5')
    response = test_app.post('/movies')
    #tests to make sure the redirect was successful
    assert response
    assert response.status_code == 302 #status code for a redirect

    #asserts that the movie was successfully created and posted
    response = test_app.post('/movies', follow_redirects=True)
    assert response.status_code == 200
