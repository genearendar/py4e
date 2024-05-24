import urllib.request
import re
import xml.etree.ElementTree as ET

#check if the url is valid
def is_valid_url(url):
    return re.search(r'^https?://[^\s/$.?#].[^\s]*$', url) is not None

#enter url and limit failed attempts to 3
def input_url(max_attempts = 3):
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

def read_url():
    ''' Reads the url, parces XML, finds numbers 
    and calculates their sum '''

    try:
        url_data = urllib.request.urlopen(input_url()).read()
    except:
        print("Can't open url")
        return None
    tree = ET.fromstring(url_data)
    comments_lst = tree.findall('comments/comment')
    count_lst = [int(comment.find('count').text) for comment in comments_lst]
    return sum(count_lst)

print(read_url())




