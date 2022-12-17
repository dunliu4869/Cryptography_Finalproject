def bbs(s):
    # s is relatively prime to n
    # two large prime p and q where n = p * q
    # p and q are secretly kept, n is public and reusable
    p = 173
    q = 271
    n = p * q

    x = []
    x.append(s ** 2 % n)
    b = []

    # set 50 digit
    for i in range(1, 50):
        num = x[i - 1] ** 2 % n
        x.append(num)
        b.append(x[i] % 2)

    # convert list b binary number to decimal
    d_num = int(''.join(str(x) for x in b), 2)

    #print(b)
    #print(d_num)
    return d_num

#print(bbs(977))
# get decimal number 182096120426651