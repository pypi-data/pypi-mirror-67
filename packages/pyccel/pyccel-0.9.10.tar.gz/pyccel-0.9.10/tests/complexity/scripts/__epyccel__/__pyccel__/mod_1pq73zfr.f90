module mod_1pq73zfr

implicit none




contains

!........................................
subroutine product_loop_on_2d_array_F(z) 

  implicit none
  integer(kind=8), intent(inout)  :: z (0:,0:)
  integer(kind=8), allocatable  :: s (:) 
  integer(kind=8)  :: m  
  integer(kind=8)  :: n  
  integer(kind=8)  :: i  
  integer(kind=8), pointer  :: x (:) 
  integer(kind=8)  :: Dummy_0303  
  integer(kind=8)  :: j  
  integer(kind=8), pointer  :: y (:) 
  integer(kind=8)  :: Dummy_1145  
  integer(kind=8)  :: Dummy_10  
  integer(kind=8)  :: Dummy_327  







  allocate(s(0:1))
  s = [size(z,1), size(z,2)]
  m = s(0_8)
  n = s(1_8)


  allocate(x(0:m))
  Dummy_0303 = 0_8
  do i = 0, m - 1_8, 1
    x(Dummy_0303) = i
    Dummy_0303 = Dummy_0303 + 1_8
  end do

  allocate(y(0:n))
  Dummy_1145 = 0_8
  do j = 0, n - 1_8, 1
    y(Dummy_1145) = j
    Dummy_1145 = Dummy_1145 + 1_8
  end do



  do Dummy_10 = 0, m - 1_8, 1
    do Dummy_327 = 0, n - 1_8, 1
      j = y(Dummy_327)
      i = x(Dummy_10)
      z(i, j) = i - j
    end do
  end do

end subroutine
!........................................

end module