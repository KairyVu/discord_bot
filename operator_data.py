import requests
from bs4 import BeautifulSoup

url = "https://gamepress.gg/arknights/operator/typhon"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
tags = soup.find("div", id="operator-overview")
print(tags.text)