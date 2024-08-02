def proper_divisor(num):
    sum_of_divisors = 0
    
    for i in range(1, (num // 2) + 1):
       if num%i == 0:
           sum_of_divisors += i
           
    return sum_of_divisors


def sum_of_amicable_numbers(n):
    
    index = 1
    sum = 0
    while index <= n:
        a = proper_divisor(index)
        b = proper_divisor(a)
        
        if index == b and index < a:
            sum += a + b

        index += 1
    return sum

print(sum_of_amicable_numbers(10000))