def modInverse(x,m):
    for i in range(1, m):
        if ((x % m) * (i % m)) % m == 1:
            return i
    return -1

