#%%
# Problem: Find sum of first n even Fibinacci numbers.
from curses import wrapper
from logging.config import valid_ident
from re import S
from typing import Callable


def fib(n):
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return prev

def iseven(n):
    return n % 2 == 0

def sum_even_fib(n):
    return sum(filter(iseven,map(fib,range(n))))

# %%
# Problem: List the letters in the acronym for a name, which includes the first letter of each capitalized word.
def iscap(word):
    return len(word) >0 and word[0].isupper()

def first(word):
    return word[0]

def get_words(string):
    return string.split(' ')

def acronym(string):
    return tuple(map(first,filter(iscap,get_words(string))))
# %%
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance
    return withdraw
# %%
def make_dict():
    container = []
    def get_item(key):
        for k,v in container:
            if k == key:
                return v
        return -1

    def set_item(key,val):
        for i in range(len(container)):
            if container[i][0] == key:
                container[i][1] = val
                return
        container.append((key,val))

    def dispatch(message,key=None,val=None):
        if message == 'get_item':
            return get_item(key)
        elif message == 'set_item':
            set_item(key,val)
        elif message == 'keys':
            return tuple(key for key,_ in container)
        elif message == 'values':
            return tuple(val for _,val in container)
        elif message == 'items':
            return tuple((key,val) for key,val in container)

    return dispatch

# %%
# 9 * c = 5 * (f - 32)
def make_converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [make_connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


from operator import add, sub
def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)

from operator import mul, truediv
def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def make_connector(name=None):
    """A connector between constraints."""
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {
        'val': None,
        'set_val': set_value,
        'forget': forget_value,
        'has_val': lambda: connector['val'] is not None,
        'connect': lambda source: constraints.append(source)
    }
    return connector

def inform_all_except(source, message, constraints):
    """Inform all constraints of the message, except source."""
    for c in constraints:
        if c != source:
            c[message]()

celsius = make_connector('Celsius')
fahrenheit = make_connector('Fahrenheit')
celsius['set_val']('user', 25)
make_converter(celsius,fahrenheit)
# %%
def fact(n):
    def iter(i,m):
        if i > n: return m
        return iter(i+1,i*m)
    return iter(1,1)
# %%
def make_counter():
    return lambda n: lambda: (n := n+1)

counter = make_counter()
# %%
# Thinkiong about streams
# Input data needs to be enumerated as a a stream!
class TreeNode:
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(n):
    root = TreeNode(0)
    curr = root
    for i in range(n):
        curr.left = TreeNode(2*i+1)
        curr.right = TreeNode(2*i+2)
        curr = curr.left
    return root

# Problem 1 Given a tree return sum of squares of odd leaves

def isodd(n):
    return n % 2 == 1
def square(n):
    return n*n

def enum(root):
    if root:
        if root.left is None and root.right is None:
            yield root.val
        for leaf in  enum(root.left):
            yield leaf
        for leaf in  enum(root.right):
            yield leaf

n = 5
root = create_tree(n)
sum(map(square,filter(isodd,enum(root))))

#%%
# Problem 2 append odd fibonacci numbers until n
from functools import lru_cache
@lru_cache
def fib(n):
    if n <= 1: return n
    return fib(n-1)+fib(n-2)

def enum(n):
    return range(n+1)

def isodd(num):
    return num % 2 ==1


n = 15
# Input data needs to be enumerated as a a stream!
input_stream = enum(n)
tuple(filter(isodd,map(fib,input_stream)))


# %%
class Node:
    def __init__(self,val):
        self.val = val

n1 = Node(10)
def foo(root):
    root.val =200
foo(n1)
# %%
ls = []
def foo(ls):
    print(id(ls))
    ls.append(1)

foo(ls)
print(id(ls))

# %%
def summation(n, term, successor):
    sm,i = 0,0
    while i < n:
        sm += term(i)
        i = successor(i)
    return sm
def cube(x):
    return x**3
def next_element(x):
    return x+1

def identity(x):
    return x
def next_element(x):
    return x+1

summation(10,cube,next_element)
summation(10,identity,next_element)
# %%
def square(x):
    return x**2
def successor(x):
    return x+1

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess

def near(x, f, g):
    return approx_eq(f(x), g(x))

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

def golden_update(guess):
    return 1/guess + 1

def golden_test(guess):
    return near(guess, square, successor)

iter_improve(golden_update, golden_test)
# %%
def main(m):
    def foo():
        l,r = 0, 100
        m = l+r >> 1
        return m
    m = foo()
    return m
print(main(5))
# print(x)
# %%
(define sum
  (lambda (term a next b)
    (cond ((a > b) 0)
            (+ (term a)
               (sum term (next a) next b)))))

(define sum-powers
  (lambda (a b n)
    (sum (lambda (x) (expt x n)) a 1+ b)))

(define product-powers
  (lambda (a b n)
    (product (lambda (x) (expt x n)) a 1+ b)))

#%%
from typing import Callable

def product(start:int, end:int, term: Callable, next: Callable):
    if start > end:
         return 1
    return term(start) * product(next(start), end, term, next)

