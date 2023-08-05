function zip_prod (m) result(res)

  use mod_on8we4im, only: mod_zip_prod => zip_prod
  implicit none
  integer(kind=8), intent(in)  :: m 
  integer(kind=8)  :: res  

  res = mod_zip_prod(m)
end function