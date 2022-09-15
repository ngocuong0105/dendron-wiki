#%%
from string import ascii_letters
from typing import List


def is_equal(exp, var: str) -> bool:
    return exp[0] == var

def is_atom(exp) -> bool:
    return isinstance(exp,str) and (exp in ascii_letters or exp.isnumeric())

def a1(exp):
    return exp[1][0]

def a2(exp):
    return exp[1][1]

def make_sum(a1, a2):
    if a1.isnumeric() and a2.isnumeric():
        return str(int(a1) + int(a2))
    return '+' + '(' + a1 + ' '+ a2 + ')'

def make_prod(m1, m2):
    if m1.isnumeric() and m2.isnumeric():
        return str(int(m1) * int(m2))
    return '*' + '(' + m1 +' '+ m2+ ')'

def is_constant(exp, var: str) -> bool:
    return is_atom(exp) and not is_equal(exp, var)

def is_same_variable(exp, var: str) -> bool:
    return is_atom(exp) and is_equal(exp,var)

def is_sum(exp) -> bool:
    return not is_atom(exp) and exp[0] == '+'

def is_prod(exp) -> bool:
    return not is_atom(exp) and exp[0] == '*'

def deriv(exp, var: str):
    if is_constant(exp, var):
        return '0'
    elif is_same_variable(exp, var):
        return '1'
    elif is_sum(exp):
        return make_sum(deriv(a1(exp), var), deriv(a2(exp), var))
    elif is_prod(exp):
        return make_sum(
            make_prod(deriv(a1(exp), var), a2(exp)),
            make_prod(a1(exp), deriv(a2(exp), var)),
        )

# %%
