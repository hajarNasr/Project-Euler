def pentagon_numbers():
    i = 1
    while True:
        x = i*(3*i-1)/2
        for j in range(1, i):
            y = j*(3*j-1)/2
            if is_penta(x-y) and is_penta(x+y):
                return x-y
        i += 1        
#stolen equation
def is_penta(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

print(pentagon_numbers())    