import sympy      
def nth_prime(n):
    prime_num = 0 
    for i in range(n):
        prime_num = sympy.nextprime(prime_num)  
    return prime_num
