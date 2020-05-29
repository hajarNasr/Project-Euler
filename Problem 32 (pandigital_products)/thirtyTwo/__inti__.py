def pandigital_products():
  pd = set()
  for i in range(1,  100):
    for j in range(100, 9999):
        digits = str(i) + str(j) + str(i*j)
        if ("".join(sorted(digits)) == "123456789"): 
            pd.add(i*j)

  return sum(pd) 