from app.utils import get_env_variable
from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

if (0):
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PASSWORD = get_env_variable("POSTGRES_PASSWORD")
    POSTGRES_DB = get_env_variable("POSTGRES_DB")
    POSTGRES_URL_BASE = get_env_variable("POSTGRES_URL_BASE")

    DB_URL = '{base}://{user}:{pw}@{url}/{db}'.format(base=POSTGRES_URL_BASE,
        user=POSTGRES_USER, pw=POSTGRES_PASSWORD, url=POSTGRES_URL, db=POSTGRES_DB)
    APP_SECRET = get_env_variable("APP_SECRET")
    REDIS_URL = "redis://{redis_url}/0".format(redis_url=get_env_variable("REDIS_URL"))
else:
    APP_SECRET = 'secret'
    DB_URL = 'postgres://iqqeroltvqorbp:c7410b23004f8591fea855841f37cc22bd3aefcbd35374ee0bb52398078c3199@ec2-174-129-252-228.compute-1.amazonaws.com:5432/d2mraslh5bj3o5'


app = Flask(__name__,static_folder='./static')
app.config['SECRET_KEY'] = APP_SECRET
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['REDIS_URL'] = 'redis://h:p302cc71bf5a28456cf4fa06208bbc2bab6f1b7016979c3e8692f7734b9724a66@ec2-34-199-192-253.compute-1.amazonaws.com:18249'

redis_store = FlaskRedis(app)

from app import models, utils
from app.views import *

@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    from sqlalchemy_utils import database_exists, create_database, drop_database
    if app.debug:
        if database_exists(DB_URL):
            print('Deleting database.')
            drop_database(DB_URL)
        if not database_exists(DB_URL):
            print('Creating database.')
            create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')
