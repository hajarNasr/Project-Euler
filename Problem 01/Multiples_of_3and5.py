def multiplesOf3and5(number):
    all_multiples_of_3and5 = [i for i in range(number) if not i % 3 or not i % 5]
    return sum(all_multiples_of_3and5)