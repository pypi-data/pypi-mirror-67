function double_loop (n) result(z)

  use mod_darrdcdk, only: mod_double_loop => double_loop
  implicit none
  integer(kind=8), intent(in)  :: n 
  integer(kind=8)  :: z  

  z = mod_double_loop(n)
end function