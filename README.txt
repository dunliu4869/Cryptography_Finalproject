Major import library contain:
random
math
unittest
------------------------------------------
Files contain:
bbs.py:
bbs(s) Blum-Blum-Shub Pseudorandom Number Generator

bsgs.py:
bsgs(g, y, p) Baby-step-giant-step

euler_phi.py:
euler_phi(a) Euler's totient function

exgcd.py:
exgcd(a, b) extended euclidean algorithm

fastexp.py:
fastexp(b, p, d) fast exponentiation algorithm

gcd.py:
gcd(a, b) greatest common divisor

isprime.py:
is_prime(n, k=128) check if a number is prime

modinverse.py:
modInverse() Modular Multiplicative Inverse

naor_reingold.py:
naor_reingold(n,p,q,x,r) output the result of random decimal number

order.py:
order(a, n, b) find the order

pminus1.py:
pminus1(n) Pollard p-1 Factorization Algorithm

pollardRho.py:
pollardRho() Pollard’s Rho Factorization Algorithm

primeGen.py:
generate_prime_number(length=50)  generate a 50 bits long prime

primitiveroot.py:
primitive_root(p) search the smallest primitive root of p

PrmRtSrch.py
generate all of the primitive roots

Elgamal.py
steps of Elgamal

RSA.py
steps of RSA

testelgamal.py
unittest of Elgamal

testrsa.py
unittest of RSA
-----------------------------------------------------
The funtion mainly used for RSA:
pollardRho() Pollard’s Rho Factorization Algorithm: will return one factor of input n

bbs() Blum-Blum-Shub Pseudorandom Number Generator: by given two prime number p,q(can be generater by naor_reingold and tested by miller_rabin method), put into a number "s" that relatively prime to n(p*q), and manually set range of wanted digit binary number, finally convert into decimal number.

is_prime() Miller-Rabin primality test: by given "n" as number and manually set "k" rounds, the result is either True or false

pick_e() random pick e, let 1<e<fn and gcd(e,x) = 1

pick_d() by given e and fn to do the Modular Multiplicative Inverse

RSA encryption and decryption has been provided in the rsa_process() with comment line to explain details



The function mainly used for Elgamal:
order(): to prove an integer b is the order of a mod n

primitiveroot(): based on the result of phi(n) and order() to judge whether a is the primitive root of n or not

bsgs(): by given g(primitive root), y(β value stand for alice public key computed by pow_mod(g,d,p)), p(prime number), this function will be used to intercept the communication between alice and bob. Eve can use bsgs method calculate the secret key d by sloving the discrete logarithm problem in Elgamal

Elglmal encryption and decryption has been provided in the elgamal() with comment line to explain details




The naor_reingold.py file mainly output the result of random decimal number
the unique funcition in naor_reingold.py file is random_bitnumber(), when input specific "n", it will output two n bit long primes p and q and 2n bits long prime r. After generator p,q,r, we can manually select n and x into the naor_reingold() to output random 0 or 1. The naro_reingold_generator() can manually set the run tims of the naor_reingold() so that we can get sequence of 0 and 1, finally combain these 0 and 1 and convert it from binary to decimal number.

naor_reingold() algorithm followed lecture 10 slides, and with comment line to explain details
