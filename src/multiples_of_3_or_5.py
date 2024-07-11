
def multiples_of_3_or_5(num):
    list_of_multiples = [numbers for numbers in range(num) if numbers%3 == 0 or numbers%5 == 0]
    sum_of_multiples_of_3_or_5 = 0
    
    for x in list_of_multiples:
        sum_of_multiples_of_3_or_5 += x
        
    return sum_of_multiples_of_3_or_5

print(multiples_of_3_or_5(1000))