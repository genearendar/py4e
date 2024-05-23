import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # type: ignore
first_url = 'http://py4e-data.dr-chuck.net/known_by_Abar.html'

#Function to find the name and the new link
def get_link(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    soup_links = soup('a')
    print(soup_links[position-1].text)
    next_url = soup_links[position-1]['href']
    return next_url

#Run the function with initial url first and with new url afterwards

try:
    count = int(input('Count:'))
    position = int(input('Position:'))
except:
    print('Invalid number')
for i in range(count):
    if i == 0:
        current_url = first_url
    current_url = get_link(current_url)