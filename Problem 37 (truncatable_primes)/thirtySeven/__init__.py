def prime_seive():
    n = 1000000
    arr = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n**0.5 + 1.5)):
        for j in range(i*i, n+1, i):
            arr[j] = False

    return {p:p for p in range(len(arr)) if arr[p]}

def truncatable_primes(n):
    primes = prime_seive()
    res = []
    for p in primes:
        if p in [2, 3, 5, 7]: continue 
        str_p = str(p)
        len_p = len(str_p)
        from_left  = [int("".join(str_p[i:]))    for i in range(1, len_p)]
        from_right = [int("".join(str_p[-len_p:-i])) for i in range(1, len_p)]
        if all([p in primes for p in from_left]) and all([p in primes for p in from_right]):
            res.append(p)

    return sum(res[:n])       
     
 

