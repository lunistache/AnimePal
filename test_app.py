from app import app

# Test that the index page returns a status code of 200
def test_index_page():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

# Test that the predict page returns a status code of 200
def test_predict_page():
    with app.test_client() as client:
        response = client.post('/predict', data={
            'title': 'Test Title',
            'genre': 'Test Genre',
            'description': 'Test Description',
            'type': 'Test Type',
            'producer': 'Test Producer',
            'studio': 'Test Studio'
        })
        assert response.status_code == 200

# Test that the predict page returns a predicted rating
def test_predicted_rating():
    with app.test_client() as client:
        response = client.post('/predict', data={
            'title': 'Cowboy Bebop',
            'genre': "'Action', 'Adventure', 'Comedy', 'Drama', 'Sci-Fi', 'Space'",
            'description': 'In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as "Cowboys." The ragtag team aboard the spaceship Bebop are two such individuals. ',
            'type': 'TV',
            'producer': 'Bandai Visual',
            'studio': 'Sunrise'
        })
        assert b'Predicted rating:' in response.data
