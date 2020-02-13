import datetime
from flask import Flask, jsonify, g
from flask_login import UserMixin
from peewee import *
# import os from playhouse.db_url
# import multiprocessing.connect

DATABASE =SqliteDatabase('playlists.sqlite')


# if 'ON_HEROKU' in os.environ:
#     DATABASE = connect(os.environ.get
#         ('DATABASE_URL'))
#     else DATABASE = PostgresqlDatabase('Spotless_app')

# Class User(UserMixin, Model):
#     username = CharField(unique = True)
#     email = CharField(unique = True)
#     password = CharField()
#     created_at = DateTimeField(default=datetime.datetime.now)
    
class Meta:
    database = DATABASE
    
class Playlist(Model):
    name = CharField()  
    # owner = ForeignKeyField(User, backref = 'playlists')
    
class Meta:
        database = DATABASE
        
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Playlist], 
    safe=True)
    print('Tables Created')
    DATABASE.close()