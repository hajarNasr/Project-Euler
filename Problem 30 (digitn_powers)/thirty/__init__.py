def digitn_powers(n):
    highest_num = n * (9 ** n)
    result = 0
    for i in range(2,highest_num+1):
        if is_sum_of_powers(i, n):
            result += i
    return result        

def is_sum_of_powers(num, power):
    sum_digits = 0
    for i in str(num):
        sum_digits += int(i) ** power

    return True if sum_digits == num else False

