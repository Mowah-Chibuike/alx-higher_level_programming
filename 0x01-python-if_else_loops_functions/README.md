0x00. Python - Hello, World

Learning Objectives
- General
	- Why Python programming is awesome
	- Why indentation is so important in Python
	- How to use the if, if ... else statements
	- How to use comments
	- How to affect values to variables
	- How to use the while and for loops
	- How is Python’s for different from C‘s?
	- How to use the break and continues statements
	- How to use else clauses on loops
	- What does the pass statement do, and when to use it
	- How to use range
	- What is a function and how do you use functions
	- What does return a function that does not use any return statement
	- Scope of variables
	- What’s a traceback
	- What are the arithmetic operators and how to use them

Requirements
- Python Scripts
	- Allowed editors: vi, vim, emacs
	- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/usr/bin/python3
	- Your code should use the pycodestyle (version 2.8.*)
	- All your files must be executable
	- The length of your files will be tested using wc

- Shell Scripts
	- Allowed editors: vi, vim, emacs
	- All your scripts will be tested on Ubuntu 20.04 LTS
	- All your scripts should be exactly two lines long (wc -l file should print 2)
	- All your files should end with a new line
	- The first line of all your files should be exactly #!/bin/bash
	- All your files must be executable

- C Scripts
	- Allowed editors: vi, vim, emacs
	- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
	- All your files should end with a new line
	- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
	- You are not allowed to use global variables
	- No more than 5 functions per file
	- The prototypes of all your functions should be included in your header file called lists.h
	- Don’t forget to push your header file
	- All your header files should be include guarded

Tasks
- Mandatory
	- 0-positive_or_negative.py: prints whether the number stored in the variable number is positive or negative. 
	- 1-last_digit.py: prints the last digit of the number stored in the variable number.
	- 2-print_alphabet.py: prints the ASCII alphabet, in lowercase, not followed by a new line.
	- 3-print_alphabt.py: prints the ASCII alphabet, in lowercase, except letters q and e, not followed by a new line
	- 4-print_hexa.py: prints all numbers from 0 to 98 in decimal and in hexadecimal.
	- 5-print_comb2.py: prints numbers from 0 to 99.
	- 6-print_comb3.py: prints all possible different combinations of two digits.
	- 7-islower.py: contains function that checks for lowercase character.
	- 8-uppercase.py: contains function that prints a string in uppercase followed by a new line.
	- 9-print_last_digit.py: contains function that prints the last digit of a number.
	- 10-add.py: adds two integers and returns the result.
	- 11-pow.py: contains function that computes a to the power of b and return the value.
	- 12-fizzbuzz.py: prints the numbers from 1 to 100 separated by a space. For multiples of three print Fizz instead of the number and for multiples of five print Buzz. For numbers which are multiples of both three and five print FizzBuzz.
	- 13-insert_number.c: function in C that inserts a number into a sorted singly linked list.

- Advanced
	- 100-print_tebahpla.py: program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.
	- 101-remove_char_at.py: contains function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
	- 102-magic_calculation.py: Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
