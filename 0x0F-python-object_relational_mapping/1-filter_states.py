#!/usr/bin/python3
"""
Module list state where name start with N
"""
import sys
import MySQLdb


def main():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
