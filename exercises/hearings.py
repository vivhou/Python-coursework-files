import json
import requests

hearing_list = []
page = 1
total_pages = 1

apikey = 'e938a42c79fb489fad98560d99d5de82'

base_url = 'http://congress.api.sunlightfoundation.com/'
hearings_endpoint = 'hearings'
url = base_url + hearings_endpoint

def harvest_page(page):	
	query_params = {
	'committee_id': 'HSRU', 
	'apikey': apikey,
	'page': page
	}

	response = requests.get(url, params = query_params)

	data = response.json()

	count = data['count']

	page = int(data['page']['page']) + 1
	per_page = data['page']['per_page']

	total_pages = float(count/per_page)
		
	for hearing in data['results']:
		hearing_record = {'description': hearing['description'], 'url': hearing['url']}
		hearing_list.append(hearing_record)
	return page, total_pages

while page <= total_pages:
	page, total_pages = harvest_page(page)

print hearing_list
