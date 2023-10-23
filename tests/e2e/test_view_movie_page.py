# TODO: Feature 4
#Nicholas Zoll
from src.repositories.movie_repository import get_movie_repository

def test_view_movie_page(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie("Aliens","James Cameron", 4)
    test_url = '/movies/' + str(test_movie.movie_id) #url with the correct movie_id 

    response = test_app.get(test_url)
    data = response.data.decode('utf-8')
    assert response.status_code == 200 #checks if request is successful 
    test_id = str(test_movie.movie_id)
    assert test_id in data #checks if the associated movie_id appears on the page

def test_view_movie_page_bad_1(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    test_movie = movie_repository.create_movie("Jumanji","Joe Johnston", 4)
    test_movie_other = movie_repository.create_movie("The Thing","John Carpenter", 5)
    test_url = '/movies/' + str(test_movie.movie_id) #url with the correct movie_id 

    response = test_app.get(test_url) 
    data = response.data.decode('utf-8')
    assert response.status_code == 200 #checks if request is successful 
    test_id_other = str(test_movie_other.movie_id)
    test_director_other = str(test_movie_other.director)
    test_title_other = str(test_movie_other.title)
    assert test_id_other not in data #checks that other movie fields are not displayed accidentally 
    assert test_director_other not in data
    assert test_title_other not in data


def test_view_movie_page_bad_2(test_app):
    movie_repository = get_movie_repository()
    movie_repository.clear_db()

    response = test_app.get('/movies/1')
    assert response.status_code == 400 #checks if request is unsuccessful when invalid movie id is used 
