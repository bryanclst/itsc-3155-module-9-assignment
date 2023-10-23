# TODO: Feature 2
from src.models.movie import Movie
def test_create_movie():

    #tests a successful movie creation
    movie = Movie(movie_id=id, title='Shin Kamen Rider', director='Hideaki Anno', rating=5)
    assert movie
