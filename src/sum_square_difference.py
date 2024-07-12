# Helper function 1
def sum_of_squares(n):
    sum = (n*(n + 1)*(2*n + 1)) / 6
    return sum
    
# Helper function 2
def squares_of_sum(n):
    sum = (n*(n + 1) / 2)
    return pow(sum, 2)
    
    
#  Sum Square Difference function
def sum_square_difference(n):
    return squares_of_sum(n) - sum_of_squares(n)

print(sum_square_difference(20))
