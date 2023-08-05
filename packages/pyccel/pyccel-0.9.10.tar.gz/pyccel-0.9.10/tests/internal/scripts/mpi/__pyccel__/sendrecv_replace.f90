
program prog_sendrecv_replace

use mpi
implicit none

integer(kind=4)  :: ierr  
integer(kind=4)  :: size  
integer(kind=4)  :: count  
integer(kind=4)  :: rank  
integer(kind=4)  :: partner  
integer(kind=4), allocatable  :: status (:) 
integer(kind=4)  :: comm  
integer(kind=4)  :: msg  
integer(kind=4)  :: tag  
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


if (rank == 0_8 ) then
  partner = Int(1_8, 4)
end if
if (rank == 1_8 ) then
  partner = Int(0_8, 4)
end if
msg = rank + 1000_8


count = Int(1_8, 4)
tag = Int(1234_8, 4)
allocate(status(0:mpi_status_size - 1_8))
status = 0


call mpi_sendrecv_replace(msg, count, MPI_INTEGER8, partner, tag, &
      partner, tag, comm, status, ierr)


print *, 'I, process ', rank, ', I received', msg, ' from process ', partner


call mpi_finalize(ierr)

end program prog_sendrecv_replace