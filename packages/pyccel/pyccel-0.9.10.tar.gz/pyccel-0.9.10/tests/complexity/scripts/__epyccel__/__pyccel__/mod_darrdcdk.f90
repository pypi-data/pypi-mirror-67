module mod_darrdcdk

implicit none




contains

!........................................
function double_loop(n) result(z)

  implicit none
  integer(kind=8)  :: z  
  integer(kind=8), value  :: n
  integer(kind=8)  :: x  
  integer(kind=8)  :: i  
  integer(kind=8)  :: y  
  integer(kind=8)  :: j  

  x = 0_8
  do i = 3_8, 9_8, 1
    x = x + 1_8
    y = n*x
    do j = 4_8, 14_8, 1
      z = x - y
    end do

  end do

  return
end function
!........................................

end module