from spotify import spotipy
from spotify.oauth2 import SpotifyClientCredentials
from b_app.models import Song
from b_app import db
import numpy as np


def spotify_songs():
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(
        c_id='spotify_id',
        c_secret='spotify_secret'
        ))

    results = sp.search(q='genre:pop', limit=50)
    for item in results ['tracks']['items']:
        title = item['name']
        artist = item['artists'][0]['name']
        album = item['album']['name']
        features = np.random.rand(10)
        feats_str = ','.join(map(str, features))

        n_song = Song(title=title, artist=artist, album=album, features=feats_str)
        db.session.add(n_song)
        db.session.commit()
