# this is not the efficient solution for large numbers
def prime_summation(num):
    list_of_primes = []  
    for i in range(2, num):
        if is_prime(i):
           list_of_primes.append(i)
    return sum(list_of_primes) 

def is_prime(num):
      prime = True
      for i in range(2, int(num/2)+1):
            if num % i == 0:
                  prime = False
      return prime            

'''
Sieve of Eratosthenes Algorithm    => the efficient algorithm to find prime numbers below n
def sieve(n):
    primes = 2*[False] + [True] * (n -1)
    for i in range(2, int(n**0.5+1.5)):
        for j in range(i*i, n+1, i):
            primes[j] = False
    return [prime for prime, checked in enumerate(primes) if checked] 
'''   
            

