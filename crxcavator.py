import requests
from api import crx_key

key = crx_key()

api_url = 'https://api.crxcavator.io/v1/submit'

headers = {
    'APIKey': key,
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

params = {
    "extension_id": "ajanlknhcmbhbdafadmkobjnfkhdiegm"
}

response_info = requests.post(url = api_url, headers = headers, data = params)

# with open ('crxcavator_api.json', 'r') as file:
#     response_info = json.load(file)

print(response_info.text)
