import requests
import math
import re
from bs4 import BeautifulSoup

ROOT_URL = "http://nces.ed.gov/collegenavigator"
INDEX_URL = ROOT_URL + "?s=all&l=93&ct=2&ic=1&an=5&ax=50"  
PAGINATION_DIV_ID = "ctl00_cphCollegeNavBody_ucResultsMain_divMsg"


def get_num_pages(pagination):
	"""Returns the total number of pages given pagination string
	:param pagination: Pagination string (i.e.: 1-20 of 100 Results)
	"""
	words = pagination.split()
	per_page = int(words[0][2:])
	total = int(words[2])
	pages = total / per_page
	# Add one if pages doesn't divide evenly
	if total % per_page != 0:
		pages = pages + 1
	return pages

def is_college_link(href):
	"""Returns whether or not an anchor is a college link
	:param href: hyperlink string
	"""
	return href and re.compile("id=").search(href)

def get_colleges():
	response = requests.get(INDEX_URL)
	soup = BeautifulSoup(response.text, "html.parser")

	# Get the total number of pages in the result
	pagination = soup.find("div", attrs={"id": PAGINATION_DIV_ID})
	pages = get_num_pages(pagination.get_text())

	# Store colleges in list of dictionaries
	colleges = []
	college = {}

	# Iterate over all of the pages
	for i in range(1, pages+1):
		print("Parsing colleges page: " + str(i))
		response = requests.get(INDEX_URL + "&pg=" + str(i))
		soup = BeautifulSoup(response.text, "html.parser")

		# There is only one "resultsTable" in the HTML that 
		# contains the list of college links and information 
		table = soup.find("table", attrs={"class": "resultsTable"})
        	for link in table.findChildren(href=is_college_link):
			college['name'] = link.get_text()
			college['url'] = link.get('href')
			colleges.append(college.copy())

	return colleges

def get_college_scholarship_data(college):
	"""Retrieves college scholarship data and adds to college
	:param college: college dictionary container
	"""
	response = requests.get(ROOT_URL + college['url'])
	soup = BeautifulSoup(response.text, "html.parser")

	finaid = soup.find("div", attrs={"id": "finaid"})
	table = finaid.find("tbody")

	try:
		# Get Grant-scholarship aid info 
		row = table.find(string="Grant or scholarship aid").parent.parent
		cols = row.find_all("td")
		college['Percent receiving Grant or scholarship aid'] = cols[2].get_text()


		row = table.find(string="Grant or scholarship aid").parent.parent
		cols = row.find_all("td")
		college['Grant-scholarship-aid average'] = cols[4].get_text()

		row = table.find(string="Institutional grants or scholarships").parent.parent
		cols = row.find_all("td")
		college['Percent receiving Institutional grants or scholarships average'] = cols[2].get_text()

		row = table.find(string="Institutional grants or scholarships").parent.parent
		cols = row.find_all("td")
		college['Institutional grants or scholarships average'] = cols[4].get_text()

	except (AttributeError, TypeError):
		print('\033[93m' + college['name'] + " has no scholarship data, skipping!!" + '\033[0m')
		college['Percent receiving Grant or scholarship aid'] = "-"
		college['Grant-scholarship-aid average'] = "-"
		college['Percent receiving Institutional grants or scholarships average'] = "-"
		college['Institutional grants or scholarships average'] = "-"

# Get initial list of colleges and links
print("Getting initial list of colleges")
colleges = get_colleges()

# Get additional scholarship data for each college
for college in colleges:
	print(college['name'] + ": Retrieving scholarship data")
	get_college_scholarship_data(college)

for college in colleges:
	print(repr(str(college['name'])) + ", " + college['Percent receiving Grant or scholarship aid'] + ", " + college['Grant-scholarship-aid average'] + ", " + college['Percent receiving Institutional grants or scholarships average'] + ", " + college['Institutional grants or scholarships average'])

# 	