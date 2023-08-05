@types( int )
def double_loop( n ):
    x = 0
    for i in range( 3, 10 ):
        x += 1
        y  = n*x
        for j in range( 4, 15 ):
            z = x-y
    return z
