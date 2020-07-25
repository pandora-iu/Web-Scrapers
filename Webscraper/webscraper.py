from bs4 import BeautifulSoup
import requests

url = "https://smartpages.nexpart.com/smartpage.php?mfrlinecode=GKI&partnumber=AF12061"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for data = content.find_All('span', attrs={"class": "lang_en sp_title"}).get_text():
    print(content)