from typing import Callable
def summation(start:int, end:int, term: Callable, next: Callable):
    if start > end:
         return 0
    return term(start) + summation(next(start), end, term, next)

def sum_powers(start:int, end:int, n:int):
    def power(a):
        return a**n
    def plus_one(a):
        return a+1
    return summation(start,end, power, plus_one)

def prod_powers(start:int, end:int, n:int):
    def power(a):
        return a**n # n is a free variable, a is a bound variable
    def plus_one(a):
        return a+1
    return product(start,end, power, plus_one)

print(sum_powers(1,5,2))
print(prod_powers(1,5,2))

# %%

# Python is dynamically typed -> dynamic binding (no way to have static binding)
# Java is statically ypeb but can add Dynamic binding

from typing import Callable
def summation(start:int, end:int, term: Callable, next: Callable):
    if start > end:
            return 0
    return term(start) + summation(next(start), end, term, next)

def sum_powers(start:int, end:int, n:int):
    def power(a,n):
        return a**n # n is a free variable
    def plus_one(a):
        return a+1
    return summation(start,end, lambda x: power(x,n), plus_one)
# %%

if not (1==0):
    print(2)
else:
    print(1/0)

def unless(predicate, st1, st2):
    if not predicate:
        print(st1)
    else:
        print(st2)
def unless(predicate, st1, st2):
    if not predicate:
        print(st1())
    else:
        print(st2())


unless(1==0,lambda: 2, lambda: 1/0)
# applicative order of evaluation breaks my unless function
# I need to add a delay to the arguments st1, stm2
# %%
def modify(ls,m):
    ls[0] = 1
    m += 1
    ls = [2222,2]
ls = [3,1,3]
m = 0
modify(ls,m)
print(ls)
print(m)
# %%
import numpy as np
x = np.arange(10)
x.shape = (2,5)
x.shape = 10 # this is a scalar
x.shape = (1,10) # this is a matrix
y = x[0] # is a view, it is not a copy of the data
x.shape = (2,5)
# So note that x[0, 2] == x[0][2] though the second case is
# more inefficient as a new temporary array
# is created after the first index that is subsequently indexed by 2.
# %%
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2]) # start:stop:step
print(x[1:7]) # start:stop

x = np.array([[[1,1],[2,2],[3,3]], [[4,4],[5,5],[7,6]]])
x.shape = (3,2,2)
x[:3,:2,:2] # equivalent to x[0:3,0:2,0:2] and x[:3,:2,:2] and x[..., 0:2]
x[..., 0:2] # ellipsis is a placeholder for all the dimensions
# %%
x = np.arange(5)

# %%
def custom_cache(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@custom_cache
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)


# fib(n) == custom_cache(fib)(n)
# %%
def cache(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

print(cache(fib)(50))

# %%
import random

def dict_cache(size):
    def dict_cache_param(func):
        cache = {}
        def wrapper(*args):
            key = str(args)
            if key not in cache:
                cache[key] = func(*args)
                if len(cache) > size:
                    del_key = random.choice(list(cache.keys()))
                    while del_key == key:
                        del_key = random.choice(list(cache.keys()))
                    del cache[del_key]
            return cache[key]
        return wrapper
    return dict_cache_param

@dict_cache(size = 10)
def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)

# %%

type(zip([1,2,3],['a','b','c']))
# %%
ls = list(zip([1,2,3],['a','b','c']))
# %%
# The first property of an Iterator that we'll looked at is that it only needs to know how to get the next item.
# It doesn't need to store the entire data in memory if we don't need the entire data structure

# Another really interesting property of Iterators is that they can represent sequences without even using a data structure!
# range(1,10000) is O(1)

# Our final property is one that we couldn't even do by copying values into an Array—handling an infinite sequence.
#%%
ls = list(zip([1,2,3],[4,5,6]))
# %%
def unzip(arr):
    return list(zip(*arr))
# %%

def cache(size):
    def dict_cache(func):
        cache = {}
        def wrapper(*args):
            if len(cache) == size:
                del cache[random.choice(list(cache.keys()))]
            key = str(args)
            if key not in cache:
                cache[key] = func(*args)
            return cache[key]
        return wrapper
    return dict_cache

@cache(10)
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

def odd_sum(arr):
    return sum(num for num in arr if num%2)
# %%
def custom_range(start,end):
    while start < end:
        yield start
        start += 1

r = custom_range(1,10)
for i in r:
    print(i)
# %%
class Iterator:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def next(self):
        if self.start == self.end: raise StopIteration
        self.start += 1
        return self.start-1

    def has_next(self):
        return self.start != self.end

    def __next__(self):
        if self.start == self.end: raise StopIteration
        self.start += 1
        return self.start-1

    def __iter__(self):
        return self
it = Iterator(1,10)
# %%



