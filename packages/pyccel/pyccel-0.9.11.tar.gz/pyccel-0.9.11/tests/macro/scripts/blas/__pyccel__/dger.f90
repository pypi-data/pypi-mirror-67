
program prog_dger

implicit none

real(kind=8), allocatable  :: a (:,:) 
integer(kind=8)  :: incy  
real(kind=8), allocatable  :: y (:) 
integer(kind=8)  :: incx  
real(kind=8), allocatable  :: x (:) 
integer(kind=8)  :: n  
integer(kind=8)  :: m  
real(kind=8)  :: alpha  
!TODO - y must be optional






n = 4_8
m = 5_8


allocate(a(0:m - 1_8, 0:n - 1_8))
a = 0.0
allocate(x(0:m - 1_8))
x = 0.0
allocate(y(0:n - 1_8))
y = 0.0


!...
x(0_8) = 2.0d0
x(1_8) = 3.0d0
x(2_8) = 4.0d0
x(3_8) = 5.0d0
x(4_8) = 6.0d0
!...


!...
y(0_8) = 1.0d0
y(1_8) = -1.0d0
y(2_8) = 1.0d0
y(3_8) = -1.0d0
!...


alpha = 2.0d0
incx = 1_8
incy = 1_8





call dger(n, m, alpha, y, 1_8, x, 1_8, a, n)
print *, a

end program prog_dger