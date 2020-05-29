def tri_penta_hexa(n):
    i = 286
    while True:
        tri = (i*(i+1))/2
        if is_penta(tri) and is_hexa(tri):
            return tri 
        i += 1  

#stolen equations
def is_penta(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

def is_hexa(n):
    if (1+(8*n+1)**0.5) % 4 == 0:
        return True
    return False    

print(tri_penta_hexa(40756))    