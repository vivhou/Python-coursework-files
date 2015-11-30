import csv

text = """
	<table>
	<thead>
		<th>Resource</th>
		<th>Count</th>
	</thead>
"""

# += adds text to text variable


with open('va.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader: 
		text += "	<tr>"
		for cell in row:
			text += "		<td>%s</td>" % (cell)

		text += "	</tr>"
	

text += '</table>'

with open('va.html', 'w') as html_file:
	html_file.write(text)