# helper function 
def palindrome_checker(strng):
    strng = str(strng)
    left_index = 0
    right_index = len(strng) - 1
    
    while left_index < (len(strng) - 1):
        if strng[left_index] != strng[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True

# largest palindrome product function
def largest_palindrome_product(start_num, end_num):
    max_pal = 0
    for i in range(start_num, end_num):
        for j in range(start_num, end_num):
            if palindrome_checker(i*j):
                if max_pal < (i*j):
                    max_pal = (i*j)
    print(max_pal)
largest_palindrome_product(90, 100)