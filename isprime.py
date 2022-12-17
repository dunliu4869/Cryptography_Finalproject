import random

def is_prime(n, k=128):
    # Handle small numbers
    if n in (2, 3):
        return True
    if n == 1 or n % 2 == 0:
        return False

    # Find r and d such that n - 1 = 2^r * d
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test the number against k witnesses
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True