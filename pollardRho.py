from gcd import gcd

def pollardRho(n):
    x = 2
    y = x ** x + 1
    g = 1

    while g == 1:
        x = (x * x + 1) % n
        y = (pow(y*y + 1,2) + 1) % n
        g = gcd(abs(x - y), n)

    if g == n:
        return None
    else:
        return g


print(pollardRho(646184512626547))