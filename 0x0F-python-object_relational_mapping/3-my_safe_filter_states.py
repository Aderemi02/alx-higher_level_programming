#!/usr/bin/python3
"""
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument
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
            "SELECT * FROM states WHERE name LIKE %s", {argv[4], }
            )
    row = dbcursor.fetchall()

    for line in row:
        print(line)
    dbcursor.close()
    dbcon.close()
