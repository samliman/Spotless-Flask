#initialize Flask instance
from flask import Flask, jsonify, g
from flask_cors import CORS
import os 
app = Flask(__name__)
app.secret_key = 'clandestine'
import models

# Set up Connection and close logic
@app.before_request
def before_request():
    """Connect to the db"""
    g.db = models.DATABASE
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response

#  URL
@app.route('/')
def index():
    return 'Heyo!'

# Run app on start
DEBUG = True
PORT = 8000
if __name__== '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)