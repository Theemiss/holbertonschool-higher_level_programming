#!/usr/bin/python3
"""
Module list state
"""
import sys
import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db= sys.argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT id,name FROM states ORDER by id DESC")
row = cur.fetchall()
for r in row:
	print (r)
cur.close()
conn.close()
