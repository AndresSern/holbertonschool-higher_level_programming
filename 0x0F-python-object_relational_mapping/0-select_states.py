#!/usr/bin/python3
""" Script that lists all 'states' from the database hbtn_0e_0_usa
     Results is showed in ascending order by states.id """

import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="nochetriste11021",     # password
                     db="hbtn_0e_0_usa",
                     port=3306)   # name of the database
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC;")

for row in cur.fetchall():
    print(row)
