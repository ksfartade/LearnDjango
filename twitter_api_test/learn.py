import requests
url = "https://mineresume.com/api/accounts/loader_text/jk"
response = requests.get(url = url)

print("Response type: " , type(response))

# response_json = response.json()
# print("Response json type: ", type(response_json))

# print("Response json data: ", response_json)

text_data = response.text
print("Text type: ", type(text_data))

print("Text data: ", text_data)
