import requests

from bs4 import BeautifulSoup

num, url = int(input()), input()
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
anchors = soup.find_all('a')
print(anchors[num - 1].get('href'))
