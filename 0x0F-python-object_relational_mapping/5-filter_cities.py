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
        state_name = argv[4]

        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=user,
                passwd=password,
                db=database
        )

        cur = db.cursor()
        query = """\
SELECT cities.name FROM cities
INNER JOIN states
ON cities.state_id = states.id
WHERE BINARY states.name = %s
ORDER BY cities.id
"""
        cur.execute(query, (state_name,))

        results = cur.fetchall()
        delim = ''
        for city in results:
            print(delim, end=city[0])
            delim = ', '
        print()

        cur.close()
        db.close()
    else:
        print('Not enough arguments!!\n\
Usage: script mysql_username mysql_password dbname')
