import json
import requests
from pprint import pprint


page = 1
total_pages = 1

api_key = 'api_key'
field_params= '2'
#field_params_2 = 'University'
endpoint = 'https://api.data.gov/ed/collegescorecard/v1/schools'


def harvest_page(page):
	query_params = {
	'school.ownership': field_params, 
	'api_key': api_key,
	'page': page,
	'_per_page': 50,
	#'_fields': 'school.name, completion.title_iv.low_inc.completed_by.4yrs'
	}

	response = requests.get(endpoint, params = query_params)

	data = response.json()
	#print(data)

	total = data['metadata']['total']


	page = int(data['metadata']['page']) + 1
	per_page = data['metadata']['per_page']
	total_pages = float(total/per_page)

	#print(page, per_page, total_pages)

 	return page, total_pages
	while page <= total_pages:
		page, total_pages = harvest_page(page)

def get_results():
	results = []
	result = {}

def get_debt(result):
 	try:
 		result['low_income'] = school['2013']['aid']['median_debt']['income']['30001_75000']
	except KeyError, e:
 		retrieve_data = "null"
 	
results = get_results()

for result in results:
	print(results['low_income'])

 	



#print data_list
#for info in data_list:
#	print("Name: %s, Percentage: %s" % (region['name'], region['percentage_low_income']))
