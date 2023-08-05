module mod_weld3rua

implicit none




contains

!........................................
function factorial(n) result(x)

  implicit none
  integer(kind=8)  :: x  
  integer(kind=8), value  :: n
  integer(kind=8)  :: i  

  x = 1_8
  do i = 2_8, n, 1
    x = i*x
  end do

  return
end function
!........................................

end module