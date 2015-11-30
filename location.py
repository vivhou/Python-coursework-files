import json
import requests
apikey = 'e938a42c79fb489fad98560d99d5de82'

endpoint = 'http://congress.api.sunlightfoundation.com/legislators/locate'

zip_code = raw_input('Give me a zip code')

query_params = {'zip': zip_code, 'apikey': apikey}

response = requests.get(endpoint, params = query_params)

print(response.url)

data = response.json()

for politician in data['results']:
	title = politician['title']
	first_name = politician['first_name']
	last_name = politician['last_name']
	print("%s. %s %s" % (title, first_name, last_name))