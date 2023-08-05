@types( 'int[:,:](order=F)' )
def product_loop_on_2d_array_F( z ):

    from numpy     import shape
    from itertools import product

    s = shape( z )
    m = s[0]
    n = s[1]

    x = [i for i in range(m)]
    y = [j for j in range(n)]

    for i,j in product( x, y ):
        z[i,j] = i-j
