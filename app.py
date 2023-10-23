from flask import Flask, redirect, render_template, request, abort

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    all_movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, all_movies=all_movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page

    #Chase Chiswell

    #extract movie rating data from the create movies form
    mov_title = request.form.get('mov_title')
    mov_director = request.form.get('mov_director')
    mov_rating = request.form.get('mov_rating')

    if mov_title == None or mov_director == None or mov_title == "" or mov_director == "" or mov_rating == None or int(mov_rating) > 5 or int(mov_rating) < 1:
        abort(400)
    
    #create a movie using the extracted data and redirect to the movies page
    movie_repository.create_movie(mov_title, mov_director, mov_rating)
 
    return redirect('/movies')


@app.get('/movies/search')
@app.post('/movies/search')
def search_movies():
    # Feature 3 - Bryan
    searching = False
    movie = None # this will be set to a value if a valid movie title is given
    if request.method == 'POST': # only do stuff with the form if a post request was made
        searching = True
        title = request.form.get('title')
        if title == None or title == "":
            abort(400)
        else:
            movie = movie_repository.get_movie_by_title(title)
    return render_template('search_movies.html', search_active=True, searching=searching, movie=movie)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    #Nicholas Zoll
    single = movie_repository.get_movie_by_id(movie_id) # use the passed-in movie_id value with the get_movie_by_id function to get the movie object
    if single == None:
        abort(400)
    

    return render_template('get_single_movie.html', single = single) #pass in the movie


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

