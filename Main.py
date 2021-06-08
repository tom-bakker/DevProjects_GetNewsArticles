"""Python project to webscrape particular news websites for articles.

"""
from bs4 import BeautifulSoup
import requests
"""Fetches the article contents and title from a URL

Args:
URL : The URL of the article to webscrape.
"""
def get_article(URL):
    #TODO: Make it so that any News Article URL can be inserted and the program can find the article.
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1')
    body = soup.find('div', class_='article-body')
    #TODO:Add print to csv file so it can be better utilised.
    print(title.text)
    print(body.text)
def main():
    URL = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'
    get_article(URL)
if __name__ =="__main__":
    main()


