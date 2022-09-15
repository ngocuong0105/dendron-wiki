# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

# standard compiler question
# this calls for a standard expression parser implementation where you call parse-functions on those with the lowest precendence and recursively invoke parse-functions of things with higher precendence.

from collections import deque

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Standard parser implementation based on this BNF
    Grammar:
       s := expression
       expression := term | term { [+,-] term] }
       term := factor | factor { [*,/] factor] }
       factor :== digit | '(' expression ')'
       digit := [0..9]
    '''
    def expTree(self, s: str) -> 'Node':
        return self.parse_expression(deque(s))

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while tokens and tokens[0] in '+-':
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(op, lhs, rhs)
        return lhs
    
    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while tokens and tokens[0] in '*/':
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(op, lhs, rhs)
        return lhs
    
    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft() # consume (
            node = self.parse_expression(tokens)
            tokens.popleft() # consume )
            return node
        else:
            token = tokens.popleft()
            return Node(token) # token is an operand (number)
