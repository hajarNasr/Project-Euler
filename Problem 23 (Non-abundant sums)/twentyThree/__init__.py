import math
def sum_of_non_abundant_numbers(num):
    all_abundants = set()
    sum_all = 0
    for i in range(1, num+1):
        if sum_all_divisors(i) > i:
            all_abundants.add(i)
        if not any((i-j in all_abundants) for j in all_abundants):
            sum_all += i
    return sum_all                      

def sum_all_divisors(num):
    all_divisors = []
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            all_divisors.append(i)
            if num // i not in all_divisors:
                all_divisors.append(num//i)
    return 1 + sum(all_divisors)