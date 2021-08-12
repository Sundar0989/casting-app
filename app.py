import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, db_drop_and_create_all
from config import *
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  #db_drop_and_create_all()

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE')
    return response

  # Get request for actors end point
  @app.route('/actors', methods=['GET'])
  def get_actors():
    actors = Actor.query.all()

    if len(actors) == 0:
        return abort(404)
    
    return jsonify({
        'success': True,
        'actors': [actor.format() for actor in actors]
    }), 200

  # Get request for movies end point
  @app.route('/movies', methods=['GET'])
  def get_movies():
    movies = Movie.query.all()

    if len(movies) == 0:
        return abort(404)
    
    return jsonify({
        'success': True,
        'movies': [movie.format() for movie in movies]
    }), 200

  # Delete actors
  @app.route('/actors/<int:id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(jwt, id):
    actor = Actor.query.get(id)

    if not actor:
        return abort(404)
    
    try:
      actor.delete()
      return jsonify({
        'success': True,
        'actors': id
      }), 200
    except:
      return abort(422)

  # Delete movies
  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(jwt, id):
    movie = Movie.query.get(id)

    if not movie:
        return abort(404)
    
    try:
      movie.delete()
      return jsonify({
        'success': True,
        'movies': id
      }), 200
    except:
      return abort(422)

  # Post actors
  @app.route('/actors', methods=['POST'])
  @requires_auth('post:actors')
  def create_actors(jwt):
    
    body = request.get_json()

    try:
      name = body.get('name')
      age = body.get('age')
      gender = body.get('gender')
      actor = Actor(name=name, age=age, gender=gender)
      actor.insert()
      return jsonify({
        'success': True,
        'actors': [actor.format()]
      }), 200
    except:
        return abort(422)

  # Post movies
  @app.route('/movies', methods=['POST'])
  @requires_auth('post:movies')
  def create_movies(jwt):
    
    body = request.get_json()

    try:
      title = body.get('title')
      release_date = body.get('release_date')
      movie = Movie(title=title, release_date=release_date)
      movie.insert()
      return jsonify({
        'success': True,
        'movies': [movie.format()]
      }), 200
    except:
        return abort(422)

  # Patch actors
  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(jwt, id):
    body = request.get_json()
    actor = Actor.query.get(id)

    if not actor:
        return abort(404)

    try:
        actor.name = body.get('name')
        actor.age = body.get('age')
        actor.gender = body.get('gender')
        actor.update()
        return jsonify({
        'success': True,
        'actors': [actor.format()]
    }), 200
    except:
        return abort(422)
        
  # Patch movies
  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(jwt, id):
    body = request.get_json()
    movie = Movie.query.get(id)

    if not movie:
        return abort(404)

    try:
        movie.title = body.get('title')
        movie.release_date = body.get('release_date')
        movie.update()
        return jsonify({
        'success': True,
        'movies': [movie.format()]
    }), 200
    except:
        return abort(422)

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "resource not found"
      }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  @app.errorhandler(500)
  def internal_server(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "internal server error"
      }), 500
  '''
  @TODO implement error handler for 404
      error handler should conform to general task above
  '''
  '''
  @TODO implement error handler for AuthError
      error handler should conform to general task above
  '''
  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
    """
    Receive the raised authorization error and propagates it as response
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

  return app

# create the app
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)