from flask import Blueprint, jsonify
from b_app import app, db
from b_app.models import Song, User
from flask_login import login_required, current_user
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


routes = Blueprint('routes'. __name__)


@routes.route('/songs')
@login_required
def get_songs():
    songs = Song.query.all()
    return jsonify([{'title': song.title, 'artist': song.artist, 'album': song.album} for song in songs])

@routes.route('/recommendations')
@login_required
def get_recommendations():
    user_songs = Song.query.filter_by(user_id=current_user.id).all()
    if not user_songs:
        return ([])

    user_feats = np.array([np.fromstring(song.feats, sep=',') for song in user_songs])
    a_songs = Song.query.all()
    a_feats= np.array([np.fromstring(song.feats, sep=',') for song in a_songs])

    similarities = cosine_similarity(user_feats, a_feats)
    recommendations = []
    for index in np.argsort(-similarities, axis=1)[:10].flatten():
        song = a_songs[index]
        recommendations.append({'title': song.title, 'artist': song.artist, 'album': song.album})
    return jsonify(recommendations)
