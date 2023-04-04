#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter, and \
displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    from sys import argv
    from urllib.request import urlopen
    from urllib.parse import urlencode

    email = urlencode(argv[2])
    with urlopen(argv[1], email) as response:
        content = response.read()
        content.decode('utf-8')
        print(content)
