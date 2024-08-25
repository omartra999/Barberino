from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique = True, nullable=False)
    email = db.Column(db.String(255),unique = True, nullable=False)
    password = db.Column(db.String(255),unique = True, nullable=False)
    location = db.Column(db.String(255))
    confirmed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, server_default=func.now(), nullable=False)


    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password_hash(self, password_hash):
        return check_password_hash(self.password, password_hash)
    
    def __init__(self, first_name, last_name, email, username, password):
        self.firstname = first_name
        self.lastname = last_name
        self.username = username
        self.set_password(password)
        self.email = email


class Barber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255),unique = True, nullable=False)
    password = db.Column(db.String(255),unique = True, nullable=False)
    services = db.Column(db.String(255))
    location = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP, server_default=func.now(), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password_hash(self, password_hash):
        return check_password_hash(self.password, password_hash)
    
    def __init__(self, username):
        self.username = username
 