subroutine product_loop_on_2d_array_F (n0_z, n1_z, z) 

  use mod_1pq73zfr, only: mod_product_loop_on_2d_array_F => &
      product_loop_on_2d_array_F
  implicit none
  integer(kind=4), intent(in)  :: n0_z 
  integer(kind=4), intent(in)  :: n1_z 
  integer(kind=8), intent(inout)  :: z (0:n0_z-1,0:n1_z-1)

  call mod_product_loop_on_2d_array_F(z)
end subroutine