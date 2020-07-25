from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
%matplotlib inline

url = "https://www.yelp.ca/search?cflt=restaurants&find_loc=Toronto%2C+ON"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
type(soup)

text = soup.get_text()
title = soup.title
print(title)

all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# soup = BeautifulSoup(yelp_page_source_page1, 'html.parser')
# all = soup.find_all(
#     'li', {'class': 'lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT'})

# for data in all:
#     info_scraped = {}
#     try:
#         base = data.find('h3', {
#                          'class': 'lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp'})
#         number_sequence = base.text[0]
#         if int(number_sequence) in (1, 2, 3, 4, 5, 6, 7, 8, 9):
#             try:
#                 info_scraped['Restaurant Name'] = data.find('h3', {'class': 'lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp'}).find(
#                     'a', {'class': 'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'}).text
#             except:
#                 print(None)
#             try:
#                 info_scraped['Phone Number'] = data.find('div', {'class': 'lemon--div__373c0__1mboc container__373c0__19wDx u-padding-l2 border-color--default__373c0__2oFDT text-align--right__373c0__3fmmn'}).find(
#                     'p', {'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'}).text
#             except:
#                 print(None)
#             try:
#                 info_scraped['Address'] = data.find('div', {'class': 'lemon--div__373c0__1mboc container__373c0__19wDx u-padding-l2 border-color--default__373c0__2oFDT text-align--right__373c0__3fmmn'}).find(
#                     'span', {'class': 'lemon--span__373c0__3997G'}).text
#             except:
#                 print(None)
#             try:
#                 info_scraped['States'] = data.find('div', {'class': 'lemon--div__373c0__1mboc container__373c0__19wDx u-padding-l2 border-color--default__373c0__2oFDT text-align--right__373c0__3fmmn'}).find(
#                     'div', {'class': 'lemon--div__373c0__1mboc display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'}).text
#             except:
#                 print(None)
#             try:
#                 info_scraped['Number of Review'] = data.find(
#                     'div', {'class': 'lemon--div__373c0__1mboc attribute__373c0__1hPI_ display--inline-block__373c0__2de_K border-color--default__373c0__2oFDT'}).text
#             except:
#                 print(None)
#             try:
#                 info_scraped['Image URL'] = data.find(
#                     'img', {'class': 'lemon--img__373c0__3GQUb photo-box-img__373c0__O0tbt'}).get('src')
#             except:
#                 print(None)
#             try:
#                 info_scraped['Category'] = data.find('div', {'class': 'lemon--div__373c0__1mboc largerScrollablePhotos__373c0__3FEIJ arrange__373c0__UHqhV border-color--default__373c0__2oFDT'}).find('div', {'class': 'lemon--div__373c0__1mboc mainAttributes__373c0__1r0QA arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT'}).find(
#                     'div', {'class': 'lemon--div__373c0__1mboc priceCategory__373c0__3zW0R border-color--default__373c0__2oFDT'}).find('span', {'class': 'lemon--span__373c0__3997G display--inline__373c0__1DbOG border-color--default__373c0__2oFDT'}).text
#             except:
#                 print(None)
#             final_data.append(info_scraped)
#     except:
#         continue
