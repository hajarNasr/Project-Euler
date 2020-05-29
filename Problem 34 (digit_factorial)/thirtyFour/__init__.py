def add_fact_digits(num):
    facts_1_9 = {"0":1, "1":1, "2":2, "3":6, "4":24, "5":120, "6":720, "7":5040, "8":40320, "9":362880,} 
    return sum([facts_1_9[i] for i in list(num)])
    

def digit_factorial():
    res = {"sum":0, "numbers":[]}
    for i in range(11, 100000):
        digits = list(str(i))
        if add_fact_digits(str(i)) == i:
            res["sum"] += i
            res["numbers"] += [i]
    return res        

