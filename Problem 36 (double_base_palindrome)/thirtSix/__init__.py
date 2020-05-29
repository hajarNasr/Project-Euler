def is_palindromic(n):
    bin_n = bin(n)[2:]
    n = str(n)
    return bin_n == bin_n[::-1] and n == n[::-1]
    
def double_base_palindromes(n):
    sum_p = 0
    for i in range(1, n+1):
        if is_palindromic(i):
            sum_p += i

    return sum_p