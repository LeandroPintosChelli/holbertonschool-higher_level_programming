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
    cursor.execute("""SELECT cities.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.states_id
                    WHERE states.name LIKE %s
                    ORDER BY cities.id ASC""", (argv[4]))
    print(", ".join([ct[2] for ct in cursor.fetchall() if ct[4] == argv[4]]))
