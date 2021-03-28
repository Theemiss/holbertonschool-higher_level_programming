#!/usr/bin/python3
"""
 takes in the name of a state as an argument
 and lists all cities of that state, using the
database hbtn_0e_4_usa
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
    state_name = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_name,))
    row = cur.fetchall()
    re = ""
    for r in row:
        re += r[0] + ", "
    print(re[0:-2:])
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
