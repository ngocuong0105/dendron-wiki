# Contraint based system for 9 * c = 5 * (f - 32)
# Check Chapter 2 in SICP notes

#%%
# Implementation

# Constraints = fictionaries which receive info from connectors by means of two messages:
# • constraint['new_val']() indicates that some connector that is connected to the constraint has a
# new value.
# • constraint['forget']() indicates that some connector that is connected to the constraint has for-
# gotten its value

from operator import add, sub
def adder(a, b, c):
    """
    The constraint that a + b = c.
    To support multidirectional constraint propagation, the adder must also specify that it
    subtracts a from c to get b and likewise subtracts b from c to get a
    """
    return make_ternary_constraint(a, b, c, add, sub, sub)

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


# We will implement connectors that respond to the following messages:

# connector['set_val'](source, value) indicates that the source is requesting the connector
# to set its current value to value.
# • connector['has_val']() returns whether the connector already has a value.
# • connector['val'] is the current value of the connector.
# • connector['forget'](source) tells the connector that the source is requesting it to forget its
# value.
# • connector['connect'](source) tells the connector to participate in a new constraint, the source.


from operator import mul, truediv
def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)

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



# Be the user:
celsius = make_connector('Celsius')
fahrenheit = make_connector('Fahrenheit')
def make_converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [make_connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)

make_converter(celsius, fahrenheit)

# Primitives in our language:
# - adder, multiplier, constant constraints

# Use message passing to coordinate constraints and connectors.

# To answer messages we use dictionary.

# A dispatch dictionary will have string-valued keys that denote the messages it accepts.
# The values associated with those keys will be the responses to those messages. 

# Constraints are dictionaries that do not hold local states themselves.
# Their responses to messages are non-pure functions that change the connectors that they constrain.

# Connectors are dictionaries that hold a current value and respond to messages that manipulate that value.

# Constraints will not change the value of connectors directly, but instead will do so by sending messages, so that
# the connector can notify other constraints in response to the change. In this way, a connector represents a number,
# but also encapsulates connector behavior.

# What we want:

# Send message to a connector:
celsius['set_val']('user', 25) # this is a function
# Celsius = 25
# Fahrenheit = 77


# %%
