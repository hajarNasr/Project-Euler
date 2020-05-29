def champer_nownes_constant(n):
    all_nums = "".join(list(map(str,list(range(1,n+1)))))
    dn = [1, 10, 100, 1000, 10000, 100000, 1000000]
    result = 1
    for i in dn:
       try:
          result *= int(all_nums[i-1])
       except:
          break
    return result      

print(champer_nownes_constant(1000000))    
