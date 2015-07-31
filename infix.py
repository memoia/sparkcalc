import unittest
import operator
from collections import deque, namedtuple
from types import IntType


OperatorProperty = namedtuple('OperatorProperty', ('weight', 'method'))


class BaseOperators(object):
    """Subclass this to add new operators"""

    operators = {  # symbol to precendence (higher value is higher precedence)
        '*': OperatorProperty(10, operator.mul),
        '/': OperatorProperty(10, operator.div),
        '+': OperatorProperty(5, operator.add),
        '-': OperatorProperty(5, operator.sub),
    }

    def is_operator(self, symbol):
        return symbol in self.operators

    def weight(self, operator):
        if not self.is_operator(operator):
            raise ValueError('{} is not an operator'.format(operator))
        return self.operators[operator].weight

    def method(self, operator):
        if not self.is_operator(operator):
            raise ValueError('{} is not an operator'.format(operator))
        return self.operators[operator].method


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


class BaseTokenizer(object):

    def __init__(self, operator_instance=None):
        self.operators = BaseOperators() if operator_instance is None else operator_instance

    def is_operator(self, symbol):
        return self.operators.is_operator(symbol)

    def is_valid_symbol(self, symbol):
        return symbol.isdigit() or self.is_operator(symbol)

    def tokens(self, infix_string):
        items = infix_string.split()
        if not all(map(self.is_valid_symbol, items)):
            raise ValueError('Invalid character in {}'.format(items))
        return items


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


class RPNBuilder(object):
    """Convert an infix string to reverse polish notation using shunting yard"""
    def __init__(self, infix_string, token_cls=BaseTokenizer, operator_cls=BaseOperators):
        self.in_str = infix_string
        self.operators = operator_cls()
        self.tokenizer = token_cls(self.operators)
        self.opqueue = deque()
        self.symbols = []

    def _next_op_has_precedence(self, symbol):
        if not len(self.opqueue) > 0:
            return False
        next_op = self.opqueue[0]
        return self.operators.weight(next_op) >= self.operators.weight(symbol)

    def _handle_operator(self, symbol):
        while self._next_op_has_precedence(symbol):
            self.symbols.append(self.opqueue.popleft())

    def build(self):
        for symbol in self.tokenizer.tokens(self.in_str):
            if self.operators.is_operator(symbol):
                self._handle_operator(symbol)
                self.opqueue.appendleft(symbol)
            else:
                self.symbols.append(symbol)

        while len(self.opqueue) > 0:
            self.symbols.append(self.opqueue.popleft())

        return self.symbols


class TestRPNBuilder(unittest.TestCase):
    def test_simple_addition(self):
        """Does '1 + 2' result with 1 2 + ?'"""
        result = RPNBuilder('1 + 2').build()
        self.assertEqual(result, ['1', '2', '+'])

    def test_precedence(self):
        """Does '1 + 2 * 3' result with 1 2 3 * + ?"""
        result = RPNBuilder('1 + 2 * 3').build()
        self.assertEqual(result, ['1', '2', '3', '*', '+'])


class RPNEvaluator(object):
    """Evaluate a character list of integers and operators in RP-notation"""
    def __init__(self, rpn_list, operator_cls=BaseOperators):
        self.in_lst = rpn_list
        self.operators = operator_cls()
        self.queue = deque()

    def _next_values(self):
        second_value = self.queue.popleft()
        first_value = self.queue.popleft()
        return (first_value, second_value)

    def evaluate(self):
        for symbol in self.in_lst:
            if self.operators.is_operator(symbol):
                method = self.operators.method(symbol)
                self.queue.appendleft(method(*self._next_values()))
            else:
                self.queue.appendleft(int(symbol))
        return self.queue.pop()


class TestRPNEvaluator(unittest.TestCase):
    def test_simple_addition(self):
        """Does '1 + 2' evaluate to 3 ?"""
        rpn_ops = RPNBuilder('1 + 2').build()
        self.assertEqual(3, RPNEvaluator(rpn_ops).evaluate())

    def test_precedence(self):
        """Does '1 + 2 * 3' evaluate to 7 ?"""
        rpn_ops = RPNBuilder('1 + 2 * 3').build()
        self.assertEqual(7, RPNEvaluator(rpn_ops).evaluate())

    def test_example_provided_in_readme(self):
        instr = '4 + 4 * 8 / 2 + 10'
        rpn_ops = RPNBuilder(instr).build()
        self.assertEqual(30, RPNEvaluator(rpn_ops).evaluate())


def eval_expr(in_str):
    """Main entry point for module use."""
    return RPNEvaluator(RPNBuilder(in_str).build()).evaluate()


if __name__ == '__main__':
    unittest.main(verbosity=2)
