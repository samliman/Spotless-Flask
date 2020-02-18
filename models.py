import datetime

from flask import Flask
from peewee import *
from flask_login import UserMixin
from playhouse.db_url import connect
# import os


DATABASE = SqliteDatabase('spotless.sqlite')
class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = DATABASE

    # Create Tables
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
    