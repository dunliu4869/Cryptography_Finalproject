import random


from fastexp import fastexp
from primitiveroot import primitive_root
from modinverse import modInverse
from bsgs import bsgs


def elgamal(p):
    # alice choose prime p and integer g in Zp
    # encrypt message m
    m = 54321
    print("the plaintext is:", m)

    g = primitive_root(p)
    print("the primitive root of p is:", g)

    # d is alice private key
    d = random.randint(1, p - 1)

    beta = fastexp(g, d, p)

    # alice's public key (p,g,beta)

    # bob random pick k
    k = random.randint(1, p - 1)

    # Encryption m (1 <= m <= p-1) send y1 y2 to alice
    y1 = fastexp(g, k, p)
    y2 = (m * fastexp(beta, k, p)) % p

    # ciphertext y1 y2 are public
    cipher = y1, y2

    print("the Alice's private d is: ", d, " β is: ", beta, " and Bob's random k is:", k)
    print("Bob send the ciphertext:", cipher)

    # Decryption based on m = y1^(-k) * y2 mod p
    d_message = y2 * modInverse(pow(y1, d, p), p) % p

    print("Alice's decrypt message is:", d_message)

    # Eve intercept Alice and Bob's message
    # with knowing alice public key (p,g,y) and bob ciphertext y1 and y2
    # since ciphertext consists random k, we need to use bsgs to compute the discrete log of y

    # x is the alice private key d
    x = bsgs(2, 16, 37)
    # print(x)

    # once alice private d is known, Eve can get beta pow(g,d,p)
    # then just repeat d_message
    new_beta = pow(2, 4, 37)

    if new_beta == beta:
        d_message = y2 * modInverse(pow(y1, d, p), p) % p

    print("Eve's decryption is:", d_message)


elgamal(37)



