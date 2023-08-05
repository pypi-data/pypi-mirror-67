@types( int )
def sum_natural_numbers( n ):
    x = 0
    for i in range( 1, n+1 ):
        x += i
    return x
