# importing lib

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import requests
import base64


# Setting up client for spotify api


#PLEASE ENTER YOUR OWN client_id and client_secret see (guide.txt for help)

client_id = '5fca1c7bb348462aa06215d155953a50'
client_secret = '8f4c16e4d7aa476ab71305973df02fa6'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# default parameters and functions
popular_tracks = sp.playlist_tracks('5S8SJdl1BDc0ugpkEvFsIL') # seed playlist or Primary data


def calculate_cosine_similarity(user_features, track_features):

    # calculating cosine similarity using audio featutes danceability, energy and valence

    user_features = [user_features[1]['danceability'], user_features[1]['energy'], user_features[1]['valence']]
    track_features = [track_features['danceability'], track_features['energy'], track_features['valence']]
    return cosine_similarity([user_features], [track_features])[0][0]


# model 

class model:
    
    def get_audio_features(track_uris):
        audio_features = []
        for uri in track_uris:
            track_id = uri
            track_features = sp.audio_features(track_id)
            if track_features:
                audio_features.append(track_features[0])
        return audio_features
    
    def similarity_matrix(user_audio_features):
        similarities = []
        for track in popular_tracks['items']:
            track_audio_features = sp.audio_features(track['track']['uri'])[0]
            similarity = calculate_cosine_similarity(user_audio_features, track_audio_features)
            similarities.append((track['track']['name'], track['track']['artists'][0]['name'], similarity))
            similarities.sort(key=lambda x: x[2], reverse=True)

        return similarities
        
    def recommend_song(similarities):
        rmm = []
        for track in similarities[:5]:
            rmm.append([str(track[0]), str(track[1])])
            #print(f"Track: {track[0]}, Artist: {track[1]}, Similarity: {track[2]:.2f}")        
        return rmm    

# accesblity class help us to get uri of the input songs by the users which help us to get audio features to generate cosine similarity

class accesbilty:

    def find_uri(song):

        client_credentials = f'{client_id}:{client_secret}'
        base64_encoded_client_credentials = base64.b64encode(client_credentials.encode()).decode('utf-8')


        token_url = 'https://accounts.spotify.com/api/token'
        token_data = {
            'grant_type': 'client_credentials',
        }

        token_headers = {
            'Authorization': f'Basic {base64_encoded_client_credentials}',
             
        }

        token_response = requests.post(token_url, data=token_data, headers=token_headers)
        token_data = token_response.json()
        access_token = token_data['access_token']

        search_url = 'https://api.spotify.com/v1/search'
        search_params = {
            'q': song,
            'type': 'track',
        }

        search_headers = {
            'Authorization': f'Bearer {access_token}',
        }

        search_response = requests.get(search_url, params=search_params, headers=search_headers)
        search_data = search_response.json()

        if search_data['tracks']['total'] > 0:
            
            song_uri = search_data['tracks']['items'][0]['uri']
            return song_uri

        else:
            print('Song not found on Spotify')




