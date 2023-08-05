function fibonacci (n) result(x)

  use mod_g115b2c8, only: mod_fibonacci => fibonacci
  implicit none
  integer(kind=8), intent(in)  :: n 
  integer(kind=8)  :: x  

  x = mod_fibonacci(n)
end function