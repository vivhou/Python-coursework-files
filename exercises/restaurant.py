#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('restaurant.db')

menu =(
	(1, 'Taco', 5),
	(2, 'Hamburger', 7),
	(3, 'greenbeans', 9),
	(4, 'Ma Po Tofu', 11),
	(5, 'Biryani', 10),
	(6, 'Plantains', 5)

	)

with con: 
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Menu")
	cur.execute("CREATE TABLE Menu(id INT, item TEXT, price INT)")

	cur.executemany("INSERT INTO Menu VALUES(?, ?, ?)", menu)

