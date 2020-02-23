import math
def sum_amicable_num(num):
    amicable_numbers = set()
    for a in range(1, num):
        b = sum_all_factors(a)
        if sum_all_factors(b) == a and a != b:
               amicable_numbers.update([a,b])
    return sum(amicable_numbers)        

def sum_all_factors(num):
    all_factors = []
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            all_factors.append(i)
            if num // i not in all_factors:
                all_factors.append(num//i)
    return 1 + sum(all_factors)