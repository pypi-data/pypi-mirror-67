module mod_wrb1km9w

implicit none




contains

!........................................
subroutine product_loop_on_2d_array_C(z) 

  implicit none
  integer(kind=8), intent(inout)  :: z (0:,0:)
  integer(kind=8), allocatable  :: s (:) 
  integer(kind=8)  :: m  
  integer(kind=8)  :: n  
  integer(kind=8)  :: i  
  integer(kind=8), pointer  :: x (:) 
  integer(kind=8)  :: Dummy_0258  
  integer(kind=8)  :: j  
  integer(kind=8), pointer  :: y (:) 
  integer(kind=8)  :: Dummy_1119  
  integer(kind=8)  :: Dummy_194  
  integer(kind=8)  :: Dummy_41  







  allocate(s(0:1))
  s = [size(z,2), size(z,1)]
  m = s(0_8)
  n = s(1_8)


  allocate(x(0:m))
  Dummy_0258 = 0_8
  do i = 0, m - 1_8, 1
    x(Dummy_0258) = i
    Dummy_0258 = Dummy_0258 + 1_8
  end do

  allocate(y(0:n))
  Dummy_1119 = 0_8
  do j = 0, n - 1_8, 1
    y(Dummy_1119) = j
    Dummy_1119 = Dummy_1119 + 1_8
  end do



  do Dummy_194 = 0, m - 1_8, 1
    do Dummy_41 = 0, n - 1_8, 1
      j = y(Dummy_41)
      i = x(Dummy_194)
      z(j, i) = i - j
    end do
  end do

end subroutine
!........................................

end module