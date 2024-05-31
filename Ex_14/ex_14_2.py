import urllib.request, urllib.parse, urllib.error
import re
import json
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()
api_url = 'https://api.geoapify.com/v1/geocode/search'
api_key = os.environ.get('MAP_API_KEY')
print(api_key)
while True:
    input_address = input('Type the address:\nOr type "Quit" to quit: ').lower()
    if input_address == "stop" or input_address == "none" or input_address == "quit":
        break
    params = {
        "text": input_address,
        "apiKey": api_key
    }
    headers = {
        "Accept": "application/json"
    }
    url = f"{api_url}?{urllib.parse.urlencode(params)}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            json_data = json.load(response)
            status_code = response.getcode()
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")

    print(json_data["features"][0]["properties"]["plus_code"])

