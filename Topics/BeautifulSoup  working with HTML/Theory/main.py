import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
r = requests.get(url)
bs = BeautifulSoup(r.content, 'html.parser')
bsa = bs.find_all('a', {'entity' in 'href', 'topic' in 'href'})
print([x.text for x in bsa if x.text.startswith(letter) and len(x.text) > 1])
#  You can experiment here, it won’t be checked

