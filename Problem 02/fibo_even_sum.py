def fibo_even_sum(n):
    a, b = 1, 2                    
    fibo_numbers = [a, b]
    for _ in range(n-2):
        a, b = b, a+b
        fibo_numbers.append(b)      #appends the next fibo number to fibo_numbers list

    return sum([i for i in fibo_numbers if not i % 2])  #returns the sum of all even numbers in fibo_numbers

