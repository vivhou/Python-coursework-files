import requests
from BeautifulSoup import BeautifulSoup 
import csv

result = requests.get("https://www.congress.gov/resources/display/content/Most-Viewed+Bills")

soup= bs4.BeautifulSoup(result.text)

table_section = soup.find('div', {'id': 'main'})

bill_links = []
popularity = {}

for link in table_section('a'):
	href = link['href']
	bill_links.append([link.text, link['href']])

	if href in popularity:
		popularity[href] += 1

	else:
		popularity[href] = 1
print(popularity)