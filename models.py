import datetime
from peewee import *
from flask_login import UserMixin
import os from playhouse.db_url 
import multiprocessing.connect

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get
        ('DATABASE_URL'))
    else DATABASE = PostgresqlDatabase('Spotless_app')

Class User(UserMixin, Model):
    username = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField()
    
    class Meta:
        database = DATABASE
        
    class Playlist(Model):
        name = CharField()  
        owner = ForeignKeyField(User, backref = 'tracks')
        
    class Meta:
            database = DATABASE
            
    def initialize():
        DATABASE.connect()
        DATABASE.create_tables([User, Track], 
        safe=True)
        print('Tables Created')
        DATABASE.close()