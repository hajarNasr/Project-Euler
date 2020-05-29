from functools import reduce
def lexicographic_permutations(n):
    from_0_9 = list("0123456789")
    res = ""
    while len(from_0_9) > 1:
         d, n = divmod(n, fact( len(from_0_9)-1))
         res += from_0_9.pop(d)
    return int(res+ from_0_9[0])

def fact(n):
    return reduce(lambda x, y: x* y, range(1, n+1))
   