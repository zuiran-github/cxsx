import requests
from bs4 import BeautifulSoup

# url = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-04-20&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG"
url = "https://b2c.csair.com/portal/flight/direct/query"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

r = requests.post(url, {})
# r = requests.get(url, headers=headers)
r.encoding = 'UTF-8'

soup = BeautifulSoup(r.text, "html.parser")
# title = soup.find("title").text

print(soup)