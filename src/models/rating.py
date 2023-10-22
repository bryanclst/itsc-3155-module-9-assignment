#src/models/ratings.py 

class Rating:
    def __init__(self, movie_title, rating):
        self.movie_title = movie_title
        self.rating = rating
        
def __repr__(self):
    return f"<Rating(movie_title='{self.movie_title}', rating={self.rating})>"

