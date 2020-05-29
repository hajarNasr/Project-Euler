def is_pandigital(contact):
    return "".join(sorted(contact)) == "123456789"

def pandigital_multiples():
    p_digitals, contact = {}, ""
    for num in range(1, 10000):
        contact = str(num)
        for n in range(2, 10):
            contact += str(num * n)
            if len(contact) > 9:
                break
            if len(contact) == 9 and is_pandigital(contact):
                p_digitals[int(contact)] = num
    return max(p_digitals)           

