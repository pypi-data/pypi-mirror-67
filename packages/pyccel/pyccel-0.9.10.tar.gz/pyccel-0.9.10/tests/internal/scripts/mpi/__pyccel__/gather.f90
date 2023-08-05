
program prog_gather

use mpi
implicit none

integer(kind=4)  :: ierr  
integer(kind=4)  :: size  
integer(kind=8), allocatable  :: values (:) 
integer(kind=4)  :: block_length  
integer(kind=8), allocatable  :: data (:) 
integer(kind=4)  :: rank  
integer(kind=8)  :: i  
integer(kind=4)  :: master  
integer(kind=4)  :: comm  
integer(kind=8)  :: nb_values  
!coding: utf-8















!we need to declare these variables somehow,
!since we are calling mpi subroutines
ierr = Int(-1_8, 4)
size = Int(-1_8, 4)
rank = Int(-1_8, 4)


call mpi_init(ierr)


comm = mpi_comm_world
call mpi_comm_size(comm, size, ierr)
call mpi_comm_rank(comm, rank, ierr)


master = Int(1_8, 4)
nb_values = 8_8


block_length = floor(nb_values/Real(size, 8))


!...
allocate(values(0:block_length - 1_8))
values = 0
do i = 0_8, block_length - 1_8, 1
  values(i) = i + nb_values*rank + 1000_8


end do

print *, 'I, process ', rank, 'sent my values array : ', values
!...


!...
allocate(data(0:nb_values - 1_8))
data = 0


call mpi_gather(values, block_length, MPI_INTEGER8, data, block_length, &
      MPI_INTEGER8, master, comm, ierr)
!...


if (rank == master ) then
  print *, 'I, process ', rank, ', received ', data, ' of process ', master
end if
call mpi_finalize(ierr)

end program prog_gather