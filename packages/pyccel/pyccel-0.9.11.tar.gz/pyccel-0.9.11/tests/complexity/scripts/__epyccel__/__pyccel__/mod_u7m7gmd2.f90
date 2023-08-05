module mod_u7m7gmd2

implicit none




contains

!........................................
pure  subroutine const_complex_bool_int(Dummy_9830, Dummy_132, Dummy_377 &
      )

implicit none
complex(kind=8), intent(out)  :: Dummy_9830 
logical(kind=4), intent(out)  :: Dummy_132 
integer(kind=8), intent(out)  :: Dummy_377 

Dummy_9830 = cmplx(1_8,2_8)
Dummy_132 = .False.
Dummy_377 = 8_8
return
end subroutine
!........................................

end module