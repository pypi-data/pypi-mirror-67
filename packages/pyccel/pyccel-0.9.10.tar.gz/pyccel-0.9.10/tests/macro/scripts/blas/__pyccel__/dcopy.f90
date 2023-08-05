
program prog_dcopy

implicit none

integer(kind=8)  :: n  
real(kind=8), allocatable  :: a (:) 
real(kind=8), allocatable  :: b (:) 




n = 4_8


allocate(a(0:n - 1_8))
a = 0.0
allocate(b(0:n - 1_8))
b = 0.0


a(0_8) = 2.0d0
a(1_8) = 3.0d0
a(2_8) = 4.0d0
a(3_8) = 5.0d0



call dcopy(n, a, 1_8, b, 1_8)
print *, b

end program prog_dcopy