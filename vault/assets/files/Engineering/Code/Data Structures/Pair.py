#%%
# Rational numbers depend on tuples. tuples can be created from thin air!
def make_pair(x,y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch

def get_item(pair,m):
    return pair(m)

p = make_pair(1,2)
get_item(p,0) # returns 1
get_item(p,1) # returns 2
p(0) # returns 1
# %%
