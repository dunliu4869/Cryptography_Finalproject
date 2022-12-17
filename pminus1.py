# Python code for Pollard p-1
# factorization Method

from gcd import gcd
from isprime import is_prime


# function to generate
# prime factors

n = 1403         # Driver code

def pminus1(n):

    a = 2        # defining base
    i = 2        # defining exponent

    # iterate till a prime factor is obtained
    while (True):
        a = (a ** i) % n       # recomputing a as required
        d = gcd((a - 1), n)    # finding gcd of a-1 and n
        if (d > 1):            # check if factor obtained
            return d           # return the factor
            break
        # else increase exponent by one
        # for next round
        i += 1

#print(pminus1(9991))

num = n      # temporarily storing n
ans = []     # list for storing prime factors

# iterated till all prime factors
# are obtained
while (True):
    d = pminus1(num)       # function call
    ans.append(d)          # add obtained factor to list
    r = int(num / d)       # reduce n

    # check for prime using sympy
    if (is_prime(r)):
        ans.append(r)            # both prime factors obtained
        break

    # reduced n is not prime, so repeat
    else:
        num = r

#print(*ans)
print("Prime factors of", n, "are", *ans)