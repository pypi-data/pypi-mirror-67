'''
run 'flask run'
instead of 'python3 __init__.py'
'''
import random
import string
import logging
from flask import Flask, g
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    filemode='w',
    format='%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
)

logger = logging.getLogger(__name__)

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # configurations
    secretKey = 'thaipw5dc2cq3wm7qoiqd'
    app.config['JWT_SECRET_KEY'] = secretKey
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../vat.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False

    # this step is required to initialize databse
    app.app_context().push()

    # database
    db.init_app(app)
    import flaskr.model
    db.create_all()

    # jwt token manager
    JWTManager(app)

    # blueprints
    from flaskr.action import user_action, comment_action, video_action
    app.register_blueprint(user_action.bp)
    app.register_blueprint(comment_action.bp)
    app.register_blueprint(video_action.bp)

    return app
