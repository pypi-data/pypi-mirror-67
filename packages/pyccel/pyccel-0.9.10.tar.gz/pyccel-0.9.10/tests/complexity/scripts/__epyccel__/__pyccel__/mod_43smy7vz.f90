module mod_43smy7vz

implicit none




contains

!........................................
function map_on_1d_array(z) result(res)

  implicit none
  integer(kind=8)  :: res  
  integer(kind=8), intent(in)  :: z (0:)
  integer(kind=8)  :: Dummy_2766  
  integer(kind=8)  :: v  




  res = 0_8
  do Dummy_2766 = 0, size(z,1) - 1_8, 1
    v = f(z(Dummy_2766))
    res = res*v


  end do

  return
  contains 
  function f(x) result(Dummy_5211)

    implicit none
    integer(kind=8)  :: Dummy_5211  
    integer(kind=8), value  :: x

    Dummy_5211 = x + 5_8
    return
  end function
end function
!........................................

end module