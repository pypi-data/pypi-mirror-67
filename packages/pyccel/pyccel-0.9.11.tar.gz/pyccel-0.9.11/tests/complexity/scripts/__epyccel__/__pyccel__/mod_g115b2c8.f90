module mod_g115b2c8

implicit none




contains

!........................................
function fibonacci(n) result(x)

  implicit none
  integer(kind=8)  :: x  
  integer(kind=8), value  :: n
  integer(kind=8)  :: y  
  integer(kind=8)  :: i  
  integer(kind=8)  :: z  

  x = 0_8
  y = 1_8
  do i = 0, n - 1_8, 1
    z = x + y
    x = y
    y = z
  end do

  return
end function
!........................................

end module