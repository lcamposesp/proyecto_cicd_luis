import json
import requests
from bs4 import BeautifulSoup

#Codigo encargado de hacer el scraping de la pagina web
def scraping_nacion_deportes():
    added_url = 'https://www.nacion.com/'
    list_titles = []
    r = requests.get('https://www.nacion.com/puro-deporte/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    key = 1
    for titles in content:
        list_titles.append(titles['title'] +'Fuente: '+ added_url+ titles['href'])
        key+=1
    return list_titles

def jsonify_titles(list_with_titles):
    print(list_with_titles)

jsonify_titles(scraping_nacion_deportes())

