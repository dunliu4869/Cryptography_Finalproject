
import random

from gcd import gcd
from fastexp import fastexp
from euler_phi import euler_phi
from modinverse import modInverse



def pick_e(fn):
    # random pick e, let 1<e<fn and gcd(e,x) = 1
    while True:
        e = random.randint(0,fn)
        if gcd(e,fn) == 1:
            return e

def pick_d(e,fn):
    d = modInverse(e,fn)
    return d

def encryption(M,e,n):
    # M is plaintext of the message
    return fastexp(M,e,n)

def decryption(C,d,n):
    # C is the ciphertext of the message
    return fastexp(C,d,n)

def rsa_process():
    # M is plaintext, C is ciphertext
    # public key(n,e), private key(n,d)
    M = 79
    print("your plaintext is:", M)

    p = 173
    q = 271

    while p != q:
        n = p*q
        fn = euler_phi(n)
        e = pick_e(fn)
        d = pick_d(e, fn)
        print("the n is:",n, " and φ(n) is:",fn)
        # n is 46883 fn is 46440
        print("the e is:",e, " and d is:",d)

        c = encryption(M, e, n)
        print("encrypt message is:",c)
        print("decrypt message is:",decryption(c,d,n))
        break

rsa_process()


# How to break RSA with known n and e:
# (1) ed≡1 (mod φ(n)). Only knowing e and φ(n) can d be calculated
# (2) φ(n)=(p-1)(q-1). Only knowing p and q can we calculate φ(n)
# (3) n=pq. Only by decomposing n into factors can p and q be calculated
# We will use the factorization of large integers in this project to break RSA




