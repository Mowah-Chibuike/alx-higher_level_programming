#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    from sys import argv
    from MySQLdb import connect

    username = argv[1]
    password = argv[2]
    dbname = argv[3]
    state_name = argv[4]

    db = connect(host="localhost", user=username, password=password,
                 database=dbname, port=3306)
    cur = db.cursor()
    cur.execute("ALTER TABLE states\
                 CONVERT TO CHARACTER SET utf8mb4\
                 COLLATE utf8mb4_bin")
    cur.execute("SELECT * FROM states\
                WHERE states.name='{}'\
                ORDER BY states.id".format(state_name))
    res = cur.fetchall()
    for row in res:
        print(row)

    cur.close()
    db.close()
