function sum_natural_numbers (n) result(x)

  use mod_6nra8ygw, only: mod_sum_natural_numbers => sum_natural_numbers
  implicit none
  integer(kind=8), intent(in)  :: n 
  integer(kind=8)  :: x  

  x = mod_sum_natural_numbers(n)
end function