import sympy              # pip install sympy
def largest_prime_factor(num):
    prime = 2             # first prime number
    arr = [1]
    while True:
        if not num % prime:      # check if num is divisibe by the current prime number,
           arr[-1] *= prime      #   if yes => multiply prime to the last item of the list
           if arr[-1] == num:    #   to check if the multiplication of all prime items so far equals num
               return prime      #      if yes => return prime
        prime = sympy.nextprime(prime) # if num is not divisible by the current prime go to the next one
            

   
    


  