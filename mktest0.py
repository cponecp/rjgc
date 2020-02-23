import re
import sys


def calculate(expression):
    expression0 = expression
    for i in range(len(expression0)-1):
        if expression0[i] == '/' and expression0[i+1] == 0:
            return 'error0'
    if len(expression0) == 1:
        result = expression0[0]
        return result
    else:
        result1 = eval(''.join(expression0))
        expression0.clear()
        expression0.append(str(result1))
        return calculate(expression0)


if __name__ == '__main__':
    args = ' '.join(sys.argv[1:])
    if (args[0] == "'" and args[len(args)-1] == "'") or (args[0] == '"' and args[len(args)-1] == '"'):
        args = args.strip("'")
        args = args.strip('"')
    expression = re.findall('\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)', args)
    other_char = re.findall('[^(\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)|\s)]', args)
    if len(other_char) != 0:
        print('INPUT ERROR')
    else:
        left_brackets = []
        right_brackets =[]
        for i in range(len(expression)):
            if expression[i] == '(':
                left_brackets.append(i)
            elif expression[i] == ')':
                right_brackets.append(i)
        format0 = 1
        if len(left_brackets) != len(right_brackets):
            format0 = 0
        else:
            for i in range(len(left_brackets)):
                if left_brackets[i] > right_brackets[i]:
                    format0 = 0
        if format0 == 0:
            print('FORMAT ERROR')
        else:
            answer = calculate(expression)
            if answer != 'error0':
                print('计算结果为 %.10g' % float(answer))
            else:
                print('VALUE ERROR')