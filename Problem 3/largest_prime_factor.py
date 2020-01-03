import sympy              # pip install sympy
def largest_prime_factor(num):
    prime, n = 2, num             # first prime number and let n = num
    value, remainder, mul = 1, 1, 1
    while value or remainder:  # the loop should terminate when both value and reminder equal to 0
        value, remainder = divmod(n, prime)  # divide n by prime and assign the result to value and reminder
        if remainder == 0:      
            mul *= prime
            if mul == num:          # check if we reach the value of num
                return prime        # if yes => return the largest prime
            else: 
                n = value           # else reassign n to the new value
        else:  # if remainder does't equal zero, the current prime isn't a factor of num
           prime = sympy.nextprime(prime)  # go find the next prime 

            

   
    


  