#! /user/bin/python# -*- coding: utf8 -*-
import sqlite3 as lite
import sys

con = lite.connect('db/public_universities.db')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM Public")
	rows = cur.fetchall()
	# for row in rows:
	# 	print(row)

	cur.execute("SELECT COUNT(*) FROM Public")
	item_count = cur.fetchall()
	print("There are %s four-year Public Universities (admission between 5 to 50 percent)" % (item_count[0]))

	cur.execute("SELECT COUNT(*) FROM Public WHERE (in_state_change>0)")
	increase_item_count = cur.fetchall()
	for school in increase_item_count:
		print("{0} of those universities increased their tuition from 2013/2014 to 2014/2015 academic years.".format(school[0]))

	cur.execute("SELECT AVG(in_state_change) FROM Public")
	average_in_state_change = cur.fetchall()
	for Public in average_in_state_change:
		print("Average in-state tuition change from 2013/2014 to 2014/2015: {0}%".format(Public[0]))

	cur.execute("SELECT AVG(out_state_change) FROM Public")
	average_out_state_change = cur.fetchall()
	for Public in average_out_state_change:
		print("Average out-of-state tuition change from 2013/2014 to 2014/2015: {0}%".format(Public[0]))

	print(average_out_state_change)

	cur.execute("SELECT id, MIN(in_state_change) FROM Public")
	min_in_statechange = cur.fetchall()
	for Public in min_in_statechange:
		print("Lowest in-state tuition change from 2013/2014 to 2014/2015: {0} at {1}%".format(Public[0], Public[1]))

	cur.execute("SELECT id, MIN(out_state_change) FROM Public")
	min_out_statechange = cur.fetchall()
	for Public in min_out_statechange:
		print("Lowest out-of-state tuition change from 2013/2014 to 2014/2015: {0} at {1}%".format(Public[0], Public[1]))

	cur.execute("SELECT id, MAX(in_state_change) FROM Public")
	max_in_statechange = cur.fetchall()
	for Public in max_in_statechange:
		print("Highest in-state tuition change from 2013/2014 to 2014/2015: {0} at {1}%".format(Public[0], Public[1]))

	cur.execute("SELECT id, MAX(out_state_change) FROM Public")
	max_out_statechange = cur.fetchall()
	for Public in max_out_statechange:
		print("Highest out-of-state tuition change from 2013/2014 to 2014/2015: {0} at {1}%".format(Public[0], Public[1]))