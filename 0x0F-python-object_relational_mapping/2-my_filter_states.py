#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    if len(argv) > 3:
        user = argv[1]
        password = argv[2]
        database = argv[3]
        name_search = argv[4]

        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=user,
                passwd=password,
                db=database
        )

        cur = db.cursor()
        query = """SELECT * FROM states WHERE BINARY name = "{}" ORDER BY id"""
        cur.execute(query.format(name_search))

        results = cur.fetchall()
        for state in results:
            print(state)

        cur.close()
        db.close()
    else:
        print('Not enough arguments!!\n\
Usage: script mysql_username mysql_password dbname')
