from typing import Callable, Dict
from stack import Stack


def postfix(expression: str, precedence: Dict[str, int]):
    """Return the postfix verson of infix expression."""
    ops = Stack()  # Stack of operators
    result = ''
    for symbol in expression:
        if symbol.isalnum():
            # The symbol is an operand (either variable or constant). Just put it into result.
            result += symbol
        elif symbol == '(':
            # This is open parenthesis. This defined higher precedence. Put it into stack.
            ops.push(symbol)
        elif symbol == ')':
            # This is close parenthesis. Again this defined higher precedence.
            # Pop all operator of its most closest open parenthesis and put them into result.
            while ops.top() != '(':
                result += ops.pop()
            # Don't forget to pop the open parenthesis itself out of the stack.
            ops.pop()
        else:
            # Pop all operator which have higher precedence than current operator or until stack is empty and put them into stack.
            while not ops.empty() and ops.top() != '(' and precedence[ops.top()] >= precedence[symbol]:
                result += ops.pop()
            # Don't forget to push the current operator into the stack.
            ops.push(symbol)
    while not ops.empty():  # Pop all operators that are still there in stack.
        result += ops.pop()
    return result


def eval_postfix(expression: str, opers: Dict[str, Callable[[int, int], int]]) -> int:
    """
    Evaluate the postfix expression and return the result.

    Arguments:
    expression : A postfix expression whose symbol are seperated by a space.
    opers      : A dictionary of callable object mapped to each operator.

    e.g.
    >>> import operator
    >>> expression = "100 200 + 2 / 5 * 7 +"
    >>> operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,
        '^': operator.pow
    }
    >>> eval_postfix(expression, operators)
    757
    """
    s = Stack()  # Stack of operands
    for symbol in expression.split():
        if symbol.isnumeric():
            # The symbol is operand (either variable or constant). Push it into the stack.
            s.push(int(symbol))
        elif symbol in opers:
            # The symbol is operator.
            y = s.pop()  # Get second operand.
            x = s.pop()  # Get first operand.
            # Perform the operation base on operator.
            result = opers[symbol](x, y)
            s.push(result)  # Store the result back to the stack.
    return s.pop()  # The only remaining stack item would be expression result.
