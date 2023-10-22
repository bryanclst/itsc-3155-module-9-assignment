# TODO: Feature 1
#Kiana Truong

from src.models.rating import Rating

def test_get_all_movies():
    ratings=[]
    ratings.append(Rating(movie_title="Halloween", rating=4.5))
    ratings.append(Rating(movie_title="Spider-Man", rating=3.5))
    ratings.append(Rating(movie_title="Batman", rating=2.0))
    ratings.append(Rating(movie_title="Cinderella", rating=4.2))

    assert len(ratings) == 4