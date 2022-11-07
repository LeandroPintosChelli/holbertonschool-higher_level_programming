#!/usr/bin/python3
"""
list all table values (table 'states')
parameters given to script: username, password, database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    database = MySQLdb.connect(user=argv[1],
                               password=argv[2],
                               database=argv[3],
                               host="localhost",
                               port=3306)

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}'ORDER BY id ASC"
        .format(argv[4]))
    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)
