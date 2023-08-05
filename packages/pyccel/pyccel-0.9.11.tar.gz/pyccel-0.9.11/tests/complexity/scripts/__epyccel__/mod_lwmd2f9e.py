@types( 'int[:]' )
def enumerate_on_1d_array( z ):

    res = 0
    for i,v in enumerate( z ):
        res += v*i

    return res
