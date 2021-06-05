from bs4 import BeautifulSoup
import requests
URL = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find('h1')
body = soup.find('div', class_='article-body')
print(title.text)
print(body.text)


