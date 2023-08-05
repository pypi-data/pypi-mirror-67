@types( 'int[:,:](order=F)' )
def double_loop_on_2d_array_F( z ):

    from numpy import shape

    s = shape( z )
    m = s[0]
    n = s[1]

    for i in range( m ):
        for j in range( n ):
            z[i,j] = i-j
