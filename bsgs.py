import math
def bsgs(g, y, p):
    m = int(math.ceil(math.sqrt(p - 1)))
    S = {pow(g, j, p): j for j in range(m)}
    gs = pow(g, p - 1 - m, p)
    for i in range(m):
        if y in S:
            return i * m + S[y]
        y = y * gs % p
    return None

#print(bsgs(2,3,29))