/*
DESCRIBE entities;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| EntityId      | int          | NO   |     | NULL    |       |
| SourceId      | int          | NO   |     | NULL    |       |
| Name          | varchar(100) | YES  |     | NULL    |       |
| CEO           | varchar(50)  | YES  |     | NULL    |       |
| Location      | varchar(50)  | YES  |     | NULL    |       |
| Ticker        | varchar(50)  | YES  |     | NULL    |       |
| ValidFromDate |timeetime     | NO   |     | NULL    |       |
| ValidToDate   |timeetime     | NO   |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+

You should be able to see a nicely formatted table below, ensure this whole line of text is all on a single line or this won't be the case

Expand the size of your editor by dragging the middle section of the screen to the right
+----------+----------+--------------------+-----------------+-------------------+----------+---------------------+---------------------+
| EntityId | SourceId | Name               | CEO             | Location          | Ticker   | ValidFromDate       | ValidToDate         |
+----------+----------+--------------------+-----------------+-------------------+----------+---------------------+---------------------+
|     2548 |        1 | Google Inc         | Eric Schmidt    | Mountain View, CA | GOOG US  | 1960-01-01 :00      | 2011-04-03 00:00:00 |
|     2548 |        1 | Google Inc         | Larry Page      | Mountain View, CA | GOOG US  | 2011-04-04 00:00:00 | 2015-10-04 00:00:00 |
|     2548 |        1 | Alphabet Inc       | Larry Page      | Mountain View, CA | GOOGL US | 2015-10-05 00:00:00 | 2019-0:00           |
|     2548 |        1 | Alphabet Inc       | Sundar Pichai   | Mountain View, CA | GOOGL US | 2019-00:00          | 2099-12-31 00:00:00 |
|     2548 |        2 | Google Inc         | NULL            | US                | GOOG US  | 1960-01-01 00:00:00 | 2015-10-04 00:00:00 |
|     2548 |        2 | Alphabet Inc       | NULL            | US                | GOOGL US | 2015-10-05 00:00:00 | 2099-12-31 00:00:00 |
|     2548 |        3 | Google             | NULL            | USA               | GOOGL US | 1960-01-01 00:00:00 | 2015-10-04 00:00:00 |
|     2548 |        3 | Alphabet           | NULL            | USA               | GOOGL US | 2015-10-05 00:00:00 | 2099-12-31 00:00:00 |
|     4664 |        1 | Facebook Inc       | Mark Zuckerburg | Menlo Park, CA    | FB US    | 1960-01-01 00:00:00 | 2021-11-01 00:00:00 |
|     4664 |        1 | Meta Platforms Inc | Mark Zuckerburg | Menlo Park, CA    | FB US    | 2021-11-02 00:00:00 | 2099-12-31 00:00:00 |
|     4664 |        3 | Facebook           | NULL            | USA               | FB US    | 1960-01-01 00:00:00 | 2021-11-01 00:00:00 |
|     4664 |        3 | Meta               | NULL            | USA               | FB US    | 2021-11-02 00:00:00 | 2099-12-31 00:00:00 |
|     5231 |        1 | Apple Computer Inc | Steve Jobs      | Cupertino, CA     | NULL     | 1960-01-01 00:00:00 | 1980-12-11 00:00:00 |
|     5231 |        1 | Apple Computer Inc | Steve Jobs      | Cupertino, CA     | AAPL US  | 1980-12-12 00:00:00 | 2007-01-10 00:00:00 |
|     5231 |        1 | Apple Inc          | Steve Jobs      | Cupertino, CA     | AAPL US  | 2007-01-11 00:00:00 | 2011-08-23 00:00:00 |
|     5231 |        1 | Apple Inc          | Tim Cook        | Cupertino, CA     | AAPL US  | 2011-08-24 00:00:00 | 2099-12-31 00:00:00 |
|     5231 |        2 | Apple Inc          | NULL            | US                | AAPL US  | 1960-01-01 00:00:00 | 2099-12-31 00:00:00 |
|     5231 |        3 | Apple              | NULL            | USA               | AAPL US  | 1960-01-01 00:00:00 | 2011-12-31 00:00:00 |
+----------+----------+--------------------+-----------------+-------------------+----------+---------------------+------------------


Table: date

Date
2019-12-02 12:00:00---+

*/

SELECT EntityId,'Date', CEO
FROM entities e
WHERE SourceId = 1
JOIN
SELECT "DATE"
FROM date d
ON e.ValidFromDate <= d.Date <= e.ValidToD

```
#%%
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("yourapp"),
    autoescape=select_autoescape()
)
# %%


class CreditCard:
    def __init__(self, balance:int, interest_rate:float):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def withdraw(self, amount:int):
        self.balance -= amount
        self.transactions.append((-amount, self.balance))

    def deposit(self, amount:int):
        self.balance += amount
        self.transactions.append((amount, self.balance))

    def add_interest(self):
        self.balance += self.balance * self.interest

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions

productA = CreditCard(100, 0.05)
productB = CreditCard(100, 0.1)

class Bank:
    def __init__(self, name:str, products:List[CreditCard]):
        self.name = name
        self.products = products

    def get_product(self, name:str):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def get_products(self):
        return self.products

    def get_balance(self):
        balance = 0
        for product in self.products:
            balance += product.get_balance()
        return balance

    def get_transactions(self):
        transactions = []
        for product in self.products:
            transactions += product.get_transactions()
        return transactions

    def add_interest(self):
        for product in self.products:
            product.add_interest()