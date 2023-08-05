@types( 'int[:]' )
def map_on_1d_array( z ):

    @types( int )
    def f( x ):
        return x+5

    res = 0
    for v in map( f, z ):
        res *= v

    return res
