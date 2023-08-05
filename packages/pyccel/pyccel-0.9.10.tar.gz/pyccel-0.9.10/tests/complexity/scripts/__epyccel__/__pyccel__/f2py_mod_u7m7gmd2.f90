subroutine const_complex_bool_int (Dummy_9830, Dummy_132, Dummy_377) 

  use mod_u7m7gmd2, only: mod_const_complex_bool_int => &
      const_complex_bool_int
  implicit none
  complex(kind=8), intent(out)  :: Dummy_9830 
  logical(kind=4), intent(out)  :: Dummy_132 
  integer(kind=8), intent(out)  :: Dummy_377 

  call mod_const_complex_bool_int(Dummy_9830,Dummy_132,Dummy_377)
end subroutine