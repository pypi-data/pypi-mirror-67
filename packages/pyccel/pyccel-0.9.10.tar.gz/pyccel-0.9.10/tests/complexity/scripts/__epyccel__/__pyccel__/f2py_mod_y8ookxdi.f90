subroutine double_loop_on_2d_array_C (n0_z, n1_z, z) 

  use mod_y8ookxdi, only: mod_double_loop_on_2d_array_C => &
      double_loop_on_2d_array_C
  implicit none
  integer(kind=4), intent(in)  :: n0_z 
  integer(kind=4), intent(in)  :: n1_z 
  integer(kind=8), intent(inout)  :: z (0:n1_z-1,0:n0_z-1)

  !f2py integer(kind=8) :: n0_z=shape(z,0)
  !f2py integer(kind=8) :: n1_z=shape(z,1)
  !f2py intent(c) z
  call mod_double_loop_on_2d_array_C(z)
end subroutine