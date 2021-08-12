import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Movie, Actor, db_drop_and_create_all


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432', self.database_name)
        self.casting_assistant = os.getenv('CASTING_ASSISTANT_TOKEN')
        self.casting_director = os.getenv('CASTING_DIRECTOR_TOKEN')
        self.executive_producer = os.getenv('EXECUTIVE_PRODUCER_TOKEN')
        self.new_movie = {
                "title": "Parasite", 
                "release_date": '2019-10-05'
                }
        self.new_actor = {
                "name": "Tom Hanks",
                "age": 65,
                "gender": "Male"
        }
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Drop data from movies tables
    def drop_movie_data(self):
        Movie.query.delete()
        return None
    
    # drop data from actors table
    def drop_actor_data(self):
        Actor.query.delete()
        return None
    # Add data back to movie table
    def add_movie_data(self):
        # Movies data
        movie=Movie(title='Titanic', release_date='1997-12-19')
        movie.insert()
    # Add data back to actor table
    def add_actor_data(self):
        # Actors data
        actor=Actor(name='Leonardo DiCaprio', age=46, gender='Male')
        actor.insert()
        actor=Actor(name='Kate Winslet', age=45, gender='Female') 
        actor.insert()

    # success behavior for /actors endpoint
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # success behavior for /movie endpoint
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))

    # failure behavior for /actors endpoint
    def test_404_get_actors_failure(self):
        self.drop_actor_data()
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))
        self.add_actor_data() 
    
    # failure behavior for /movies endpoint
    def test_404_get_movies_failure(self):
        self.drop_movie_data()
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))
        self.add_movie_data() 
        
    # create new actor using /actors endpoint
    def test_post_actors(self):
        res = self.client().post('/actors', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for new actor using /actors endpoint
    def test_422_failure_post_actors(self):
        res = self.client().post('/actors', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))
    
    # delete actor using /actors endpoint
    def test_delete_actors(self):
        res = self.client().delete('/actors/1', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for delete actor using /actors endpoint
    def test_404_failure_delete_actors(self):
        res = self.client().delete('/actors/200', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))

    # update actor using /actors endpoint
    def test_update_actors(self):
        res = self.client().patch('/actors/2', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for update actor using /actors endpoint
    def test_422_failure_update_actors(self):
        res = self.client().patch('/actors/2', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))

    # update movie using /movies endpoint
    def test_update_movies(self):
        res = self.client().patch('/movies/1', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for update movie using /movies endpoint
    def test_422_failure_update_movies(self):
        res = self.client().patch('/movies/1', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))
    
    # create new movie using /movies endpoint
    def test_post_movies(self):
        res = self.client().post('/movies', 
            headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for new movie using /movies endpoint
    def test_422_failure_post_movies(self):
        res = self.client().post('/movies', 
            headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))

    # delete movie using /movies endpoint
    def test_delete_movies(self):
        res = self.client().delete('/movies/1', 
            headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))
    
    # failure case for delete movie using /movies endpoint
    def test_404_failure_delete_movies(self):
        res = self.client().delete('/movies/200', 
            headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(len(data))

    # Test for RBAC 
    # Casting assistant access
    # success behavior for casting assistant
    def test_success_casting_assistant(self):
        res = self.client().get('/actors',
            headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))

    # failure behavior for casting assistant
    def test_failure_casting_assistant(self):
        res = self.client().patch('/actors/2', 
            headers={"Authorization": "Bearer {}".format(self.casting_assistant)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    # success behavior for casting director
    def test_success_casting_director(self):
        res = self.client().post('/actors',
            headers={"Authorization": "Bearer {}".format(self.casting_director)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))

    # failure behavior for casting director
    def test_failure_casting_director(self):
        res = self.client().delete('/movies/1', 
            headers={"Authorization": "Bearer {}".format(self.casting_director)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    # success behavior for executive producer
    def test_success_executive_producer(self):
        res = self.client().post('/actors',
            headers={"Authorization": "Bearer {}".format(self.executive_producer)}, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data))

    # failure behavior for executive producer
    def test_failure_executive_producer(self):
        res = self.client().delete('/movies/200', 
            headers={"Authorization": "Bearer {}".format(self.executive_producer)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
    app.run()
