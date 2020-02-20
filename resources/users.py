from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user

import models

users = Blueprint('users', 'users')

# http://localhost:8000/api/v1/users/register
@users.route('/register', methods = ['POST'])
def register():
    payload = request.get_json(force = True)
    payload['email'].lower()
    print('line 15',payload)
    try:
        models.User.get(models.User.email == payload['email'])

        return jsonify(data={}, status={"code": 400, "message": "A user with that email already exists"})
    
    except models.DoesNotExist:
        payload['password'] = generate_password_hash(payload['password'])
        user = models.User.create(**payload)
        user_dict = model_to_dict(user)
        
        del user_dict['password']
        return jsonify(data=user_dict, status={'code': 200, 'message': f"Successfully registered {user_dict['email']}"})

@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json(force = True)
    payload['email'].lower()
    try:
        user = models.User.get(models.User.email == payload['email'])

        user_dict = model_to_dict(user)
        
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            return jsonify(data = user_dict, status = {'code': 200, 'message': f"Successfully logged in {user_dict['email']}"})

        else:
            return jsonify(data={}, status={'code': 401, 'message': 'Email or password is incorrect'})

    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Email or password is incorrect'})
    
@users.route('/logout', methods = ['GET'])
def logout():
    email = model_to_dict(current_user)['email']
    logout_user()

    return jsonify(data={}, status = { 'code': 200, 'message': f"Successfully logged out {email}"})
    
@users.route('/test', methods = ['GET'])
def test():
    try:
        users = [model_to_dict(user) for user in models.User.select()]
        print(users)
        return jsonify(data=users, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting the resources"})