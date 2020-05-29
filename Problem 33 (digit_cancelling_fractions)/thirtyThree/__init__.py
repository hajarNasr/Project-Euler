from math import gcd
def digit_cancelling_fractions():
    fractions = []
    for i in range(11, 99):
        for j in range(11, 99): 
           # skip all trival numbers
           if i % 10 == 0 or j % 10 == 0:
                continue

           str_i, str_j = str(i), str(j)  
           if str_i[1] == str_j[0]:
               if int(str_i[0]) / int(str_j[1]) == i / j:
                   fractions.append([i, j])  
    num , den = 1, 1    
    # multipy nums together and dens together              
    for i in fractions:
        num *= i[0]
        den *= i[1]   
    return den // gcd(num, den)    