# Casting Agency

## Introduction
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The Executive Producer within the company wants to create a system to simplify and streamline the process.

This project attempts to provide a application that does the job for the casting agency company. Users with the appropriate permission can perform actions with the database. General users can view the actors and movies database. The project is hosted in Heroku and the live link is provided below.

## Link to Heroku login
https://casting-heroku-app.herokuapp.com/        
https://casting-heroku-app.herokuapp.com/actors   
https://casting-heroku-app.herokuapp.com/movies

If you need to perform additional actions, please go through the roles below in this document for the same.

Enjoy!
 

### Installing Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the root directory and running:

```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

5. **Local Database Setup**
Once you create the database, open your terminal, navigate to the root folder, and run:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.

6. **Local Testing**
To test your local installation, run the following command from the root folder:
```bash
python test_app.py
```

### Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
Setting the `FLASK_APP` variable to `app` directs Flask to use `app.py` file to find and load the application.

## Users, Roles & Tokens
### Link to login for tokens
https://udacity-coffee-stack.us.auth0.com/authorize?audience=casting&response_type=token&client_id=rIlXKEm01qQcdAw3f1D00ACENs293PeC&redirect_uri=http://localhost:8080/actors

### Casting Assistant

```
Username - c.kishore47@gmail.com
Password - #Udacity3
Permissions - Get details about Movies & Actors
Token - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5qMmttY3Zfd0diNkhsbzlRY0pmViJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktY29mZmVlLXN0YWNrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTA5MjA5NDM1ODJiYzAwNjk0N2M5NjgiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI4NzE5ODY3LCJleHAiOjE2Mjg3MjcwNjcsImF6cCI6InJJbFhLRW0wMXFRY2RBdzNmMUQwMEFDRU5zMjkzUGVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.KFDu1NqOgWceZboJd3teAZeV6PvispAIlLBQECwZkFEYBRkjTtl3KZmawKVnjxVhkZKRayYExS2rg0_QHwZUwGAbd5rSMAoSOWSZEj_9CJTbCxfphx8Bz4VhJxwjCcMCDQyqhsu7g6s70fnpxaIzF5XVkQ0AS3Izsr_7-Ay9x30uLEGy1U8NiXU8aEN5szJ_eZvx_DU6ww2brSyo6vxqn5v7HydZkxqHnOMluXECE0nhzT7AtDGy_RUuyomKZPWnj9wx04JUbGCO6v7IfKWmkLIvPXlkn0SkcE8EBgoeEEmq5VW3AlRnDLwjZ7dsfRQm5sHYCTBmE4E1OciuAILnOw
```

### Casting Director

```
Username - sundarstyles89@gmail.com
Password - #Udacity3
Permissions - All permissions a Casting Assistant has + Add or delete an actor from the database + Modify actors or movies
Token - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5qMmttY3Zfd0diNkhsbzlRY0pmViJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktY29mZmVlLXN0YWNrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTA5MWZkY2UxNmI5MTAwNmFkNGZiOWQiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI4NzE4NDE5LCJleHAiOjE2Mjg3MjU2MTksImF6cCI6InJJbFhLRW0wMXFRY2RBdzNmMUQwMEFDRU5zMjkzUGVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.NfJhrrg25mb-psa-Gn29hP4JV60jmcmxq5O5wEYz7JxdIYaqiMI_a3VQ9vRiOdqhPxgpBZOT6Uxg0regcURkhrWdomDwMaOiSxMYSEt0g7FpNCPbiadR0g8C9ipqqBWuAQYNz1xehmXm6jpsk_IJbXItgumHZm4PYiUGUoXwjG7WAvspJOZimk6nj6h2ODQD0G4hePFDikLf3F5U0vGRimBM8fNcYJHxWW2loIxu8L9s4TENvh3j6AxCidFIeUW1cABbmjN6nzmVweVuhJ9n6VBJNs-sypDHOjOb1G2zgHDWnBLo0Q1g6N93xxdXdofydtY__Co035RgjAmpf2NTiw
```

### Executive Producer

```
Username - aishwaryaloganathan5@gmail.com
Password - Udacity#3
Permissions - All permissions a Casting Director has + Add or delete a movie from the database
Token - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5qMmttY3Zfd0diNkhsbzlRY0pmViJ9.eyJpc3MiOiJodHRwczovL3VkYWNpdHktY29mZmVlLXN0YWNrLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MTEzMjZiM2M3MjQwNTAwNzFiODc4ZDQiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNjI4NzE5NzcwLCJleHAiOjE2Mjg3MjY5NzAsImF6cCI6InJJbFhLRW0wMXFRY2RBdzNmMUQwMEFDRU5zMjkzUGVDIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.caLlkjKwlrNxFC-BkqHUe3sSQjhWy3NAp76pyvpofqk21ZoRwvqGEODqYOFMFRP4lX4t2BEBE7ZUcKHSIG31yzg8fePbG9RuAmVN7MUhY3rCT7x70VBcp2lIeES9gmj370fPlsaHFfxA60fLgzX9-KaRGe6fP5R2ws3uCXlVPKn6lGdPeHrezI5-oqLtNdBs98FmL-WPzE2Lvw3QyAxS1EOYwulTkr22Q0l8J6cYU3hd3DqrEjIfKpwD3yaTXmomSeCvKmWmnry_uWeJoya2On-eR6yy5TXw_a-QECHciByOnCK1jY3hpE2ZsPlzaYHJqGji_TnbxVgcn3sHd_Ee-w
```

## Endpoints

### GET '/actors'
- Get the actors registered in the __Actor__ database
- Request Arguments: None
- Returns: An list of dictionary object with a id, name, age, gender. 

#### Sample 

```bash
curl https://casting-heroku-app.herokuapp.com/actors
```

```
{
   "actors":[
      {
         "age":46,
         "gender":"Male",
         "id":1,
         "name":"Leonardo DiCaprio"
      },
      {
         "age":45,
         "gender":"Female",
         "id":2,
         "name":"Kate Winslet"
      }
   ],
   "success":true
}
```

### GET '/movies'
- Get the movies registered in the __Movie__ database
- Request Arguments: None
- Returns: An list of dictionary object with a title, release_date. 

#### Sample 

```bash
curl https://casting-heroku-app.herokuapp.com/movies
```

```
{
   "movies":[
      {
         "id":1,
         "release_date":"Fri, 19 Dec 1997 00:00:00 GMT",
         "title":"Titanic"
      }
   ],
   "success":true
}
```

### DELETE '/actors/id'
   
- Delete an actor from __Actor__ database
- Request Arguments: Bearer token and Actor Id
- Returns: Json object with deleted actor id and success flag as __True__. 

#### Sample    
   
```bash
curl -X DELETE https://casting-heroku-app.herokuapp.com/actors/1 -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN"
```
   
```   
{
   "actors":1,
   "success":true
}
```


### POST '/actors'
- Insert a new actor into the __Actor__ database
- Request Arguments: Bearer token and Actor json
- Returns: Success flag and inserted Actor details. 

#### Sample 

```bash
curl -X POST https://casting-heroku-app.herokuapp.com/actors -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN" -H "Content-Type: application/json" -d '{"name": "Tom Hanks", "age": 65, "gender": "Male"}'
```

```
{
   "actors":[
      {
         "age":65,
         "gender":"Male",
         "id":3,
         "name":"Tom Hanks"
      }
   ],
   "success":true
}
```

### PATCH '/actors/id'
- Update an existing actor into the __Actor__ database
- Request Arguments: Bearer token and update Actor json
- Returns: Success flag and updated Actor details. 

#### Sample 

Changing the actor name from Tom Hanks to Thomas Jeffrey Hanks

```bash
curl -X PATCH https://casting-heroku-app.herokuapp.com/actors/3 -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN" -H "Content-Type: application/json" -d '{"name": "Thomas Jeffrey Hanks", "age": 65, "gender": "Male"}'
```

```
{
   "actors":[
      {
         "age":65,
         "gender":"Male",
         "id":3,
         "name":"Thomas Jeffrey Hanks"
      }
   ],
   "success":true
}
```

### POST '/movies'
- Insert a new movie into the __Movie__ database
- Request Arguments: Bearer token and Movie json
- Returns: Success flag and inserted Movie details. 

#### Sample 

```bash
curl -X POST https://casting-heroku-app.herokuapp.com/movies -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN" -H "Content-Type: application/json" -d '{"title": "Parasite", "release_date": "2019-10-05"}'
```

```
{
   "movies":[
      {
         "id":2,
         "release_date":"Sat, 05 Oct 2019 00:00:00 GMT",
         "title":"Parasite"
      }
   ],
   "success":true
}
```

### PATCH '/movies/id'
- Update an existing movie into the __Movie__ database
- Request Arguments: Bearer token and update Movie json
- Returns: Success flag and updated Movie details. 

#### Sample 

Changing the release date from October 5, 2019 to October 4, 2019

```bash
curl -X PATCH https://casting-heroku-app.herokuapp.com/movies/2 -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN" -H "Content-Type: application/json" -d '{"title": "Parasite", "release_date": "2019-10-04"}'
```

```
{
   "movies":[
      {
         "id":2,
         "release_date":"Fri, 04 Oct 2019 00:00:00 GMT",
         "title":"Parasite"
      }
   ],
   "success":true
}
```

### DELETE '/movies/id'
   
- Delete a movie from __Movie__ database
- Request Arguments: Bearer token and Movie Id
- Returns: Json object with deleted movie id and success flag as __True__. 

#### Sample    
   
```bash
curl -X DELETE https://casting-heroku-app.herokuapp.com/movies/2 -H "Authorization: Bearer $EXECUTIVE_PRODUCER_TOKEN"
```
   
```   
{
   "movies":2,
   "success":true
}
```


