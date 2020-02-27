#!/usr/bin/python3
import re
import sys


def find_word(word, document):
    with open(document) as document_file:
        all_line = []
        for line in document_file:
            all_line.append(line)
    sentence = 0
    word_punctuation = []
    for i in range(len(all_line)):
        line_list = re.findall('\w+|\.|\?|\!', all_line[i])
        word_punctuation += line_list
        for j in range(len(word_punctuation)):
            print(word_punctuation[j], end=' ')
    return 0


if __name__ == '__main__':
    args = sys.argv[1:]
    document = args[0]
    query = args[1]
    with open(query) as query_file:
        for word in query_file:
            word = word.strip("\n")
            find_word(word, document)