subroutine product_loop_on_real_array (n0_z, z, n0_out, out) 

  use mod_x1kgr9s7, only: mod_product_loop_on_real_array => &
      product_loop_on_real_array
  implicit none
  integer(kind=4), intent(in)  :: n0_z 
  real(kind=8), intent(in)  :: z (0:n0_z-1)
  integer(kind=4), intent(in)  :: n0_out 
  real(kind=8), intent(inout)  :: out (0:n0_out-1)

  call mod_product_loop_on_real_array(z,out)
end subroutine