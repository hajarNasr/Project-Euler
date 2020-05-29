def coded_triangle_numbers(num):   
    words = ""  
    with open('words.txt', 'r') as file:
        words = file.readlines()[0].replace("\n","").split(",")

    triangles = get_first_200_triangles()  
    num_of_tri_words = 0
    for word in words[:num]:
        if sum_of_letters(word) in triangles:
           num_of_tri_words += 1

    return num_of_tri_words       

def get_first_200_triangles():
    triangles = {}
    for n in range(1,200):
       triangles[int((1/2) * n * (n+1))] = n
    return triangles 

def sum_of_letters(word):
    ALL_LETTERS = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    for letter in word:
        total+= ALL_LETTERS.index(letter)
    return total

print(coded_triangle_numbers(1786))  
    
    
