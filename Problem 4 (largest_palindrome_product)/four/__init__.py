def largest_palindrome_product(num):
    start, end = int("1"*num), int("9"*num) # start for a two-digit number should be 11 and end 99
                                            # start for a three-digit number should be 111 and end 999
    palindromes = []             
    reverse_range = (list(range(start, end+1)))[::-1] #reverse the range of (start, end) to make it begin form highest numbers

    for i in reverse_range:
        for j in reverse_range:
            product = list(str(i * j))
            if product[:len(product)] == product[::-1]:   # check if i * j is a palindrome number
                palindromes.append(i * j)                 # if yes => add it to the palindromes list
                break       
                
    return max(palindromes)
 
