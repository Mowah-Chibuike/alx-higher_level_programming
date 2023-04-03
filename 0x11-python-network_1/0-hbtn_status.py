#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as body:
        print('Body response:')
        content = body.read()
        print('\t- type: {}'.format(type(content)))
        print('\t- content: {}'.format(content))
        print('\t- utf8 content:', end=" ")
        try:
            content.decode('utf-8')
            print('OK')
        except Exception:
            print('NO')
