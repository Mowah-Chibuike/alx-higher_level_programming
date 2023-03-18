#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    from MySQLdb import connect

    if (len(argv) == 4):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        db = connect(host="localhost", port=3306, user=username,
                             password=password, database=dbname)
        cursor = db.cursor()
        cursor.execute("""SELECT cities.id, cities.name, states.name\
                       FROM states\
                       INNER JOIN cities ON states.id = cities.state_id\
                       ORDER BY cities.id""")
        res = cursor.fetchall()
        for row in res:
            print(row)
