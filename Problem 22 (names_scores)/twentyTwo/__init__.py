def names_scores():
    alphabet = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,"H":8, "I":9, "J":10, "K":11,"L":12,
                "M":13, "N":14, "O":15,"P":16, "Q":17, "R":18, "S":19, "T":20,"U":21, "V":22, "W":23,
                "X":24,"Y":25, "Z":26,}

    # open the file of names with double quotes and delete the quotes and
    # save the results in another file
    with open('names_file.txt', 'r') as quoted_names, open('names.txt', 'w') as unquoted_names:
        for line in quoted_names:
            unquoted_names.write(line.replace('"',""))   

    # open the file with unquoted names to read from it all the lines
    with open('names.txt', 'r') as file_of_names: 
        names = file_of_names.readlines() 
    # split the names by , and sort it and save the result in name
    names = sorted(names[0].split(","))

    total_scores, count = 0, 1
    # go through every item in names 
    for name in names:
        name_score = 0
        # find the alphabetical order for each letter in name and added to the name score
        for letter in name:
            name_score += alphabet[letter]
        # multiply name_score by name's alphabetical position in the list and add it to total scores 
        total_scores += name_score * count
        count += 1    

    return total_scores

