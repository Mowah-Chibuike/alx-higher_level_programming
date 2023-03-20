#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    from sys import argv
    from MySQLdb import connect

    if (len(argv) >= 5):
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        state_name = argv[4]

        db = connect(host="localhost", port=3306, user=username,
                     password=password, database=dbname)
        cursor = db.cursor()
        cursor.execute("""SELECT GROUP_CONCAT(name SEPARATOR ', ')\
                       FROM cities\
                       WHERE state_id = (\
                       SELECT id\
                       FROM states\
                       WHERE name = %s)\
                       ORDER BY id;""", (state_name,))
        res = cursor.fetchone()
        if res and res[0]:
            print(res[0])
        else:
            print()
        cursor.close()
        db.close()