def power_digit_sum(num):
    
    num_list = [int(x) for x in str(pow(2, num))]

    return sum(num_list)

print(power_digit_sum(1000))