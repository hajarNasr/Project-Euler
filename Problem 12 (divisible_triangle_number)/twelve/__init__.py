from sympy.ntheory import factorint
def divisible_triangle_number(divisors):
    n = 1
    while True:
        triangle = (n * (n+1))//2                 # calculate the next triangle number
        prime_factors_tri = factorint(triangle)   # find prime factors of the triangle number
        total_divs = 1              
        for i in prime_factors_tri:                    # let's say 6 = 2 * 3 = 2^1 + 3^1 so the number of divisors of 6 is (1+1)*(1+1) 
            total_divs *= prime_factors_tri[i]+1       # add one to the prime factors exponents and then multiply them
        if total_divs > divisors:                      # compare the total_divs of the current tirangle and see it's greater than the given divisors
            return triangle                             
        n += 1
     


