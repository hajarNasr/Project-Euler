def longest_collatz_sequence(limit):
    max_seq, starting_num = 0, 0

    for i in range(2, limit):
        collatz_sequence = count_collatz_sequence(i)
        if collatz_sequence > max_seq:
            max_seq = collatz_sequence
            starting_num = i

    return starting_num

def count_collatz_sequence(num):
    count = 0
    while num != 1:
       if num % 2 == 0:
           num = num // 2
       else:
           num = (3 * num) + 1
       count += 1
    return count 