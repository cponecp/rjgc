import re
import sys


class Calculator(object):
    def __init__(self, args1):
        if (args1[0] == "'" and args1[len(args1) - 1] == "'") or (args1[0] == '"' and args1[len(args1) - 1] == '"'):
            args1 = args1.strip("'")
            args1 = args1.strip('"')
        self.expression = re.findall('\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)', args1)
        self.other_char = re.findall('[^(\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)|\s)]', args1)

    def input_right(self):
        if len(self.other_char) != 0:
            print('INPUT ERROR')
            return 0
        return 1

    def format_right(self):
        left_brackets = []
        right_brackets =[]
        for i in range(len(self.expression)):
            if self.expression[i] == '(':
                left_brackets.append(i)
            elif self.expression[i] == ')':
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
            return 0
        return 1

    def calculate(self):
        for i in range(len(self.expression) - 1):
            if self.expression[i] == '/' and self.expression[i + 1] == '0':
                return 'VALUE ERROR'
        if len(self.expression) == 1:
            result = self.expression[0]
            return result
        else:
            result1 = eval(''.join(self.expression))
            self.expression.clear()
            self.expression.append(str(result1))
            return self.calculate()

    def print_answer(self, answer1):
        if answer1 == 'VALUE ERROR':
            print('VALUE ERROR')
        else:
            print('计算结果为 %.10g' % float(answer1))


if __name__ == '__main__':
    args = ' '.join(sys.argv[1:])
    c = Calculator(args)
    if c.input_right():
        if c.format_right():
            answer = c.calculate()
            c.print_answer(answer)
