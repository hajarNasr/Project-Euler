# Not really my solution
# a^2 + b^2 = c^2
# a + b + c = p
# c = p - a -b
# a^2 + b^2 = (p-a-b)^2 = p^2 + a^2 + b^2 -2pa – 2pb + 2ab   
def int_right_triangles(n):
   res, max_sol = 0, 0
   for p in range(2, n+1, 2):
       count = 0 
       for a in range(2, int(p/3)):
           # b = (p^2 -2pa) / (2p-2a), b has to be an integer  
           if (p*p- 2*p*a)%(2*p- 2*a) == 0:  
              # increase count if b is integer          
              count += 1
           if count > max_sol: 
              max_sol = count
              res = p
   return res  