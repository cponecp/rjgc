'''从一个txt文档中找出某些单词所在的位置'''
#!/usr/bin/python3
# -*- coding: UTF-8 -*-


import re
import sys


def find_word(words1, document1):
    '''找出单词在文档中的位置。

    以问号、句号、感叹号为句子分隔符，输出第几句/第几个词。'''
    length_words1 =len(words1)
    with open(document1) as document_file:
        all_line = []
        for line in document_file:
            all_line.append(line)
    sentence = 0
    word_amount = [0]*length_words1
    word_position = ['']*length_words1
    word_punctuation = []
    length_all_line = len(all_line)
    for i in range(length_all_line):
        line_list = re.findall(r'\w+|\.|\?|\!', all_line[i])
        word_punctuation += line_list
        while 1:
            has_punctuation = 0
            length_word_punctuation = len(word_punctuation)
            for j in range(length_word_punctuation):
                if word_punctuation[j] in {'.', '!', '?'}:
                    has_punctuation = 1
                    sentence += 1
                    for k in range(0, j):
                        word1 = word_punctuation[k].lower()
                        for x in range(0, length_words1):
                            if word1 == words1[x]:
                                word_amount[x] += 1
                                if word_amount[x] > 1:
                                    word_position[x] += ',{0}/{1}'.format(sentence, k + 1)
                                else:
                                    word_position[x] += '{0}/{1}'.format(sentence, k + 1)
                    for k in range(j, -1, -1):
                        del word_punctuation[k]
                    break
            if has_punctuation == 0:
                break
    for i in range(length_words1):
        if word_amount[i] == 0:
            print('None')
        else:
            print(word_position[i])
    return 0


if __name__ == '__main__':
    ARGS = sys.argv[1:]
    DOCUMENT = ARGS[0]
    QUERY = ARGS[1]
    words = []
    with open(QUERY) as query_file:
        for word in query_file:
            words.append((word.strip("\n")).lower())
    find_word(words, DOCUMENT)
