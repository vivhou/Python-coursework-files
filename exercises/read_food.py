#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('restaurant.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM Menu")
	rows = cur.fetchall()
	for row in rows:
		print(row)

	cur.execute("SELECT COUNT(*) FROM Menu")
	item_count = cur.fetchall()
	print("There are %s items on the Menu" % (item_count[0]))

	cur.execute("SELECT AVG(Price) FROM Menu")
	average_price = cur.fetchall()
	print("The average price is %s" % (average_price[0]))

	cur.execute("SELECT SUM(Price) FROM Menu")
	sum_price = cur.fetchall()
	print("If you ordered everything , it would cost %s" %(sum_price[0]))

	cur.execute("SELECT MIN(Price) FROM Menu")
	min_price = cur.fetchall()
	print("The minimum price is %s" %(min_price[0]))

	cur.execute("SELECT MAX(Price) FROM Menu")
	max_price = cur.fetchall()
	print("The max price is %s" %(max_price[0]))