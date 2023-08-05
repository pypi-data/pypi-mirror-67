module mod_on8we4im

implicit none




contains

!........................................
function zip_prod(m) result(res)

  implicit none
  integer(kind=8)  :: res  
  integer(kind=8), value  :: m
  integer(kind=8)  :: i  
  integer(kind=8), pointer  :: x (:) 
  integer(kind=8)  :: Dummy_0062  
  integer(kind=8)  :: j  
  integer(kind=8), pointer  :: y (:) 
  integer(kind=8)  :: Dummy_1215  
  integer(kind=8)  :: Dummy_1933  
  integer(kind=8)  :: i2  
  integer(kind=8)  :: i1  



  allocate(x(0:m))
  Dummy_0062 = 0_8
  do i = 0, m - 1_8, 1
    x(Dummy_0062) = i
    Dummy_0062 = Dummy_0062 + 1_8
  end do

  allocate(y(0:m))
  Dummy_1215 = 0_8
  do j = 0, m - 1_8, 1
    y(Dummy_1215) = 2_8*j
    Dummy_1215 = Dummy_1215 + 1_8
  end do



  res = 0_8
  do Dummy_1933 = 0, m - 1_8, 1
    i2 = y(Dummy_1933)
    i1 = x(Dummy_1933)
    res = i1*i2 + res


  end do

  return
end function
!........................................

end module