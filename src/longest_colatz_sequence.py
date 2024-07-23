# collatz sequence helper function
def collatz_sequence(num):
    count = 0
    end_count = False
    
    if num == 0:
        return False
    while not end_count:
        # I dont need to print the ranges, so I'll comment it here
        # print(int(num), end=' ')
        
        if num == 1:
            end_count = True
        if num%2 == 0:
            num /= 2
        else:
            num = (3*num) + 1
        count += 1
    return count


def longest_colatz_sequence(num):
    longest_chain = 0
    starting_num = 0
    index = 0
    
    while index <= num:
        if collatz_sequence(index) > longest_chain:
            longest_chain = collatz_sequence(index)
            starting_num = index
        
        index += 1
    print(starting_num, longest_chain)

longest_colatz_sequence(1000000)