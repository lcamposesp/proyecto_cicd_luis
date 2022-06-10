import json
from os import truncate
import requests
from bs4 import BeautifulSoup

#Codigo encargado de hacer el scraping de la pagina web
def scraping_amp_nacionales():
    added_url = 'https://www.crhoy.com/'
    list_titles = []
    dict_titles = {}
    r = requests.get('https://amprensa.com/category/nacionales/')
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)
    s = soup.find('h3', class_='entry-title td-module-title')
    content = s.find_all('a',href=True, title=True)
    print(content)
    

scraping_amp_nacionales()