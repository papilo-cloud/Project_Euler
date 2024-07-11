# helper function
def is_prime(x):
    if x <= 1:
        return False
    for index in range(2, x):
        if x%index == 0:
            return False
    return True


# largest prime factor function
def largest_prime_factor(number):
    for index in range(number//2, 2, -1):
        if number%index == 0:
            if is_prime(index):
                print(index)
                break
largest_prime_factor(13195)

