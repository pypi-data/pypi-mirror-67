function enumerate_on_1d_array (n0_z, z) result(res)

  use mod_lwmd2f9e, only: mod_enumerate_on_1d_array => &
      enumerate_on_1d_array
  implicit none
  integer(kind=4), intent(in)  :: n0_z 
  integer(kind=8), intent(in)  :: z (0:n0_z-1)
  integer(kind=8)  :: res  

  res = mod_enumerate_on_1d_array(z)
end function