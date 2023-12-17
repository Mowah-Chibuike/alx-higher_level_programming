#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    if len(argv) > 3:
        user = argv[1]
        password = argv[2]
        database = argv[3]

        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=user,
                passwd=password,
                db=database
        )

        cur = db.cursor()
        cur.execute(
                """
SELECT * FROM states ORDER BY id
                """
        )

        results = cur.fetchall()
        for state in results:
            print(state)

        cur.close()
        db.close()
    else:
        print('Not enough arguments!!\n\
Usage: script mysql_username mysql_password dbname')
