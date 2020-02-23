from functools import reduce
def sum_factorial_digits(num):
    digits = list(str(factorial(num)))     # compute factorial num and convert it to a string to list it into a list of digits
    return sum([int(i) for i in digits])   # convert items in digits into ints and add them. 

def factorial(num):
    return reduce(lambda x, y: x * y, range(2, num+1))  # return the factorial of a number
