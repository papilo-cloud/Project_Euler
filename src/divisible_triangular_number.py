
# Helper function
def divisors_count(number):
    count = 0
    for i in range(1, number+1):
        if number%i == 0:
            count += 1
    return count
            
# Triangular number functions
def divisible_triangular_number(num):
    found_num = False
    index = 1
    
    while not found_num:
        sequence = (index * (index + 1)) / 2
        if divisors_count(int(sequence)) >= num:
            found_num = True
            return sequence
        index += 1
        
num_of_divisors = 500
print(divisible_triangular_number(num_of_divisors))