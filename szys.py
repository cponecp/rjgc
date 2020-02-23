import random
import sys
from fractions import Fraction


def question():
    all_operator = ['+', '-', '*', '/']
    max_operator_amount = 5
    min_operator_amount = 2
    max_number = 10
    operator_amount = random.randint(min_operator_amount, max_operator_amount)
    random_operator = []
    for i in range(operator_amount):
        random_operator.append(random.randint(0, len(all_operator)-1))
    random_number = [str(random.randint(1, max_number))]
    for i in range(operator_amount):
        if random_operator[i] == 3:
            random_number.append(str(random.randint(1, max_number)))
        else:
            random_number.append(str(random.randint(0, max_number)))
    expression = random_number[0]
    for i in range(operator_amount):
        expression = expression + all_operator[random_operator[i]] + random_number[i+1]
    result = Fraction(eval(expression)).limit_denominator(100000000)
    print(expression, "=", end=' ')
    return result


def start_answer(question_amount1):
    question_total_amount = question_amount1
    question_number = 1
    answer_true_amount = 0
    while question_number <= question_total_amount:
        print("%u、 " % question_number, end=' ')
        result = question()
        answer = Fraction(input())
        if answer == result:
            print('回答正确')
            answer_true_amount += 1
        else:
            print('回答错误，正确答案为:', result)
        question_number += 1
    correct_rate = answer_true_amount / question_total_amount
    print("您的得分为%.1f，正确率为%.1f%%" % (correct_rate*100, correct_rate*100))


if __name__ == '__main__':
    args = sys.argv[1:]
    question_amount = int(args[0])
    if 1 <= question_amount <= 30:
        print("本次共%u题，满分100分" % question_amount)
        start_answer(question_amount)
    else:
        print("输入参数不符合要求")
    exit1 = input('完成所有题目，按任意键退出程序')


