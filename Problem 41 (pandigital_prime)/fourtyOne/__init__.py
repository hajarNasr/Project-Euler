import itertools as it
def is_prime(n):
    if n in [0, 1]:
        return False
    if n == 2: 
        return True
    for i in range(2, int(n**0.5 +1)):
        if n % i == 0:
            return False
    return True
         
def is_pandigital(num, from_1_to_n):
    return "".join(sorted(num)) == from_1_to_n

def pandigital_prime(n):
   from_1_to_n =  "".join([str(i) for i in range(1, n+1)])
   numbers = list(map("".join, it.permutations(from_1_to_n)))
   for num in numbers[::-1]:
        if len(num) == n and is_prime(int(num)) and is_pandigital(num, from_1_to_n):
            return num