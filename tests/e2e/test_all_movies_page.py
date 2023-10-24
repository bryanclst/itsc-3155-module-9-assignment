# TODO: Feature 1
# Kiana Truong

from src.repositories.movie_repository import get_movie_repository

def test_all_movies_page(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()
    
    movie_repository.create_movie('Halloween', 'San Diego', 4)
    movie_repository.create_movie('Scary Movie', 'San Dino', 2)
    
    client = test_app
    
    response = client.get('/movies')
    
    assert response.status_code ==200
    
    if response.data:
        assert b'All Movies' in response.data
        assert b'See our list of movie ratings below' in response.data
        assert b'Halloween' in response.data
        assert b'San Diego' in response.data
        assert b'4' in response.data

        assert b'Scary Movie' in response.data
        assert b'San Dino' in response.data
        assert b'2' in response.data
    else:
        assert b'No movie entries found' in response.data