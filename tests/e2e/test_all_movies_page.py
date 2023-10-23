# TODO: Feature 1
# Kiana Truong

from src.repositories.movie_repository import get_movie_repository
import sys

def test_all_movies_page(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    
    client = test_app
    
    response = client.get('/movies')
    
    #if reponse.data == null%
    if response.status_code == 200:
        if response.data:
            assert b'All Movies' in response.data
            assert b'See our list of movie ratings below' in response.data
            assert b'Halloween' in response.data
            assert b'San Diego' in response.data
            assert 4 in response.data

            assert b'Scary Movie' in response.data
            assert b'San Dino' in response.data
            assert b'2' in response.data
        else:
            pass
    else:
        assert False
