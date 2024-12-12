import requests
from bs4 import BeautifulSoup

# Étape 1 : Envoyer une requête au site
url = "http://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Étape 2 : Extraire les données
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# Étape 3 : Stocker les données
data = []
for i in range(len(quotes)):
    quote_text = quotes[i].text
    author_name = authors[i].text
    tag_list = [tag.text for tag in tags[i].find_all('a', class_='tag')]
    data.append({"quote": quote_text, "author": author_name, "tags": tag_list})

# Étape 4 : Afficher les données
for item in data:
    print(f"Citation: {item['quote']}")
    print(f"Auteur: {item['author']}")
    print(f"Tags: {', '.join(item['tags'])}")
    print('-' * 50)
