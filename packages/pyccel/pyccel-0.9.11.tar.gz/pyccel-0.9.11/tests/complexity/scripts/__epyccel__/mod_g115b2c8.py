@types( int )
def fibonacci( n ):
    x = 0
    y = 1
    for i in range( n ):
        z = x+y
        x = y
        y = z
    return x
