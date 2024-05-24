import urllib.request
import re
import json
def is_valid_url(url):
    '''Checking the url formatting
    '''
    return re.search(r'^https?://[^\s/$.?#].[^\s]*$', url) is not None

def input_url(max_attempts = 3):
    '''Limiting the number of failed urls to 3 to break out of app if can't enter
    '''
    fail_count = 0
    while fail_count < max_attempts:
        url = input('Enter url:')
        if is_valid_url(url):
            return url
        else:
            print('Not a valid url. Try again:')
            fail_count += 1
    print('Too many failed attempts')
    return None

def open_url():
    '''Open the url if possible or
    '''
    url = input_url()
    if url is not None:
        try:
            url_data = urllib.request.urlopen(url)
            return url_data
        except:
            print("Can't open url")
            return None
    else:
        quit()

def parse_json_numbers():
    valid_url = open_url()
    if valid_url is not None:
        json_data = json.load(valid_url)
        numbers = [comment['count'] for comment in json_data['comments']]
        return numbers
    else:
        return None

parsed_numbers = parse_json_numbers()
if parsed_numbers is not None:
    print(sum(parsed_numbers))
else:
    print("Parse failed")

