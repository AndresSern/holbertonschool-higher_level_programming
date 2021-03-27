#!/usr/bin/python3
""" Script that lists all 'states' with a 'name' starting with 'N' from the
    database 'hbtn_0e_usa' """

import MySQLdb
from sys import argv

db = MySQLdb.connect(host = "localhost",  # your host
                     user = argv[1],       # username
                     passwd = argv[2],     # password
                     db = argv[3],
                     port = 3306)   # name of the database
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC;")

for row in cur.fetchall():
    print(row)

cur.close()
