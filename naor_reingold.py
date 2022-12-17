import random
import unittest

from gcd import gcd
from fastexp import fastexp
from isprime import is_prime

# def random_bitnumber(n):
#     p = random.getrandbits(n)
#     q = random.getrandbits(n)
#     r = random.getrandbits(2*n)
#
#     while is_prime(p) is False:
#         p = random.getrandbits(n)
#     while is_prime(q) is False:
#         q = random.getrandbits(n)
#
#     while p == q:
#         q = random.getrandbits(n)
#         while is_prime(q) is False:
#             q = random.getrandbits(n)
#
#     return p,q,r

def random_bitnumber(n):
    p = random.randint(2**(n-1), 2**n - 1)
    q = random.randint(2**(n-1), 2**n - 1)
    r = random.randint(2**(2*n-1), 2**(2*n) - 1)

    while is_prime(p) is False:
        p = random.randint(2**(n-1), 2**n - 1)
    while is_prime(q) is False:
        q = random.randint(2**(n-1), 2**n - 1)

    while p == q:
        q = random.randint(2**(n-1), 2**n - 1)
        while is_prime(q) is False:
            q = random.randint(2**(n-1), 2**n - 1)

    return p,q,r

#print(random_bitnumber(6))

# p,q,r generator by random_bitnumber
def naor_reingold(n,p,q,x,r):
    N = p*q
    numbers = []
    pairs = []

    for i in range(2*n):
        num = random.randint(1,N)
        numbers.append(num)

    # generate a sequence of pairs a where lable as a1,0 a1,1 a2,0 a2,1...a6,1
    for i in range(0, len(numbers), 2):
        pairs.append((numbers[i], numbers[i + 1]))
    #print(pairs)

    g = random.randint(0,N)

    while gcd(g,N) == 1:
        g = g*g % N
        break
    #print(g)

    # convert binary x to decimal and each number stand for a sequence of x
    binary = format(x, "b")
    binary_x = list((map(int, binary)))
    #print(binary_x)


    # compute e as sum of vaule from a1,x1 + a2,x2 ... + an,xn
    pair_match = []
    e = 0
    for i in range(n):
        pair_match.append(pairs[i][binary_x[i]])
        for num in pair_match:
            e += num
    #print(pair_match)
    #print(e)

    # compute g^e mod N 2n bits binary
    nx_digit = fastexp(g,e,N)

    # convert nx into binary and padding extra zero on the left side
    nx_binary = list(bin(nx_digit).replace('0b', '').zfill(2*n))
    nx_list = [int(s) for s in nx_binary]
    #print(nx_digit)
    #print(nx_list)


    # compare nx_binary with random 2n digits binary which is r
    # convert r into 2n digits binary
    # function u * v = (u1v1 + ... + unvn)%2
    r_binary = list(bin(r).replace('0b', ''))
    r_list = [int(s) for s in r_binary]
    #print(r_list)


    bin_match = []
    for x,y in zip(nx_list, r_list):
        bin_match.append((x*y))

    bin_result = sum(bin_match) % 2
    #print(bin_match)
    return bin_result


# get the result of 0 or 1
#print(naor_reingold(6,11,7,43,3815))

def naro_reingold_generator():
    #pick random n and x
    n = 6
    x = 43
    new_number = []

    # set run generator n times to get a binary number
    for i in range(50):
        if n == 6:
            p = int(random_bitnumber(6)[0])
            q = int(random_bitnumber(6)[1])
            r = int(random_bitnumber(6)[2])
            new_number.append(naor_reingold(6, p, q, 43, r))

    new_numebr = int(''.join(map(str,new_number)),2)
    print(new_numebr)

naro_reingold_generator()


class TestRSA(unittest.TestCase):
    def test_random_bitsnumber(self):
        n = 6

        number = random_bitnumber(n)
        # since number return p,q,r
        p = int(number[0])
        q = int(number[1])
        r = int(number[2])

        self.assertEqual(len(bin(p)[2:]), n)
        self.assertEqual(len(bin(r)[2:]), 2*n)

if __name__ == '__main__':
    unittest.main()


