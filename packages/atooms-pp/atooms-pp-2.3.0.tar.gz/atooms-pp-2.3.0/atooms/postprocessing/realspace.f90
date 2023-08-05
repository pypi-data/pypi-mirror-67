module compute

  implicit none

  real(8), parameter :: PI = 4 * atan(1.0_8)

contains

  subroutine self_overlap(pos1, pos2, a_square, q)
    real(8),intent(in) :: pos1(:,:), pos2(:,:), a_square
    real(8),intent(out) :: q
    real(8) :: tmp(size(pos1,1))
    integer :: i
    do i = 1,size(pos1,1)
       tmp(i) = sum((pos1(i,:) - pos2(i,:))**2)
    end do
    q = count(tmp .lt. a_square)
  end subroutine self_overlap

  subroutine pbc(dist,boxDim)
      real(8), intent(inout)  :: dist(:)
      real(8), intent(in)     :: boxDim(:)
      where (abs(dist) > boxDim/2)
         dist = dist - sign(boxDim,dist)
      end where
  end subroutine pbc

  subroutine pbch(dist,boxDim,hbox)
    real(8), intent(inout)  :: dist(:)
    real(8), intent(in)     :: boxDim(:), hbox(:)
    where (abs(dist) > hbox)
       dist = dist - sign(boxDim,dist)
    end where
  end subroutine pbch

  subroutine bond_angle(center,positions,neighbors,box,dtheta,hist)
    ! Parameters
    real(8), intent(in)       :: center(:)
    real(8), intent(in)       :: positions(:,:)
    integer(4), intent(in)    :: neighbors(:)
    real(8), intent(in)       :: box(:)
    real(8), intent(in)       :: dtheta
    integer(4), intent(inout) :: hist(:)
    ! Variables
    real(8)    :: r_ij(3), r_ik(3), d_ij, d_ik
    integer(4) :: nNeighbors, nPoints, j, neigh_j, k, neigh_k, bin
    real(8)    :: dotprod, prod, costheta, theta
    ! Computation
    hist = 0
    nNeighbors = size(neighbors)
    nPoints = size(hist)
    ! Loop over all neighbors j
    do j=1,nNeighbors
      neigh_j = neighbors(j)+1  ! PYTHON
      r_ij(:) = center(:) - positions(:,neigh_j)
      call pbc(r_ij,box)
      d_ij = sqrt(sum(r_ij**2))
      ! Loop over all neighbors k != j
      do k=1,nNeighbors
        neigh_k = neighbors(k)+1  ! PYTHON
        if (neigh_k /= neigh_j) then
          r_ik(:) = center(:) - positions(:,neigh_k)  
          call pbc(r_ik,box)
          d_ik = sqrt(sum(r_ik**2))
          ! Angle (k,i,j)
          dotprod = sum(r_ij*r_ik)
          prod = d_ij*d_ik
          if (prod == 0.0_8) cycle
          costheta = dotprod/prod
          ! Enforce cos(theta) >= -1
          if (costheta <= 0.0) then 
            costheta = DMAX1(-1.0_8,costheta)
          end if
          ! Enforce cos(theta) <= 1
          if (costheta > 0.0) then
            costheta = DMIN1(1.0_8,costheta)
          end if
          theta = acos(costheta)*180.0/pi
          ! Binning
          !bin = NINT(theta)+1
          !--test
          bin = floor(theta/dtheta) + 1
          if (bin <= nPoints) hist(bin) = hist(bin) + 1
        end if
      end do
    end do
  end subroutine bond_angle

  !! Find nearest neighbors 
  !!
  !! Neighbors list is in C-order for easier handling in python.
  !! Also we give up III law because this avoids sorting the neighbors
  !! indices later and overall this is more efficient
  !! 
  subroutine neighbors_list(offset,box,pos,ids,rcut,nn,neigh)
    character(1), intent(in)  :: offset
    real(8), intent(in)  :: box(:)
    real(8), intent(in)  :: pos(:,:)
    real(8), intent(in)  :: rcut(:,:)
    integer, intent(in)  :: ids(:)
    integer, intent(inout) :: nn(:)
    integer, intent(inout) :: neigh(:,:)
    real(8)              :: rij(size(pos,1)), rijsq, hbox(size(pos,1))
    real(8)              :: rcutsq(size(rcut,1),size(rcut,2))
    integer              :: i, j, isp, jsp, delta
    if (offset == 'C') then
       delta = -1
    else
       delta = 0
    end if    
    nn = 0
    hbox = box / 2
    rcutsq = rcut**2
    do i = 1,size(pos,2)
       isp = ids(i)
       do j = i+1,size(pos,2)
          jsp = ids(j)
          rij = pos(:,i) - pos(:,j)
          where (abs(rij) > hbox)
             rij = rij - sign(box,rij)
          end where
          rijsq = dot_product(rij,rij)
          if (rijsq < rcutsq(isp,jsp)) then
             nn(i) = nn(i) + 1
             nn(j) = nn(j) + 1
             neigh(i,nn(i)) = j+delta
             neigh(j,nn(j)) = i+delta
          end if
       end do
    end do
  end subroutine neighbors_list

  subroutine neighbors(offset,box,center,pos,ids,rcut,nn,neigh)
    character(1), intent(in)  :: offset
    real(8), intent(in)  :: box(:)
    real(8), intent(in)  :: center(:), pos(:,:)
    real(8), intent(in)  :: rcut(:)
    integer, intent(in)  :: ids(:)
    integer, intent(inout) :: nn
    integer, intent(inout) :: neigh(:)
    real(8)              :: rij(size(pos,1)), rijsq, hbox(size(pos,1))
    real(8)              :: rcutsq(size(rcut))
    integer              :: i, j, isp, jsp, delta
    if (offset == 'C') then
       delta = -1
    else
       delta = 0
    end if    
    nn = 0
    hbox = box / 2
    rcutsq = rcut**2
    do j = 1,size(pos,2)
       jsp = ids(j) - delta
       rij = center(:) - pos(:,j)
       where (abs(rij) > hbox)
          rij = rij - sign(box,rij)
       end where
       rijsq = dot_product(rij,rij)
       if (rijsq < rcutsq(jsp)) then
          nn = nn + 1
          neigh(nn) = j+delta
       end if
    end do
  end subroutine neighbors

  subroutine gr_self(pidx, positions, box, hbox, distances, k)
    integer(8), intent(in)    :: pidx(:)
    integer(8), intent(out) :: k
    real(8), intent(inout)    :: distances(:)
    real(8), intent(in)       :: positions(:,:)
    real(8), intent(in)       :: box(:), hbox(size(box))
    real(8)    :: dist(size(box)), dist_sq, pos(size(box))
    integer(8) :: i, j, ii
    k = 0
    do ii=1,size(pidx)
       i = pidx(ii)
       pos = positions(:,i)
       do j=i+1,size(positions,2)
          k = k+1
          dist(:) = positions(:,j) - pos(:)
          !dist(1) = positions(1,j) - pos(1)
          !dist(2) = positions(2,j) - pos(2)
          !dist(3) = positions(3,j) - pos(3)
          !if (abs(dist(1)) > hbox(1)) dist(1) = dist(1) - sign(box(1), dist(1))
          !if (abs(dist(2)) > hbox(2)) dist(2) = dist(2) - sign(box(2), dist(2))
          !if (abs(dist(3)) > hbox(3)) dist(3) = dist(3) - sign(box(3), dist(3))
          where (abs(dist) > hbox)
             dist = dist - sign(box,dist)
          end where
          !distances(k) = sqrt(dist(1)**2 + dist(2)**2 + dist(3)**2)
          distances(k) = sqrt(sum(dist**2))
       end do
    end do
  end subroutine gr_self

  subroutine gr_distinct(pidx, positions1, positions2, box, hbox, distances, k)
    integer(8), intent(in)    :: pidx(:)
    integer(8), intent(out) :: k
    real(8), intent(inout)    :: distances(:)
    real(8), intent(in)       :: positions1(:,:), positions2(:,:)
    real(8), intent(in)       :: box(:), hbox(size(box))
    real(8)    :: dist(size(box)), dist_sq, pos(size(box))
    integer(8) :: i, j, ii
    k = 0
    do ii=1,size(pidx)
       i = pidx(ii)
       pos = positions1(:,i)
       do j=1,size(positions2,2)
          k = k+1
          !dist(1) = positions1(1,j) - pos(1)
          !dist(2) = positions1(2,j) - pos(2)
          !dist(3) = positions1(3,j) - pos(3)
          dist(:) = positions2(:,j) - pos(:)
          !if (abs(dist(1)) > hbox(1)) dist(1) = dist(1) - sign(box(1), dist(1))
          !if (abs(dist(2)) > hbox(2)) dist(2) = dist(2) - sign(box(2), dist(2))
          !if (abs(dist(3)) > hbox(3)) dist(3) = dist(3) - sign(box(3), dist(3))
          where (abs(dist) > hbox)
             dist = dist - sign(box,dist)
          end where
          !distances(k) = sqrt(dist(1)**2 + dist(2)**2 + dist(3)**2)
          distances(k) = sqrt(sum(dist**2))
       end do
    end do
  end subroutine gr_distinct
  
end module compute
