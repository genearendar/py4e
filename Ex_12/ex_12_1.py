import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # type: ignore
import re

def enter_url():
    url = input('Enter url:')
    if re.search('^https?://[^\s/$.?#].[^\s]*$', url):
        return url
    else:
        print('Not a valid url')
        enter_url()
url = enter_url()
try:
    html = urllib.request.urlopen(url).read()
except:
    print('Can\'t open the url')
    quit()
soup_html = BeautifulSoup(html, 'html.parser')
numbers = soup_html('span')
numbers = [int(number.text) for number in numbers]
print(sum(numbers))



