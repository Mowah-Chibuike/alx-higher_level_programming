# 0x0F. Python - Object-relational mapping

## Learning Objectives
### General
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements
### General
- Allowed editors: vi, vim, emacs
- Ubuntu 20.04 LTS using python3 (version 3.8.5)
- MySQLdb version 2.0.x
- SQLAlchemy version 1.4.x
- Your code should use the pycodestyle (version 2.8.*)
- All modules, classes, functions and methods should be properly documented

## Tasks
### Mandatory
- 0-select_states.py: a script that lists all states from the database hbtn_0e_0_usa
- 1-filter_states.py: a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
- 2-my_filter_states.py: a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
- 3-my_safe_filter_states.py: a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument but is safe from SQL injections
- 4-cities_by_state.py: a script that lists all cities from the database hbtn_0e_4_usa
- 5-filter_cities.py: a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
