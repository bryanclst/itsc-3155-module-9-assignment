# TODO: Feature 1
# Kiana Truong

from app import app

def test_all_movies_page():
    client = app.test_client()
    
    response= client.get('/movies')
    
    assert b'All Movies' in response.data
    assert b'See our list of movie ratings below' in response.data
