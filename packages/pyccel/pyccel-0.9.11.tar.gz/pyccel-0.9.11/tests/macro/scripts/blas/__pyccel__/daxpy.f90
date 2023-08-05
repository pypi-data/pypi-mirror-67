
program prog_daxpy

implicit none

integer(kind=8)  :: n  
real(kind=8), allocatable  :: a (:) 
real(kind=8), allocatable  :: b (:) 
real(kind=8)  :: alpha  
!TODO default value for alpha must double and not int
!right now, textx raises an error, when we pass 1.0




n = 4_8


allocate(a(0:n - 1_8))
a = 0.0
allocate(b(0:n - 1_8))
b = 0.0


a(0_8) = 2.0d0
a(1_8) = 3.0d0
a(2_8) = 4.0d0
a(3_8) = 5.0d0


b(0_8) = 5.0d0
b(1_8) = 4.0d0
b(2_8) = 9.0d0
b(3_8) = 2.0d0


alpha = 2.0d0



call daxpy(n, alpha, a, 1_8, b, 1_8)
print *, b

end program prog_daxpy