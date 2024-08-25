from .models import User
from . import db

def user_exists(username):
    return User.query.filter_by(username=username).first() is not None

def email_exists(email):
    return User.query.filter_by(email=email).first() is not None

def add_user(_first_name, _last_name, _username, _email, _password):
    user = User(first_name= _first_name, last_name= _last_name, username= _username, email= _email, password= _password)
    db.session.add(user)
    db.session.commit()
    return user