module mod_6nra8ygw

implicit none




contains

!........................................
function sum_natural_numbers(n) result(x)

  implicit none
  integer(kind=8)  :: x  
  integer(kind=8), value  :: n
  integer(kind=8)  :: i  

  x = 0_8
  do i = 1_8, n, 1
    x = i + x
  end do

  return
end function
!........................................

end module