def reciprocal_cycles(n):
    primes = sieve(n)
    for p in primes[::-1]:        
        period = 1
        while pow(10, period) % p != 1:
            period += 1
            if p-1 == period:
                return p

#Sieve of Eratosthenes Algorithm    
def sieve(n):
    primes = 2*[False] + [True] * (n -1)
    for i in range(2, int(n**0.5+ 1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked]    

print(reciprocal_cycles(1000))       