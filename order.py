# when a^b mod n is 1, the smallest integer b is the order of a mod n
# according to euler theory phi(n) would be a solution
# when phi(n) is the order of a mod n, a is the primitive root of n

def order(a, n, b):
    p = 1
    while p <= n and b ** p % a != 1:
        p += 1
    if p <= n:
        return p
    else:
        return -1


#print(order(5,7,6))