function factorial (n) result(x)

  use mod_weld3rua, only: mod_factorial => factorial
  implicit none
  integer(kind=8), intent(in)  :: n 
  integer(kind=8)  :: x  

  x = mod_factorial(n)
end function