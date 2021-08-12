import os 

database_path = os.getenv('SQLALCHEMY_DATABASE_URI')

if database_path == '':
    database_path = "postgres://ynnpueixqcogzi:20bf6125162888bc438b6a2ee909d3d145e1c36a250c05c464618f7c7bcddcd4@ec2-35-174-56-18.compute-1.amazonaws.com:5432/dnkpt83fikbov"

