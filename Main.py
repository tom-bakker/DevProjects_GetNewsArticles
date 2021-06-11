"""Python project to webscrape a Washinton Post page for the article.

"""
from bs4 import BeautifulSoup
import requests
"""Fetches the article contents and title from a URL

Args:
URL : The URL of the article to webscrape.
Returns: String of the title of the article and body of the article.
"""
def get_article(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find('h1')
    body = soup.find('div', class_='article-body')
    formattedText = format_text(body.text)
    return title.text +'\n'+ formattedText
""" Iterates through text and adds a new line to the end of each period.

Args: Text to be formatted with a new line at the end of each period.
Returns: Formatted text
"""
def format_text(text):
    returnText = ''
    for x in text:
        returnText += x
        if x == '.':
            returnText +='\n'
    return returnText
""" Writes text to file passed. 

Args: 
text: The text/string to be added to the file.
fileName: The file name of the file to be written in.
"""
def write_to_file(text, fileName):
    file = open("./" + fileName, "w+")
    file.write(text)
    print("Text written in file: " + fileName)
    file.close()
def main():
    URL = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'
    write_to_file(get_article(URL), "WashingtonPost.txt")
if __name__ =="__main__":
    main()


