def fastexp(b, p, d):
    product = 1
    for idx in range(p):
        product = product * b % d
        #print(product,pow)
    return product


#print(fastexp(11,3,28))