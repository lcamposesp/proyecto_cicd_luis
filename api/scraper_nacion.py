import json
import requests
from bs4 import BeautifulSoup

#Codigo encargado de hacer el scraping de la pagina web
def scraping_nacion_deportes():
    added_url = 'https://www.nacion.com/'
    list_titles = []
    dict_titles = {}
    r = requests.get('https://www.nacion.com/puro-deporte/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    key = 1
    for titles in content:
        list_titles.append('Noticia Deportes: ' + titles['title'] +'Fuente: '+ added_url+ titles['href'])
        key+=1
    key_dict = 1
    for item in list_titles:
        dict_titles[key_dict] = item
        key_dict+=1
    print(dict_titles)
    json_str = json.dumps(dict_titles)
    return json_str

def scraping_nacion_pais():
    added_url = 'https://www.nacion.com/'
    list_titles = []
    dict_titles = {}
    r = requests.get('https://www.nacion.com/el-pais/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    key = 1
    for titles in content:
        list_titles.append('Noticia El Pais: ' + titles['title'] +'Fuente: '+ added_url+ titles['href'])
        key+=1
    key_dict = 1
    for item in list_titles:
        dict_titles[key_dict] = item
        key_dict+=1
    print(dict_titles)
    json_str = json.dumps(dict_titles)
    return json_str

def scraping_nacion_mundo():
    added_url = 'https://www.nacion.com/'
    list_titles = []
    dict_titles = {}
    r = requests.get('https://www.nacion.com/el-mundo/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    key = 1
    for titles in content:
        list_titles.append('Noticia El Mundo: ' + titles['title'] +'Fuente: '+ added_url+ titles['href'])
        key+=1
    key_dict = 1
    for item in list_titles:
        dict_titles[key_dict] = item
        key_dict+=1
    print(dict_titles)
    json_str = json.dumps(dict_titles)
    return json_str

def scraping_nacion_tecnologia():
    added_url = 'https://www.nacion.com/'
    list_titles = []
    dict_titles = {}
    r = requests.get('https://www.nacion.com/tecnologia/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    key = 1
    for titles in content:
        list_titles.append('Noticia Tecnologia: ' + titles['title'] +'Fuente: '+ added_url+ titles['href'])
        key+=1
    key_dict = 1
    for item in list_titles:
        dict_titles[key_dict] = item
        key_dict+=1
    print(dict_titles)
    json_str = json.dumps(dict_titles)
    return json_str