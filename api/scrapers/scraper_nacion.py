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

def scraping_nacion_deportes_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    r = requests.get('https://www.nacion.com/puro-deporte/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    print(dict_url)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in dict_titles.items():
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in dict_url.items():
        if val not in temp_url:
            temp.append(val)
            res_url[key] = val
    content_to_render = dict()
    for key,val in res_titles.items():
        for key2,val2 in res_url.items():
            content_to_render[val] = "https://nacion.com"+ val2 
    return content_to_render

def scraping_nacion_elpais_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    r = requests.get('https://www.nacion.com/el-pais/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    print(dict_url)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in dict_titles.items():
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in dict_url.items():
        if val not in temp_url:
            temp.append(val)
            res_url[key] = val
    content_to_render = dict()
    for key,val in res_titles.items():
        for key2,val2 in res_url.items():
            content_to_render[val] = "https://nacion.com"+ val2 
    return content_to_render

def scraping_nacion_mundo_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    r = requests.get('https://www.nacion.com/el-mundo/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    print(dict_url)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in dict_titles.items():
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in dict_url.items():
        if val not in temp_url:
            temp.append(val)
            res_url[key] = val
    content_to_render = dict()
    for key,val in res_titles.items():
        for key2,val2 in res_url.items():
            content_to_render[val] = "https://nacion.com"+ val2 
    return content_to_render

def scraping_nacion_tecnologia_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    r = requests.get('https://www.nacion.com/tecnologia/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    print(dict_url)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in dict_titles.items():
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in dict_url.items():
        if val not in temp_url:
            temp.append(val)
            res_url[key] = val
    content_to_render = dict()
    for key,val in res_titles.items():
        for key2,val2 in res_url.items():
            content_to_render[val] = "https://nacion.com"+ val2 
    return content_to_render