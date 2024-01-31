from time import time

foundPrime = False
primes = [2, 3]

t1 = time()
for n in range(2, 1000000 + 1):
    for p in primes:
        if n % p == 0:
            foundPrime = False
            break
        else:
            foundPrime = True
    if foundPrime == True:
        primes.append(n)
    foundPrime = False
t2 = time()


print(primes)
print('it took {} seconds to calculate {} numbers and found {} prime numbers.'.format(t2 - t1, n, len(primes)))
