#!/usr/bin/python3
""" Script thak takes in an argument and displays all values in the states
    table of 'hbtn_0e_0_usa' where name matches the argument. """

import MySQLdb
import sys

argv = sys.argv

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="nochetriste11021",     # password
                     db="hbtn_0e_4_usa",
                     port=3306)   # name of the database
cur = db.cursor()

cur.execute("""SELECT cities.id, cities.name, states.name
               FROM cities INNER JOIN states
               ON cities.state_id = states.id
               ORDER BY cities.id ASC;""");

for row in cur.fetchall():
    print(row)
cur.close()
