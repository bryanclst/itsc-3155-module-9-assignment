# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    temp_movie = movie_repository.create_movie("Alien","Ridley Scott", 5)
    result = movie_repository.get_movie_by_id(temp_movie.movie_id)
    assert result == temp_movie #checks if movie exists

    movie_repository.clear_db()
    result2 = movie_repository.get_movie_by_id(1)
    assert result2 == None #checks that function returns None when given a invalid id




