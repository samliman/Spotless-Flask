#initialize Flask instance
from flask import Flask
from flask_cors import CORS
import os 
app = Flask(__name__)
app.secret_key = 'clandestine'


#start the website
app=Flask(__name__)

#  URL
@app.route('/')
def index():
    return 'Heyo!'

# Run app on start
DEBUG = True
PORT = 8000
if __name__== '__main__':
    app.run(debug=DEBUG, port=PORT)