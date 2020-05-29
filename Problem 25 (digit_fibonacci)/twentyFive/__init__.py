def gen_fib(n):
    a, b, count = 0, 1, 2
    while True:
        a, b = b, a+b
        if len(str(b)) == n: 
           yield count
        count += 1   
          

def digit_fibonacci(n):
    return next(gen_fib(n))
    

print(digit_fibonacci(1000)) 