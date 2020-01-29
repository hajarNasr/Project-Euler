len_numbers = {"1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, "8":5, "9":4, "10":3, "11":6, "12":6,
                  "13":8, "14":8, "15":7, "16":7, "17":9, "18":8, "19":8, "20":6, "30":6, "40":5, "50":5,
                   "60":5, "70":7, "80":6, "90":6, "100":10, "200":10, "300":12,"400":11, "500":11,
                    "600":10, "700":12, "800":12,"900":12, "1000":11,} 
def number_letter_counts(number):
    count = 0
    for i in range(1,number+1):
        num = str(i) 
        if int(num) > 100 and int(num) not in[200, 300, 400, 500, 600, 700, 800, 900, 1000]:  # count 3 for 'and'
            count += 3
        if num in len_numbers:                      # this is for small numbers from the numbers in the dictionar
           count += len_numbers[num]  
        else:
           if num[-2:] in len_numbers:
              count += len_numbers[num[-2:]]        # if num between *10 t0 *20 (like, 115,219, 314) count numbers individually 
              num = num[0:-2] +"00"                 # from 10 to 20 ( here,15, 19, 14) and then let num = *00 (100, 200, 300)
           count += count_letters(list(num)[::-1])  # reverse num and sent it to count letters function if num = 340 then
    return count                                    # will be sent to the function as list:0-4-3 if it's 519 it will be sent as list:0-0-5
                                                    # because in the previous step we extract the count of 19 and let num = 500
def count_letters(digits):
    count = 0
    for key, val in enumerate(digits):  
        digits[key] = val + "0"*key         # the digits are sent in reverse so the list: 0-4-3 will end up being list: 0-40-300 (for num:340)
    for digit in digits:                    # list:0-0-5 will be 0-0-500 (for num:500), list: 3-3-5 will end up list: 3-30-500(num:533)
        if digit in len_numbers:
            count += len_numbers[digit]     # now all numbers in digits should be in the dictionary
    return count
 

print(number_letter_counts(5))