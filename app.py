from flask import Flask, redirect, render_template

from src.repositories.movie_repository import get_movie_repository
from src.models.rating import Rating

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    ratings= [
        {'movie_title': 'Halloween', 'rating' : 4.5},
        {'movie_title': 'Spider-Man', 'rating' : 3.5},
        {'movie_title': 'Batman', 'rating' : 2.0},
        {'movie_title': 'Cinderella', 'rating' : 4.2},
    ]
    return render_template('list_all_movies.html', list_movies_active=True, saved_ratings=ratings)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    #Nicholas Zoll
    single = movie_repository.get_movie_by_id(movie_id) # use the passed-in movie_id value with the get_movie_by_id function to get the movie object
    single_id = single.movie_id                         # store the associated movie id into single_id
    single_title = single.title                         # store the associated movie title into single_title
    single_director = single.director                   # store the associated movie director into single_director
    single_rating = single.rating                       # store the associated rating into single_rating

    return render_template('get_single_movie.html', single = single, single_id = single_id, single_title = single_title, single_director = single_director, single_rating = single_rating) #pass in the single movie data


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    mov = movie_repository.get_movie_by_id(movie_id) # 
    mov_id = mov.movie_id                         #
    mov_title = mov.title                         #
    mov_director = mov.director                   #
    mov_rating = mov.rating                       #

    return render_template('edit_movies_form.html', mov = mov, mov_id = mov_id, mov_title = mov_title, mov_director = mov_director, mov_rating = mov_rating)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass

if __name__ == '__main__':
    app.run(debug=True)


