# Project B
# Filter the prime number from a set of random
# numbers


print("getprime.py: __name__ ---> ", __name__)
import random
import prime

rn = []
for i in range(100):
    rn.append(random.randint(1, 100))

primes = []
for n in rn:
    if(prime.checkprime(n) == True):
        primes.append(n)

print(primes)
