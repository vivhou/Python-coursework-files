import csv

with open('eggs.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['a1', 'b1', 'c1'])
	writer.writerow(['a2', 'b2', 'c2'])
	writer.writerow(['a3', 'b3', 'c3'])
	