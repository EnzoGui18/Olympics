import requests
from bs4 import BeautifulSoup
from .models import Country, Sport, Medal

def scrape_medals():
    url = 'https://olympics.com/pt/paris-2024/medalhas'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Exemplo fictício de scraping de países e medalhas
    countries_data = soup.find_all('div', class_='country-medal-row')
    for country_data in countries_data:
        country_name = country_data.find('span', class_='country-name').text
        gold = int(country_data.find('span', class_='gold-medal').text)
        silver = int(country_data.find('span', class_='silver-medal').text)
        bronze = int(country_data.find('span', class_='bronze-medal').text)

        country, created = Country.objects.get_or_create(name=country_name)
        country.gold_medals = gold
        country.silver_medals = silver
        country.bronze_medals = bronze
        country.save()
