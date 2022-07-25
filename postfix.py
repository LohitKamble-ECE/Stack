from typing import Dict
from stack import Stack


def postfix(expression: str, precedence: Dict[str, int]):
    """Return the postfix verson of infix expression."""
    ops = Stack()
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
