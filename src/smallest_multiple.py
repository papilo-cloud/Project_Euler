# Greatest Common Divisor helper function
def gcd(a, b):
    while a%b != 0:
        r = a%b
        a = b
        b = r 
    return b 


# Function to calculate the Lowest Common Multiple of numbers 
def lcm(list):
    nxt_val = 1
    crnt_lcm = list[0]  # Assume the current LCM is at index 0
    while nxt_val < len(list):
        crnt_lcm = (crnt_lcm*list[nxt_val]) / gcd(crnt_lcm, list[nxt_val])
        nxt_val += 1
    print(crnt_lcm)
    

lcm([1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        

    
