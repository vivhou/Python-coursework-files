import csv
with open('example.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		print(row)
		print("Name is %s" % (row[0]))
		for item in row:
			print(item)