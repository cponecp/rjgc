#!/usr/bin/python3
import re
import sys


def find_word(word, document):
    with open(document) as document_file:
        all_line = []
        for line in document_file:
            all_line.append(line)
    sentence = 0
    word_amount = 0
    word_punctuation = []
    for i in range(len(all_line)):
        line_list = re.findall('\w+|\.|\?|\!', all_line[i])
        word_punctuation += line_list
        while 1:
            has_punctuation = 0
            for j in range(len(word_punctuation)):
                if word_punctuation[j] in {'.', '!', '?'}:
                    has_punctuation = 1
                    sentence += 1
                    for k in range(0, j):
                        if word_punctuation[k] == word:
                            word_amount += 1
                            print('{0}/{1},'.format(sentence, k+1), end='')
                    for k in range(j, -1, -1):
                        del word_punctuation[k]
                    break
            if has_punctuation == 0:
                break
    if word_amount == 0:
        print('None', end='')
    return 0


if __name__ == '__main__':
    args = sys.argv[1:]
    document = args[0]
    query = args[1]
    with open(query) as query_file:
        for word in query_file:
            word = word.strip("\n")
            find_word(word, document)
            print()