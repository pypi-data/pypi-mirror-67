@types( int )
def zip_prod( m ):

    x = [  i for i in range(m)]
    y = [2*j for j in range(m)]

    res = 0
    for i1,i2 in zip( x, y ):
        res += i1*i2

    return res
