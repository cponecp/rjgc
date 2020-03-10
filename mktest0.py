'''计算器'''
import re
import sys


class Calculator(object):
    '''计算器所用函数'''
    def __init__(self, args1):
        if (args1[0] == "'" and args1[len(args1) - 1] == "'") \
                or (args1[0] == '"' and args1[len(args1) - 1] == '"'):
            args1 = args1.strip("'")
            args1 = args1.strip('"')
        self.expression = re.findall(r'\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)', args1)
        self.other_char = re.findall(r'[^(\d+\.*\d*|\+|\-|\*|\/|\^|\(|\)|\s)]', args1)

    def input_right(self):
        '''判断输入是否正确'''
        if len(self.other_char) != 0:
            print('INPUT ERROR')
            return 0
        return 1

    def format_right(self):
        '''判断括号是否符合要求'''
        left_brackets = []
        right_brackets = []
        for i in range(len(self.expression)):
            if self.expression[i] == '(':
                left_brackets.append(i)
            elif self.expression[i] == ')':
                right_brackets.append(i)
        format0 = 1
        if len(left_brackets) != len(right_brackets):
            format0 = 0
        else:
            len_left_brackets = len(left_brackets)
            for i in range(len_left_brackets):
                if left_brackets[i] > right_brackets[i]:
                    format0 = 0
        if format0 == 0:
            print('FORMAT ERROR')
            return 0
        return 1

    def calculate(self):
        '''判断分母是否为0，不为0时计算并返回计算结果'''
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
        '''打印结果'''
        if answer1 == 'VALUE ERROR':
            print('VALUE ERROR')
        else:
            print('计算结果为 %.10g' % float(answer1))


if __name__ == '__main__':
    ARGS = ' '.join(sys.argv[1:])
    C = Calculator(ARGS)
    if C.input_right():
        if C.format_right():
            ANSWER = C.calculate()
            C.print_answer(ANSWER)
