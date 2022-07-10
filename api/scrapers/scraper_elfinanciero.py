from cmath import log
import json
from operator import add
import requests
from bs4 import BeautifulSoup

def scraping_elfinanciero_economia_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/economia-y-politica/')
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

# Methods that are also being used
# The methods are in charge of crawling the same sites as the methods above but return a simple list with the extra content missed in the <p> tags. 
def more_content_economiaef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/economia-y-politica/')
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
    return set_more_content

def scraping_elfinanciero_opinion_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/opinion/')
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

def more_content_opinionef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/opinion/')
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
    return set_more_content

def scraping_elfinanciero_pymes_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/pymes/')
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

def more_content_pymesef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/pymes/')
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
    return set_more_content

def scraping_elfinanciero_tecnologia_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/tecnologia/')
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

def more_content_tecnologiaef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/tecnologia/')
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
    return set_more_content


def scraping_elfinanciero_gerencia_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/gerencia/')
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

def more_content_gerenciaef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/gerencia/')
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
    return set_more_content

def scraping_elfinanciero_negocios_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/negocios/')
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

def more_content_negociosef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/negocios/')
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
    return set_more_content

def scraping_elfinanciero_finanzas_for_index():
    #This is the method that will return the relevant titles and URLs to the front end that gets displayed in home
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/finanzas/')
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

def more_content_finanzasef():

    # THIS NEEDS A LITTLE BIT OF CLEANING SINCE NOT ALL LINES ARE USED OR EVEN NEED TO BE CALLED. MOSTLY LINES THAT DO NOT FOCUS ON THE EXTRA CONTENT ADDED
    # This method will return a list with the extra content missed from the pages below
    dict_titles = {}
    dict_url = {}
    dict_content = dict()
    r = requests.get('https://www.elfinancierocr.com/finanzas/')
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
    return set_more_content