import unittest
from collections import deque
from types import IntType


class BaseOperators(object):
    """Subclass this to add new operators"""
    operators = {  # symbol to precendence (higher value is higher precedence)
        '*': 10,
        '/': 10,
        '+': 5,
        '-': 5,
    }

    def is_operator(self, symbol):
        return symbol in self.operators

    def weight(self, operator):
        if not self.is_operator(operator):
            raise ValueError('{} is not an operator'.format(operator))
        return self.operators.get(operator)


class BaseTokenizer(object):

    def __init__(self, operator_cls=BaseOperators):
        self.operators = operator_cls()

    def is_operator(self, symbol):
        return self.operators.is_operator(symbol)

    def is_valid_symbol(self, symbol):
        return symbol.isdigit() or self.is_operator(symbol)

    def tokens(self, infix_string):
        items = infix_string.split()
        if not all(map(self.is_valid_symbol, items)):
            raise ValueError('Invalid character in {}'.format(items))
        return items


class RPNBuilder(object):
    """Convert an infix string to reverse polish notation using shunting yard"""
    def __init__(infix_string, token_cls=BaseTokenizer):
        self.in_str = infix_string
        self.tokenizer = token_cls()
        self.operators = deque()
        self.symbols = []

    def build(self):
        tokens = self.tokenizer.tokens(self.in_str)




class TestBaseTokenizer(unittest.TestCase):
    def setUp(self):
        self.instance = BaseTokenizer()

    def test_is_operator_when_operator_supplied(self):
        self.assertTrue(self.instance.is_operator('+'))

    def test_is_operator_when_not_operator(self):
        self.assertFalse(self.instance.is_operator('qqq'))

    def test_is_valid_symbol_when_number(self):
        self.assertTrue(self.instance.is_valid_symbol('123'))

    def test_is_valid_symbol_when_operator(self):
        self.assertTrue(self.instance.is_valid_symbol('*'))

    def test_is_valid_symbol_when_invalid(self):
        self.assertFalse(self.instance.is_valid_symbol('^'))

    def test_tokens_when_valid_string_provided(self):
        """Does '1 +   2 - 3' return ['1', '+', '2', '-', '3'] ?"""
        self.assertEqual(self.instance.tokens('1 +   2 - 3'),
                         ['1', '+', '2', '-', '3'])

    def test_tokens_raises_exception_when_invalid_symbol(self):
        """Is '1 -3' considered an invalid expression ?"""
        with self.assertRaises(ValueError):
            self.instance.tokens('1 -3')


class TestBaseOperators(unittest.TestCase):

    def setUp(self):
        self.instance = BaseOperators()

    def test_weight_for_valid_operator(self):
        """Does getting the weight of '*' return a value?"""
        self.assertTrue(type(self.instance.weight('*')) is IntType)

    def test_weight_for_invalid_operator(self):
        """Does getting the weight of '^' raise an exception?"""
        with self.assertRaises(ValueError):
            self.instance.weight('^')




class TestWhatever(unittest.TestCase):

    def test_whatever(self):
        """Does whatever?"""
        self.assertTrue(True)


class TestOtherThing(unittest.TestCase):
    def test_other(self):
        """yeah yeah?"""
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
