import os 

database_path = os.getenv('SQLALCHEMY_DATABASE_URI')

if database_path == '':
    database_path = "postgresql://localhost:5432/capstone"

