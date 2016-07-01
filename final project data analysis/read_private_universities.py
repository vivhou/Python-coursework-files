#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('db/private_universities.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM Private")
	rows = cur.fetchall()
	for row in rows:
		print(row)

	cur.execute("SELECT COUNT(*) FROM Private")
	item_count = cur.fetchall()
	print("There are %s four-year non-profit Private Universities, with admission rates of 5 to 50 percent." % (item_count[0]))


	cur.execute("SELECT COUNT(*) FROM Private WHERE (tuition_percentage_change>0)")
	increase_item_count = cur.fetchall()
	for school in increase_item_count:
		print("{0} of those universities increased their tuition from 2013/2014 to 2014/2015 academic years.".format(school[0]))


	cur.execute("SELECT AVG(tuition_percentage_change) FROM Private")
	average_tuition_percentage_change = cur.fetchall()
	print("The average percentage change in private tuition from 2013/2014 to 2014/2015 is %s" % (average_tuition_percentage_change[0]) + '%')


	cur.execute("SELECT id, MIN(tuition_percentage_change) FROM Private")
	min_change = cur.fetchall()
	for Private in min_change:
		print("Highest tuition decrease from 2013/2014 to 2014/2015: {0} at {1}%".format(Private[0], Private[1]))


	cur.execute("SELECT id, MAX(tuition_percentage_change) FROM Private")
	max_change = cur.fetchall()
	for Private in max_change:
		print("Highest tuition increase from 2013/2014 to 2014/2015: {0} at {1}%".format(Private[0], Private[1]))

con.close()