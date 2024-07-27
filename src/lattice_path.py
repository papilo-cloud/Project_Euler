# Factorial number helper function
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)


def lattice_path(k, n):
    # In a (k x n) grid, the number of lattice path from
    # coordinates (0,0) to (k,n) is equal to the number
    # of combinations of (k) objects out of (k+n) options
    #  n!/(n-k)!(k!)
    # for our matrix, (n = k = 20)
    
    n = k + n
    routes = factorial(n) // (factorial(k) * factorial(n - k))
    
    print(f'routes {routes}')
lattice_path(3, 6)