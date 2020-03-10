'''类Calculator的测试代码'''
from unittest import TestCase, mock
from mktest0 import Calculator


class TestCalculator(TestCase):
    '''类Calculator的测试函数'''
    def setUp(self):
        self.c_1 = Calculator('1+1a')
        self.c_2 = Calculator('1+1')
        self.c_3 = Calculator('(1+')
        self.c_4 = Calculator('(1+1)')
        self.c_5 = Calculator('1/0')
        self.c_6 = Calculator('1+1')
        self.c_7 = Calculator('1/0')
        self.c_8 = Calculator('1+1')

    def test_input_right(self):
        '''input_right的测试函数'''
        self.assertEqual(0, self.c_1.input_right(), "输入是正确的")
        with mock.patch('builtins.print') as mock1:
            self.c_1.input_right()
            mock1.assert_has_calls([
                mock.call('INPUT ERROR')
            ])
        self.assertEqual(1, self.c_2.input_right(), "输入是错误的")

    def test_format_right(self):
        '''format_right的测试函数'''
        self.assertEqual(0, self.c_3.format_right(), "格式是正确的")
        with mock.patch('builtins.print') as mock3:
            self.c_3.format_right()
            mock3.assert_has_calls([
                mock.call('FORMAT ERROR')
            ])
        self.assertEqual(1, self.c_4.format_right(), "格式是错误的")

    def test_calculate(self):
        '''calculate的测试函数'''
        self.assertEqual('VALUE ERROR', self.c_5.calculate(), "所给的值是正确的")
        self.assertEqual('2', self.c_6.calculate())

    def test_print_answer(self):
        '''print_answer的测试函数'''
        answer = 'VALUE ERROR'
        with mock.patch('builtins.print') as mock7:
            self.c_7.print_answer(answer)
            mock7.assert_has_calls([
                mock.call('VALUE ERROR')
            ])
        answer = '2'
        with mock.patch('builtins.print') as mock8:
            self.c_8.print_answer(answer)
            mock8.assert_has_calls([
                mock.call('计算结果为 2')
            ])
