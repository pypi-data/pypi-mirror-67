c
c -------------------------------------------------------------
c
      subroutine ginit(msave, first, nvar, naux, start_time)
c
      use amr_module
      implicit double precision (a-h,o-z)
      logical first
      
      !for setaux timing
      integer :: clock_start, clock_finish, clock_rate
      real(kind=8) :: cpu_start, cpu_finish


c ::::::::::::::::::::::::::::: GINIT ::::::::::::::::::::::::
c
c  initializes soln on all grids at 'level'  by calling qinit
c  if first = true, (first call to init), then allocate the
c  soln storage area too, else was already allocated.
c
c :::::::::::::::::::::::::::::::::::::::;::::::::::::::::::::

      if (msave .eq. 0) go to 99

      level = node(nestlevel,msave)
      hx    = hxposs(level)
      mptr  = msave
 
 10       nx      = node(ndihi,mptr) - node(ndilo,mptr) + 1
          mitot   = nx + 2*nghost
          corn1   = rnode(cornxlo,mptr)
          if(.not. (first)) go to 20
              loc                 = igetsp(mitot*nvar)
              node(store1,mptr)   = loc
              if (naux .gt. 0) then
                locaux              = igetsp(mitot*naux)
                do k = 1, mitot*naux,naux  ! set first component of aux to signal that it
                   alloc(locaux+k-1) = NEEDS_TO_BE_SET ! needs val, wasnt copied from other grids
                end do
                
                call system_clock(clock_start,clock_rate)
                call cpu_time(cpu_start)
                call setaux(nghost,nx,corn1,hx,
     &                    naux,alloc(locaux))
                call system_clock(clock_finish,clock_rate)
                call cpu_time(cpu_finish)
                timeSetaux = timeSetaux + clock_finish - clock_start
                timeSetauxCPU = timeSetauxCPU + cpu_finish - cpu_start
              else 
                locaux = 1
              endif
              node(storeaux,mptr) = locaux
              if (level .lt. mxnest) then
                loc2              = igetsp(mitot*nvar)
                node(store2,mptr) = loc2
              endif
              rnode(timemult, mptr) = start_time
              go to 30
 20       continue
c
c  if 2nd time through, put initial values in store2 so finer grids
c  can be advanced with interpolation of their boundary values.
c  new time soln should still be in location store1.
c
          loc     = node(store2,mptr)
          locaux  = node(storeaux,mptr)
c
   30     continue
          call qinit(nvar,nghost,nx,corn1,hx,
     &               alloc(loc),naux,alloc(locaux))

c
          mptr  = node(levelptr, mptr)
      if (mptr .ne. 0) go to 10
c
c
 99   continue
      return
      end
