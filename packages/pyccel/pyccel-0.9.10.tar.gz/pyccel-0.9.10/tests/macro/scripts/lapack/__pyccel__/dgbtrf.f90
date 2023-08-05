
program prog_dgbtrf

implicit none

integer(kind=8)  :: mu  
real(kind=8), allocatable  :: a (:,:) 
integer(kind=8), allocatable  :: ipiv (:) 
integer(kind=8)  :: info  
integer(kind=8)  :: ml  
integer(kind=8)  :: lda  
integer(kind=8)  :: n  
integer(kind=8)  :: m  




n = 25_8
ml = 1_8
mu = 1_8
lda = 2_8*ml + mu + 1_8


allocate(a(0:lda - 1_8, 0:n - 1_8))
a = 0.0


!Superdiagonal, Diagonal, Subdiagonal
m = ml + mu
a(m - 1_8, 1_8:n - 1_8) = -1.0d0
a(m, 0_8:n - 1_8) = 2.0d0
a(m + 1_8, 0_8:n - 2_8) = -1.0d0


info = -1_8
allocate(ipiv(0:n - 1_8))
ipiv = 0





call dgbtrf(n, n, ml, mu, a, lda, ipiv, info)

end program prog_dgbtrf