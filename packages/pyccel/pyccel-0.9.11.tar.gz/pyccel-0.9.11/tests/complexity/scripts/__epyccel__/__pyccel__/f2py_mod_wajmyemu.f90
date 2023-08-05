subroutine expr_complex_int_bool (n, Dummy_6173, Dummy_6272, Dummy_4104 &
      )

  use mod_wajmyemu, only: mod_expr_complex_int_bool => &
      expr_complex_int_bool
  implicit none
  integer(kind=8), intent(in)  :: n 
  complex(kind=8), intent(out)  :: Dummy_6173 
  integer(kind=8), intent(out)  :: Dummy_6272 
  logical(kind=8), intent(out)  :: Dummy_4104 

  call mod_expr_complex_int_bool(n,Dummy_6173,Dummy_6272,Dummy_4104)
end subroutine