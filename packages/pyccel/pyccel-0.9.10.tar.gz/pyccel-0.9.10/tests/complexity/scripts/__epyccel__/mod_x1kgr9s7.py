@types( 'real[:], real[:]' )
def product_loop_on_real_array( z, out ):

    from numpy     import shape

    s = shape( z )
    n = s[0]

    for i in range(n):
        out[i] = z[i]**2
