# estimate golden ration, purely functional
def square(x):
    return x**2
def successor(x):
    return x+1

def approx_eq(x, y, tolerance=1e-5):
    return abs(x - y) < tolerance

def near(x, f, g):
    return approx_eq(f(x), g(x))

def golden_update(guess):
    return 1/guess + 1

def golden_test(guess):
    return near(guess, square, successor)

def iter_improve(update, test, guess=1):
    while not test(guess):
        guess = update(guess)
    return guess


iter_improve(golden_update, golden_test)