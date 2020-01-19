def large_sum():
    sum_num = 0
    with open('large-number.txt', 'r') as file:
      for line in file:
         sum_num += int(line)
        
    return str(sum_num)[:10]

