---
id: 7khpigcji0ufpuptuqozcft
title: Python
desc: ''
updated: 1750948041514
created: 1750781063837
---

- [Python Language Reference](https://docs.python.org/3/reference/datamodel.html)
- [Fluent Python Book](https://elmoukrie.com/wp-content/uploads/2022/05/luciano-ramalho-fluent-python_-clear-concise-and-effective-programming-oreilly-media-2022.pdf)


# Memory Management
```python
del df # does not release memory to the OS
```


# Private methods
Private methods are those methods which can't be accessed in other class except the class in which they are declared.

- One underscore is to show it is a internal function: `_function_name()`
- Two underscores: the idea is to use double __ to fully disclose methods as private so python will convert them form __private_method to _Myclass__my_private_method and will not let a child class overwrite this method. 

# del and Garbage Collection

"Objects are never explicitly destroyed; however when they become unreachable hey may be garbage-collected."

```python
1 == (1) # returns true
x and (x) usually mean the same thing
del x # this is a statement not a function
del(x) # would do the same thing


(1,) # tuple
```

- `del` deletes the reference, not the object
```python
l1 = [1,2] # l1 reference to the object [1,2]
l2 = l1 # l2 reference to the object
del l1 # deletes reference l1
print(l2) # [1,2]
```

```python
# example of a life of an object
import weakref
def bye():
    print('... goodbye my lover')
ender = weakref.finalize(s1, bye)
ender.alive # True
del s1
ender.alive # True
s2 = '' # ... goodbye my lover
ender.alive # False
```

Objects may be deleted by the garbage collector once they become unreachable! In CPython When the reference count of an object reaches zero, the garbage collector disposes of it. 

# == vs `is`

- `==` compares values, `is` compares if it referencing to the same object

```python
l1 = [1,2]
l2 = l1[::] # make copy
l2 == l1 # true
l1 is l2 # false

l3 = [1,2]

l3 == l2 # true
```


**Garbage Collector**

reference-counting - when it becomes zero it is unreachable and collected.

CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable,
but is not guaranteed to collect garbage containing circular references.


- simple assignment does not create copies - references to the same object
- function parameters are passed as aliases, which means the function may change any mutable object received as an argument. Need to make local copy to prevent this.
- Using mutable objects as default values for function parameters is dangerous because if parameters are changed in-place, the default value is changed!

# Python Data Model

- [Data Model from Python Language Reference](https://docs.python.org/3/reference/datamodel.html)


Every object has identity (address of the place in memory), type and value. Only value can be changed (for mutable objects). Immutable objects cannot have their value changed.

`is` operator compares the identity of two objects `==` compares their value.

`id()` gives an integer representing the identity
