import sympy                
def smallest_multiple(num):
    prime_factors = {}
    for i in range(2, num+1):
        primes = prime_factors_of(i)       # calculate prime factors for numbers from 2 to num
        for j in primes: 
            if j in prime_factors:                    
                if prime_factors[j] < primes.count(j):  # by the end of this loop only the number with the highest exponent will
                   prime_factors[j] = primes.count(j)   # be saved into the dictionary of prime factors
            else:                                       # 2 is 2^1, 4 is 2^2 and 8 is 2^3 so '2: 3' will be in the dictionary 
                prime_factors[j] = primes.count(j)      # for num = 10 the dictionary will look like this {2: 3, 3: 2, 5: 1, 7: 1}

    return multiply(prime_factors)

def multiply(prime_factors):                           # primary_factors = {2: 3, 3: 2, 5: 1, 7: 1} 
    total = 1
    for key in prime_factors:
        total *= key**prime_factors[key]
    return total                                       # total = 2^3 * 3^2 * 5^1 * 7^1 

def prime_factors_of(num):                # a function to calculate prime factors of a number
    value, remainder, mul, prime = 1, 1, 1, 2
    prime_factors = []
    n = num
    while value or remainder:
        value, remainder = divmod(n, prime)
        if remainder == 0:
            prime_factors.append(prime)
            mul *= prime
            if mul == num:
                return prime_factors
            else: 
                n = value  
        else: 
           prime = sympy.nextprime(prime) 
       

    
           

   
    


  