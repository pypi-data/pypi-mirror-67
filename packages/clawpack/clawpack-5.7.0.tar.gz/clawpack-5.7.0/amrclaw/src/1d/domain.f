c
c  ----------------------------------------------------------
c
      subroutine domain (nvar,vtime,nx,naux,start_time)
c
      use amr_module
      implicit double precision (a-h,o-z)
      logical    vtime

c
c  allocate initial coarse grid domain. set node info & initialize grid
c  initial space and time step set here too
c
      mstart = nodget()
c
c code assumes in many places that lower left corner at (0)
c this initial code sets the domain
c if it is too large, birect will chop it up into several pieces
c
      rnode(cornxlo,mstart)   = xlower
      rnode(cornxhi,mstart)   = xupper
      node(nestlevel,mstart) = 1
      node(levelptr,mstart)  = 0
      lstart(1) = mstart

      if (flag_richardson) then
      if (((nx/2)*2 .ne. nx)) then
         write(outunit,*)" must have even number of cells"
         write(*,*)      " must have even number of cells"
         stop
      endif
      endif

      node(ndilo,mstart) = 0
      node(ndihi,mstart) = nx-1

      lfine = 1
      call  birect(mstart)
      call  ginit (mstart, .true., nvar, naux, start_time)
c
c  compute number of grids at level 1 (may have been bi-rected above)
c  needs to be done here since this is used when calling advanc for
c  parallelization
      ngrids = 0
      ncells = 0
       mptr = lstart(1)
       do while (mptr .gt. 0)
          ngrids = ngrids + 1
          ncells = ncells + (node(ndihi,mptr)-node(ndilo,mptr)+1)
          mptr = node(levelptr, mptr)
       end do
       numgrids(1) = ngrids
       numcells(1) = ncells
       avenumgrids(1) = avenumgrids(1) + ngrids
       iregridcount(1) = 1
       if (ngrids .gt. 1) call arrangeGrids(1,ngrids)

       write(*,100) ngrids,ncells
 100   format("there are ",i4," grids with ",i8," cells at level   1")

c      set lbase to 1 here, to put domain 1 grids in lsit
c      once and for all.  Only here, this once, (and if restarting)
c      does listStart have to be set outside of makeGridList
c      but call it with lbase 0 to make grid 1
       listStart(1) = 1
       call makeGridList(0)
       call makeBndryList(1)  ! 1 means level 1
c
c  set stable initial time step using coarse grid data
c
      if (vtime) then
         mptr = lstart(1)
         dx   = hxposs(1)
         dt   = possk(1)
         dtgrid = dt
 60           mitot = node(ndihi,mptr)-node(ndilo,mptr) + 1 + 2*nghost
              locaux = node(storeaux,mptr)
c             # added cfl to call to estdt so call.i isnt needed in estdt:
              call estdt(alloc(node(store1,mptr)),mitot,nvar,
     1                   dx,dtgrid,nghost,alloc(locaux),naux,cfl)
              dt = dmin1(dt,dtgrid)
              mptr   = node(levelptr,mptr)
            if (mptr .ne. 0) go to 60
         possk(1) = dt
      endif
c
c set rest of possk array for refined timesteps
c
      iregsz(1) = nx
      iregst(1) = 0
      iregend(1) = nx-1
      do 70 level = 2, mxnest
         iregsz(level) = iregsz(level-1) * intratx(level-1)
         possk(level)  = possk(level-1)/dble(kratio(level-1))
 70   continue
c
      return
      end
