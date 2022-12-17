from euler_phi import euler_phi
from order import order


def primitive_root(p):
    n = euler_phi(p)
    for a in range(2, p):
        if order(p, n, a) == n:
            return a


#print(primitive_root(7))
