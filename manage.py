from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from models import db
import os

app = create_app()

database_path = os.environ.get('SQLALCHEMY_DATABASE_URI')
if database_path = '':
    database_path = 'postgres://ynnpueixqcogzi:20bf6125162888bc438b6a2ee909d3d145e1c36a250c05c464618f7c7bcddcd4@ec2-35-174-56-18.compute-1.amazonaws.com:5432/dnkpt83fikbov'
app.config["SQLALCHEMY_DATABASE_URI"] = database_path

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
