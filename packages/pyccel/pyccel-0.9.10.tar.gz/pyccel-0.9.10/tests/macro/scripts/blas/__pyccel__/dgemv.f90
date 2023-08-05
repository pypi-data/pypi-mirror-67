
program prog_dgemv

implicit none

real(kind=8), allocatable  :: a (:,:) 
real(kind=8), allocatable  :: y (:) 
real(kind=8)  :: beta  
real(kind=8), allocatable  :: x (:) 
integer(kind=8)  :: n  
integer(kind=8)  :: m  
real(kind=8)  :: alpha  
!TODO - y must be optional
!- t must be optiona, default 0 (map 1 -> 'T' and 0 -> 'N')
!- default value for beta must be 0.0 and not 0






n = 4_8
m = 5_8


allocate(a(0:m - 1_8, 0:n - 1_8))
a = 0.0
allocate(x(0:m - 1_8))
x = 0.0
allocate(y(0:n - 1_8))
y = 0.0


!...
a(0_8, 0_8) = 1.0d0
a(0_8, 1_8) = 6.0d0
a(0_8, 2_8) = 11.0d0
a(0_8, 3_8) = 16.0d0


a(1_8, 0_8) = 2.0d0
a(1_8, 1_8) = 7.0d0
a(1_8, 2_8) = 12.0d0
a(1_8, 3_8) = 17.0d0


a(2_8, 0_8) = 3.0d0
a(2_8, 1_8) = 8.0d0
a(2_8, 2_8) = 13.0d0
a(2_8, 3_8) = 18.0d0


a(3_8, 0_8) = 4.0d0
a(3_8, 1_8) = 9.0d0
a(3_8, 2_8) = 14.0d0
a(3_8, 3_8) = 19.0d0


a(4_8, 0_8) = 5.0d0
a(4_8, 1_8) = 10.0d0
a(4_8, 2_8) = 15.0d0
a(4_8, 3_8) = 20.0d0
!...


!...
x(0_8) = 2.0d0
x(1_8) = 3.0d0
x(2_8) = 4.0d0
x(3_8) = 5.0d0
x(4_8) = 6.0d0
!...


alpha = 2.0d0
beta = 0.0d0





call dgemv('N', n, m, alpha, a, n, x, 1_8, 0_8, y, 1_8)
print *, y

end program prog_dgemv