import requests
from requests_oauthlib import OAuth1
import os

# Replace these values with your own
consumer_key = os.getenv('API_KEY')
consumer_secret = os.getenv('API_SECRET')
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)


# Path to the media file you want to upload
media_path = 'media/cute-love.gif'
# Media upload endpoints
media_upload_init_url = 'https://upload.twitter.com/1.1/media/upload.json?command=INIT'
media_upload_append_url = 'https://upload.twitter.com/1.1/media/upload.json?command=APPEND'
media_upload_finalize_url = 'https://upload.twitter.com/1.1/media/upload.json?command=FINALIZE'

# Media file details
total_bytes = os.path.getsize(media_path)
media_type = 'video/mp4'  # or 'image/gif'
media_category = 'dm_video'  # or 'dm_gif'

# Initialize media upload
init_data = {
    'command': 'INIT',
    'total_bytes': total_bytes,
    'media_type': media_type,
    'media_category': media_category
}
init_response = requests.post(media_upload_init_url, auth=auth, data=init_data)
init_response.raise_for_status()
print('Respones: ', init_response)
media_id = init_response.json()['media_id']
print("Media_id: ", media_id)
print("Response data: ", init_response.json())

# Upload media in chunks
chunk_size = 4 * 1024 * 1024  # 4 MB per chunk
with open(media_path, 'rb') as file:
    chunk_index = 0
    while True:
        chunk_data = file.read(chunk_size)
        if not chunk_data:
            break
        files = {'media': chunk_data}
        append_data = {
            'command': 'APPEND',
            'media_id': media_id,
            'segment_index': chunk_index
        }
        append_response = requests.post(media_upload_append_url, auth=auth, data=append_data, files=files)
        append_response.raise_for_status()
        chunk_index += 1

# Finalize media upload
finalize_data = {
    'command': 'FINALIZE',
    'media_id': media_id
}
finalize_response = requests.post(media_upload_finalize_url, auth=auth, data=finalize_data)
finalize_response.raise_for_status()