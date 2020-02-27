#!/usr/bin/python3
#import re
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    document = args[0]
    query = args[1]
    with open(query) as query_file:
        for word in query_file:
            print(word)