#initialize Flask instance
from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
# import os

app = Flask(__name__)
app.secret_key = 'clandestine'

login_manager = LoginManager()
login_manager.init_app(app)

import models
from resources.users import users
from resources.playlists import playlists

CORS(playlists, origin=['http://localhost:3000'], supports_credentials=True)
CORS(users, origin=['http://localhost:3000'], supports_credentials=True)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify(
        data = {
            'error': 'User not logged in.'
        },
        status = {
            'code': 401,
            'message': 'You must be logged in to access that resource.'
        }
    )

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(playlists, url_prefix='/api/v1/playlists')

# Default route
@app.route('/')
def index():
    return 'Heyo!'

# Run app on start
DEBUG = True
PORT = 8000
if __name__== '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)