module mod_x1kgr9s7

implicit none




contains

!........................................
subroutine product_loop_on_real_array(z, out) 

  implicit none
  real(kind=8), intent(in)  :: z (0:)
  real(kind=8), intent(inout)  :: out (0:)
  integer(kind=8), allocatable  :: s (:) 
  integer(kind=8)  :: n  
  integer(kind=8)  :: i  






  allocate(s(0:0))
  s = [size(z,1)]
  n = s(0_8)


  do i = 0, n - 1_8, 1
    out(i) = z(i)**2_8
  end do

end subroutine
!........................................

end module