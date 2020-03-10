'''计算器'''
import re
import sys


if __name__ == '__main__':
    ARGS = ' '.join(sys.argv[1:])
    if (ARGS[0] == "'" and ARGS[len(ARGS)-1] == "'") \
            or (ARGS[0] == '"' and ARGS[len(ARGS)-1] == '"'):
        ARGS = ARGS.strip("'")
        ARGS = ARGS.strip('"')
    EXPRESSION = re.findall(r'\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)', ARGS)
    OTHER_CHAR = re.findall(r'[^(\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)|\s)]', ARGS)
    if len(OTHER_CHAR) != 0:
        print('INPUT ERROR')
    else:
        LEFT_BRACKETS = []
        RIGHT_BRACKETS = []
        LEN_EXPRESSION = len(EXPRESSION)
        for i in range(LEN_EXPRESSION):
            if EXPRESSION[i] == '(':
                LEFT_BRACKETS.append(i)
            elif EXPRESSION[i] == ')':
                RIGHT_BRACKETS.append(i)
        FORMAT0 = 1
        if len(LEFT_BRACKETS) != len(RIGHT_BRACKETS):
            FORMAT0 = 0
        else:
            LEN_LEFT_BRACKETS = len(LEFT_BRACKETS)
            for i in range(LEN_LEFT_BRACKETS):
                if LEFT_BRACKETS[i] > RIGHT_BRACKETS[i]:
                    FORMAT0 = 0
        if FORMAT0 == 0:
            print('FORMAT ERROR')
        else:
            try:
                ANSWER = eval(''.join(EXPRESSION))
                print('计算结果为 %.10g' % ANSWER)
            except ZeroDivisionError:
                print('VALUE ERROR')
