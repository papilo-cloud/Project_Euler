def pythagoran_triplet(number):
    for a in range(1, number):
        b = 1
        while b < a:
            c = number - a - b
            if ((a*a) + (b*b) - (c*c) == 0):
                print(a*b*c)
                
            b += 1
    
(pythagoran_triplet(1000))