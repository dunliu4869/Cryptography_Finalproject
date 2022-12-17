import math

def euler_phi(a):
    ans = a
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            ans = ans // i * (i - 1)
            while a % i == 0:
                a = a / i
    if a > 1:
        ans = ans // a * (a - 1)
    return int(ans)


#print(euler_phi(100))