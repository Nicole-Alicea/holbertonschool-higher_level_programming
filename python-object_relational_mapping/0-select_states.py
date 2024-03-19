#!/usr/bin/python3
'''This script connects to a MySQL database and lists all of the states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys import argv


if __name__ == '__main__':
    '''Connects to the database and prints out the states'''

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)