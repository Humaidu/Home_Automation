
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    contact = db.Column(db.String(16), unique = True, nullable = False)
    password = db.Column(db.String(16), nullable = False)


    