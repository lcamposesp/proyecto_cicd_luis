from cmath import log
import json
from operator import add
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
    dict_content = dict()
    r = requests.get('https://www.nacion.com/puro-deporte/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    added_content = s.find_all('p')
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    key_more_content = 1
    for item in added_content:
        dict_content[key_more_content] = item.text
        key_more_content+=1
    print(dict_content)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    set_more_content = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    for key,val in dict_content.items():
        set_more_content.append(val)
    print(set_more_content)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
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
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
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
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
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
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
    return content_to_render

def scraping_nacion_economia_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    r = requests.get('https://www.nacion.com/economia/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
    return content_to_render

def more_content_deportes():
    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.nacion.com/puro-deporte/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='results-list-container')
    content = s.find_all('a',href=True,title=True)
    added_content = s.find_all('p')
    #Adding items from the content scraping
    key=1
    for item in content:
        dict_titles[key] = item['title']
        dict_url[key] = item['href']
        key += 1
    key_more_content = 1
    for item in added_content:
        dict_content[key_more_content] = item.text
        key_more_content+=1
    print(dict_content)
    # Cleanup of duplicate results
    # This currently works for the titles being returned correctly but not the actual links, which are WIP   
    temp = []
    res_titles = dict()
    for key,val in sorted(dict_titles.items()):
        if val not in temp:
            temp.append(val)
            res_titles[key] = val
    temp_url = []
    res_url = dict()
    for key,val in sorted(dict_url.items()):
        if val not in temp_url:
            temp_url.append(val)
            res_url[key] = val
    set_titles = list()
    set_url = list()
    set_more_content = list()
    for key,val in res_titles.items():
        set_titles.append(val)
    for key,val in res_url.items():
        set_url.append(val)
    for key,val in dict_content.items():
        set_more_content.append(val)
    print(set_more_content)
    # Uncomment the lines below for debugging more the assigment of titles to urls
    # Content to render is using a zip method, which combines two lists to a single dictionary creating a key,val association between the values of each 
    # print(set_titles)
    # print(set_url)
    content_to_render = dict(zip(set_titles,set_url))
    return set_more_content