0x06. Python - Classes and Objects

Learning Objectives
- General
	- Why Python programming is awesome
	- What is OOP
	- “first-class everything”
	- What is a class
	- What is an object and an instance
	- What is the difference between a class and an object or instance
	- What is an attribute
	- What are and how to use public, protected and private attributes
	- What is self
	- What is a method
	- What is the special __init__ method and how to use it
	- What is Data Abstraction, Data Encapsulation, and Information Hiding
	- What is a property
	- What is the difference between an attribute and a property in Python
	- What is the Pythonic way to write getters and setters in Python
	- How to dynamically create arbitrary new attributes for existing instances of a class
	- How to bind attributes to object and classes
	- What is the __dict__ of a class and/or instance of a class and what does it contain
	- How does Python find the attributes of an object or class
	- How to use the getattr function

Requirements
- General
	- Allowed editors: vi, vim, emacs
	- Ubuntu 20.4 LTS using python3(version 3.8.5)
	- The first line of all your files should be exactly #!/usr/bin/python3
	- Your code should use the pycodestyle (version 2.8.*)
	- All modules, classes and functions(inside and outside) must have documentation

Tasks
- Mandatory
	- 0-square.py: contains an empty class Square that defines a square
	- 1-square.py: contains a class Square that defines a square by:
		- Private instance attribute: size
		- Instantiation with size (no type/value verification)
	- 2-square.py: contains a class Square that defines a square by:
		- Private instance attribute: size
		- Instantiation with optional size
	- 3-square.py: contains a class Square that defines a square by:
                - Private instance attribute: size
                - Instantiation with optional size
		- Public instance method: def area(self): that returns the current square area
	- 4-square.py: contains a class Square that defines a square by:
                - Private instance attribute: size
			- property def size(self): to retrieve it
			- property setter def size(self, value): to set it
                - Instantiation with optional size
                - Public instance method: def area(self): that returns the current square area
	- 5-square.py: contains a class Square that defines a square by:
                - Private instance attribute: size
                        - property def size(self): to retrieve it
                        - property setter def size(self, value): to set it
                - Instantiation with optional size
                - Public instance method: def area(self): that returns the current square area
		- Public instance method: def my_print(self): that prints in stdout the square
		with the character #:
			- if size is equal to 0, print an empty line
	- 6-square.py: contains a class Square that defines a square by:
                - Private instance attribute: size
                        - property def size(self): to retrieve it
                        - property setter def size(self, value): to set it
		- Private instance attribute: position
			- property def position(self): to retrieve it
			- property setter def position(self, value): to set it:
				- position must be a tuple of 2 positive integers, otherwise raise
				a TypeError exception with the message position must be a tuple of
				2 positive integers
                - Instantiation with optional size and optional position
                - Public instance method: def area(self): that returns the current square area
                - Public instance method: def my_print(self): that prints in stdout the square
                with the character #:
                        - if size is equal to 0, print an empty line
			- position should be use by using space - Don’t fill lines by spaces when
			position[1] > 0
