import requests

media_path = 'media/zomato.txt'
# Upload media in chunks
chunk_size = 1024  # 4 MB per chunk
with open(media_path, 'rb') as file:
    chunk_index = 0
    while True:
        chunk_data = file.read(chunk_size)  # Read a chunk of the file
        if not chunk_data:
            break  # Break the loop if no more data
        print(chunk_data)
        print("emtpy line")
        # chunk_index += 1