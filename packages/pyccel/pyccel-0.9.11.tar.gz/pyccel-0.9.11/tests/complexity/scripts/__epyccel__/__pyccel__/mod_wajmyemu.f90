module mod_wajmyemu

implicit none




contains

!........................................
pure  subroutine expr_complex_int_bool(n, Dummy_6173, Dummy_6272, &
      Dummy_4104)

implicit none
complex(kind=8), intent(out)  :: Dummy_6173 
integer(kind=8), intent(out)  :: Dummy_6272 
logical(kind=8), intent(out)  :: Dummy_4104 
integer(kind=8), value  :: n

Dummy_6173 = cmplx(0,1)*n + 0.5d0
Dummy_6272 = 2_8*n
Dummy_4104 = n == 3_8 
return
end subroutine
!........................................

end module