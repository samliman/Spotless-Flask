from flask import request, jsonify, Blueprint
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

playlists = Blueprint('playlists', 'playlists')

# Create route
@playlists.route('/create', methods=["POST"])
@login_required
def create_playlist():
    try:
        payload = request.get_json(force = True)
        payload['created_by'] = current_user.id
        playlist = models.Playlist.create(**payload)
        print(playlist.__dict__)
        print(dir(playlist)) #########################
        playlist_dict = model_to_dict(playlist)

        return jsonify(data = playlist_dict, status = {"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error creating the resources"})


# Show route
@playlists.route('/<id>', methods=["GET"])
def get_one_playlist(id):
    try:
        playlist = models.Playlist.get_by_id(id)
        print(playlist)
        playlist_dict = model_to_dict(playlist)
        return jsonify(data = playlist_dict, status={"code": 200, "message": f"Found playlist with id {playlist.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting one resource"})

# Update route
@playlists.route('/<id>', methods=["PUT"])
def update_playlist(id):
    try:
        payload = request.get_json()
        payload['owner']=current_user.id
        query = models.Playlist.update(**payload).where(models.Playlist.id == id)
        query.execute()
        updated_playlist = model_to_dict(models.Playlist.get_by_id(id))
        return jsonify(data=updated_playlist, status={"code": 200, "message": f"Resource updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error updating one resource"})


# Delete route
@playlists.route('/<id>', methods=["DELETE"])
def delete_playlist(id):
    try:
        query = models.Playlist.delete().where(models.Playlist.id == id)
        query.execute()
        return jsonify(data='Resource successfully deleted', status={"code": 200, "message": "Resource successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error deleting resource"})
