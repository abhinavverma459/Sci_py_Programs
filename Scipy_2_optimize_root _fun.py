from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot=root(eqn,0)  # optimize function has root fun() so use it
print(myroot)

