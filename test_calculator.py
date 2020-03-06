from unittest import TestCase, mock
from mktest0 import Calculator


class TestCalculator(TestCase):
    def test_input_right(self):
        self.c1 = Calculator('1+1a')
        self.assertEqual(0, self.c1.input_right(), "输入是正确的")
        with mock.patch('builtins.print') as mock1:
            self.c1.input_right()
            mock1.assert_has_calls([
                mock.call('INPUT ERROR')
            ])
        self.c2 = Calculator('1+1')
        self.assertEqual(1, self.c2.input_right(), "输入是错误的")

    def test_format_right(self):
        self.c3 = Calculator('(1+')
        self.assertEqual(0, self.c3.format_right(), "格式是正确的")
        with mock.patch('builtins.print') as mock3:
            self.c3.format_right()
            mock3.assert_has_calls([
                mock.call('FORMAT ERROR')
            ])
        self.c4 = Calculator('(1+1)')
        self.assertEqual(1, self.c4.format_right(), "格式是错误的")

    def test_calculate(self):
        self.c5 = Calculator('1/0')
        self.assertEqual('VALUE ERROR', self.c5.calculate(), "所给的值是正确的")
        self.c6 = Calculator('1+1')
        self.assertEqual('2', self.c6.calculate())

    def test_print_answer(self):
        self.c7 = Calculator('1/0')
        answer = 'VALUE ERROR'
        with mock.patch('builtins.print') as mock7:
            self.c7.print_answer(answer)
            mock7.assert_has_calls([
                mock.call('VALUE ERROR')
            ])
        self.c8 = Calculator('1+1')
        answer = '2'
        with mock.patch('builtins.print') as mock8:
            self.c8.print_answer(answer)
            mock8.assert_has_calls([
                mock.call('计算结果为 2')
            ])
