# Feature 3 - Bryan
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_title() -> None:
    movies = get_movie_repository()
    movies.clear_db()

    m1 = movies.create_movie("test", "test", 1)
    assert movies.get_movie_by_title(m1.title) == m1

    movies.clear_db()
    assert movies.get_movie_by_title("test") == None
    assert movies.get_movie_by_title(None) == None