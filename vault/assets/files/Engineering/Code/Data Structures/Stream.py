#%%
# stream is a recursive data structure showing that data and functions/procedures are the same thing

class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'

    def _compute_rest1():
        empty = Stream.empty()
        return empty

    def __init__(self,first, compute_rest = _compute_rest1):
        assert callable(compute_rest)
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return f'Stream({repr(self.first)}, <...>)'

# %%
# Infinite Streams
def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)

# %%
def map_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

s = integer_stream(3)
squares = map_stream(lambda x: x**2, s)
print(squares.rest.rest)


# %%
# Compute Eristoten table of prime numbers
def filter_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()

def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k-1
    return first_k

def primes(pos_stream):
    def not_divisible(x):
        return x % pos_stream.first != 0
    def compute_rest():
        return primes(filter_stream(not_divisible, pos_stream.rest))
    return Stream(pos_stream.first, compute_rest)

prime_numbers = primes(integer_stream(2))
first_k_as_list(prime_numbers, 10)
# %%
