#!/usr/bin/python3
"""
list all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    database = MySQLdb.connect( username=argv[1],
                                password=argv[2],
                                dbname=argv[3],
                                host="localhost",
                                port=3306)

    c = database.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    db= c.fetchall()
    for i in db:
        print(i)
    c.close()
    db.close()