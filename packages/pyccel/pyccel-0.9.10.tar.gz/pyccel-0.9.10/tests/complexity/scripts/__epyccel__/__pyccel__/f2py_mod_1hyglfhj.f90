subroutine double_loop_on_2d_array_F (n0_z, n1_z, z) 

  use mod_1hyglfhj, only: mod_double_loop_on_2d_array_F => &
      double_loop_on_2d_array_F
  implicit none
  integer(kind=4), intent(in)  :: n0_z 
  integer(kind=4), intent(in)  :: n1_z 
  integer(kind=8), intent(inout)  :: z (0:n0_z-1,0:n1_z-1)

  call mod_double_loop_on_2d_array_F(z)
end subroutine