from sympy.ntheory.primetest import isprime

def quadratic_primes(arange):
    a, b, max_n = [0, 0, 0]
    for i in prime_sieve(arange + 1):   # b must be prime
        for j in range(-i + 2, 0, 2):   
            n = 1
            while isprime(n*n + j*n + i):  # equation= n^2 +  a*n + b, it has to generate prime numbers
                n += 1
                if n > max_n:
                    a, b, max_n = j, i, n
    return a * b                


#Sieve of Eratosthenes Algorithm  
def prime_sieve(n):
    '''generate all primes from 2 to n'''

    alist  = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** 0.5 + 1.5)):
        for j in range(i*i, n+1, i):
            alist[j] = False
    return [prime for prime, checked in enumerate(alist) if checked]  


