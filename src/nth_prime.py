def nth_prime(nth_term): 
    x = 2
    count = 0
    found_prime = False
    while not found_prime:
        for i in range(2, x):
            if x%i == 0:
                break
        else:
            count += 1
            if count == nth_term:
                found_prime = True
                break
        x += 1  
    print(count)  
    print(x)        
    

print(nth_prime(10001))