from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


#wherever the __init__.py file is, the whole folder becomes a package and we can import anything in this file

#initializing Flask
def create_app():
    app = Flask(__name__)

    #secure cookies and session data
    app.config['SECRET_KEY'] = 'asdasd' #secret key for the app

    # stores the database in the website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # initializing database
    db.init_app(app)

    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    # loading users using their id
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')



