import requests
import json
from indicter import crx_returned

# extension = "ajanlknhcmbhbdafadmkobjnfkhdiegm"

def crx_report(extension):
    url = "https://api.crxcavator.io/v1/report/{}?platform=Chrome&new_scan=true".format(extension)

    payload = ""
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    crx_returned(extension, response.json())

def crx_meta(extension):
    url = "https://api.crxcavator.io/v1/metadata/{}".format(extension)

    payload={}
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    return False


