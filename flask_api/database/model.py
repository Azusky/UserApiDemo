from enum import unique
from .db import db

class User(db.Document):
    email = db.StringField(required=True,unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
