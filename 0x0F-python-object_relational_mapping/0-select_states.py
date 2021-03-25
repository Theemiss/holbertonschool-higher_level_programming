#!/usr/bin/python3
"""
Module list state
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
    query = "SELECT id,name FROM states ORDER by id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for r in row:
        print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
