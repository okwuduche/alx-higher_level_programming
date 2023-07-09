#!/usr/bin/python3

"""takes in a URL, sends a request to the URL
and displays the body of the response."""

from sys import argv
from requests import get

if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    if response.status_code > 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

