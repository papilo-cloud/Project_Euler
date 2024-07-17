# Prime number helper function
def is_prime(num):
    if num <= 1:
        return False
    for index in range(2, num):
        if num%index == 0:
            return False
    return True

def summation_of_primes(number):
    index = 0
    sum = 0
    while index < number:
        if is_prime(index):
            sum += index
        index += 1
    return sum

print(summation_of_primes(2000000))