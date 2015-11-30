#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('public_universities2.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM Public2")
	rows = cur.fetchall()
	for row in rows:
		print(row)


	cur.execute("SELECT AVG(percent_awarded) FROM Public2")
	average_percent_awarded = cur.fetchall()
	print("The average percentage of students who were awarded with a grant or scholarship (2013-14) among PUBLIC universities was %s" % (average_percent_awarded[0]) + "%")


	cur.execute("SELECT AVG(average_award) FROM Public2")
	average_award_student = cur.fetchall()
	print("The average amount of a grant/scholarship award for a student in public universities (2013-14) was $%s" % (average_award_student[0])) 

con.close()