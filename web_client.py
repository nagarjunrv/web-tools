import bs4
import requests
from bs4 import BeautifulSoup
import datetime


def chunkstring(string, length):
    words = string.replace('\n', ' ').split(' ')
    return (' '.join(words[0+i:length+i]) for i in range(0, len(words), length))


def get_content(link):
    # Getting the page's source code:
    source = requests.get(link)

    # Creating the BeautifulSoup object:
    source = BeautifulSoup(source.content.decode("utf-8"), "html.parser")

    # Variable that will hold all the text:
    text =  source.text

    text_gen = chunkstring(text.replace(u"\u2019", "'"), 15)
    datestamp = datetime.date.today().strftime("%B %d, %Y").replace(' ', '_').replace(',', '')
    target_file = F'{datestamp}.txt'
    with  open(target_file, "w") as  file:
        for l in text_gen:
            file.write(F'{l}\n')
    return target_file
