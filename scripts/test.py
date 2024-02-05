import requests
from bs4 import BeautifulSoup
import csv

def google_search_first_company_url(keyword):
    headers = {'User-Agent': 'Mozilla/5.0'}
    google_search_url = f'https://www.google.com/search?q={keyword}'
    response = requests.get(google_search_url, headers=headers)
    print(response.text)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Busca el primer resultado de búsqueda. Este selector podría necesitar actualizaciones.
        first_result = soup.find('div', class_='tF2Cxc')
        if first_result:
            link = first_result.find('a', href=True)
            if link:
                return link['href']
    return None

def save_urls_to_csv(keywords, filename='company_urls.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Keyword', 'URL'])
        for keyword in keywords:
            url = google_search_first_company_url(keyword)
            print(f'Keyword: {keyword} - URL: {url}')
            writer.writerow([keyword, url])

# Lista de palabras clave para buscar
keywords = ['OpenAI', 'Google AI', 'Microsoft AI']

#save_urls_to_csv(keywords)


import requests
from bs4 import BeautifulSoup

# Reemplaza 'url_de_la_pagina' con la URL de la página que deseas analizar
url = 'https://www.google.com/search?q=OpenAI'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

urls_http = []

# Busca todas las etiquetas <a>, extrae los atributos 'href' que comiencen con "http://"
for link in soup.find_all('a', href=True):
    if link['href'].startswith('/url?q=http://'):
        urls_http.append(link['href'])

# Imprime las URLs que comienzan con "http://"
for url in urls_http:
    print(url)
