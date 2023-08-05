module mod_1hyglfhj

implicit none




contains

!........................................
subroutine double_loop_on_2d_array_F(z) 

  implicit none
  integer(kind=8), intent(inout)  :: z (0:,0:)
  integer(kind=8), allocatable  :: s (:) 
  integer(kind=8)  :: m  
  integer(kind=8)  :: n  
  integer(kind=8)  :: i  
  integer(kind=8)  :: j  






  allocate(s(0:1))
  s = [size(z,1), size(z,2)]
  m = s(0_8)
  n = s(1_8)


  do i = 0, m - 1_8, 1
    do j = 0, n - 1_8, 1
      z(i, j) = i - j
    end do

  end do

end subroutine
!........................................

end module