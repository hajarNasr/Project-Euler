def distinct_powers(n):
    a = list(range(2, n+1))
    return len({i**j for i in a for j in a})        
