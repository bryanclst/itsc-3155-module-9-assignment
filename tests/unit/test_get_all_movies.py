# TODO: Feature 1
#Kiana Truong

from src.repositories.movie_repository  import  get_movie_repository
movie_repository = get_movie_repository()

def test_get_all_movies():
    movie_repository.clear_db()
    
    movie_repository.create_movie('Halloween', 'San Diego', 4)
    movie_repository.create_movie('Movie2', 'Director2', 3)
    movie_repository.create_movie('Movie3', 'Director3', 2)
    movie_repository.create_movie('Movie4', 'Director4', 1)
    
    all_movies = movie_repository.get_all_movies()
    
    assert len(all_movies) == 4