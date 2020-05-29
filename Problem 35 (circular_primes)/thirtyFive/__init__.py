def prime_seive(n):
    arr = [False, False] + [True] * (n-1)
    for i in range(2, int(n**0.5 + 1.5)):
        for j in range(i*i, n+1, i):
            arr[j] = False 
    return {i:i for i in range(len(arr)) if arr[i]}  

def get_rotations(n):
    return [int(n[i:] + n[:i]) for i in range(len(n))]
    

def circular_primes(n):
    primes = prime_seive(n)
    circ_p = 0
    for p in primes:
        rotations = get_rotations(str(p))
        if all(r in primes for r in rotations):
            circ_p += 1

    return circ_p