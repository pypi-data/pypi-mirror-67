module mod_lwmd2f9e

implicit none




contains

!........................................
function enumerate_on_1d_array(z) result(res)

  implicit none
  integer(kind=8)  :: res  
  integer(kind=8), intent(in)  :: z (0:)
  integer(kind=8)  :: i  
  integer(kind=8)  :: v  



  res = 0_8
  do i = 0, size(z,1) - 1_8, 1
    v = z(i)
    res = i*v + res


  end do

  return
end function
!........................................

end module