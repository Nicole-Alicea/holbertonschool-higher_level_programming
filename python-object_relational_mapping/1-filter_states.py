#!/usr/bin/python3
'''This script lists all of the states that start with
    uppercase "N" from the database "hbtn_0e_0_usa"
'''


import MySQLdb
from sys import argv


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE BINARY 'N%' \
                   ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for x in rows:
        print(x)

    cursor.close()
    db.close()
    