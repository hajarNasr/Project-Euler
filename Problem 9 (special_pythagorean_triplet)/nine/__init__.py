import math                                  
def special_pythagorean_triplet(num):                   # a^2 + b^2 = c^2  
   for a in range(1, num):                              # c = sqrt(a^2 + b^2)
      for b in range(a+1, num):                         # a + b + c = num
         c = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) # a + b + sqrt(a^2 + b^2) = num    
         if a + b + c == num:                                 
               return int(a*b*c)
            

