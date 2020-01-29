import math
def power_digit_sum(exp):
    number = int(math.pow(2, exp))
    sum_num = sum(list(map(int, list(str(number)))))   # convert number into a string then a list of int digits them sum all digits
    return sum_num
 