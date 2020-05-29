import itertools as it
def substring_divisibility():  
    pandigital_numbers = list(map("".join,it.permutations("0123456789"))) 
    result = []
    for index in range(len(pandigital_numbers)):
        num = pandigital_numbers[index]
        if not int(num[1:4])%2 and not int(num[2:5])%3 and not int(num[3:6])%5 and not int(num[4:7])%7 and not int(num[5:8])%11 and not int(num[6:9])%13 and not int(num[7:10])%17:
            result.append(num)      

    return result
    

print(substring_divisibility())  
    