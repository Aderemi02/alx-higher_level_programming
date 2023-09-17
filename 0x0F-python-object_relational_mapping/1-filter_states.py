#!/usr/bin/python3
"""
 a script that lists all states with a name starting with
 N (upper N) from the database hbtn_0e_0_usa
 """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    a script that lists all states from the database hbtn_0e_0_usa
    N (upper N) from the database hbtn_0e_0_usa
    """
    dbcon = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    dbcursor = dbcon.cursor()
    dbcursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
                    'N%' ORDER BY states.id"
            )
    row = dbcursor.fetchall()

    for line in row:
        print(line)
    dbcursor.close()
    dbcon.close()
