
def even_fibonacci_numbers(num):
    current_fib = 1
    prev_fib = 0
    count = 1
    sum = 0
    while count < num:
        if current_fib % 2 == 0:
            sum += current_fib
            
        print(prev_fib, end=" ",)    
        current_fib = prev_fib + current_fib
        prev_fib =  current_fib - prev_fib
        count += 1
    print('\n',sum)

# 4000000 is actually a large number :(
even_fibonacci_numbers(4000)