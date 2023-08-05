c
c ---------------------------------------------------------
c
      subroutine grdfit (lbase,lcheck,nvar,naux,cut,time,
     1                   start_time)
c
      use amr_module
      implicit double precision (a-h,o-z)
      integer clock_start, clock_finish, clock_rate
      integer clock_start1
c
      dimension  corner(nsize,maxcl)
      integer    numptc(maxcl), prvptr
      logical    cout
      logical    fit1, nestck1
      data       cout/.false./
c
c ::::::::::::::::::::: GRDFIT :::::::::::::::::::::::::::::::::;
c  grdfit called by setgrd and regrid to actually fit the new grids
c         on each level. lcheck is the level being error estimated
c         so that lcheck+1 will be the level of the new grids.
c ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;
c

      call system_clock(clock_start,clock_rate)


c ### initialize region start and end indices for new level grids
      iregst(lcheck+1) = iinfinity
      iregend(lcheck+1) = -1

c     ## flag all grids at given level based on error ests.
c     ## npts is number of points actually colated - some
c     ## flagged points turned off due to proper nesting requirement.
c     ## (storage based on nptmax calculation however).

      call system_clock(clock_start1,clock_rate)
      call flglvl1(nvar,naux,lcheck,nptmax,index,lbase,npts,start_time)
      call system_clock(clock_finish,clock_rate)
      timeFlglvl = timeFlglvl + clock_finish - clock_start1

      if (npts .eq. 0) go to 99
c
      levnew    = lcheck + 1
      hxfine    = hxposs(levnew)
c
c     ## call smart_bisect grid gen. to make the clusters
c        till each cluster ok. needs scratch space.
c
       idim = iregsz(lcheck)
c       lociscr = igetsp(idim+jdim)

       call smartbis(alloc(index),npts,cut,numptc,nclust,lbase,
     2               corner,idim)
c     2               corner,alloc(lociscr),alloc(locjscr),idim,jdim)
c       call reclam(lociscr,idim+jdim)

       if (gprint) then
          write(outunit,103) nclust
          write(outunit,104) (icl, numptc(icl),icl=1,nclust)
 103      format(' ',i4,' clusters after bisect')
 104      format('         cluster ',i5,' has points: ',i8)
       endif
c
c     ##  for each cluster, fit the actual grid, set up some data structures
c
 50   ibase   =  0
      icl     =  1
      prvptr  =  null
c
 70   mnew      = nodget()
c       if (lcheck .eq. 2 .and. (mnew .ne. 6 .and. mnew .ne. 7)) go to 69 
c       if (lcheck .eq. 1 .and. (mnew .ne. 3 .and. mnew .ne. 2 )) go to 69 
 75   call  moment(node(1,mnew),alloc(index+1*ibase),numptc(icl),usage)

      if (gprint) write(outunit,100) icl,mnew,usage,numptc(icl)
100   format('         cluster ',i5,' new rect.',i5,
     1       ' usage ',e12.5,' with ',i5,' pts.')

      node(ndilo,mnew) = node(ndilo,mnew)*intratx(lcheck)
      node(ndihi,mnew) = (node(ndihi,mnew)+1)*intratx(lcheck) - 1
      rnode(cornxlo,mnew)  = node(ndilo,mnew)*hxfine + xlower
      rnode(cornxhi,mnew)  = (node(ndihi,mnew)+1)*hxfine + xlower
      node(nestlevel,mnew)     = levnew
      rnode(timemult,mnew)   = time

      if (gprint) write(outunit,101) (node(i,mnew),i=1,nsize),
     &                              (rnode(i,mnew),i=1,rsize)
 101  format(4i5,4i15,/,2i15,5i15,/,2i15,/,3e15.7)
c
c     ##  if new grid doesn't fit in base grid, nestck bisect it
c     ##  and returns 2 clusters where there used to be 1.
c
c 2/28/02 : Added naux to argument list; needed by call to outtre in nestck

      fit1= nestck1(mnew,lbase,alloc(index+ibase),numptc(icl),numptc,
     1             icl,nclust,nvar, naux)
      if (.not. fit1) go to 75
c
c     ##  grid accepted. put in list.
      if (newstl(levnew) .eq. null) then
          newstl(levnew)  = mnew
      else
          node(levelptr,prvptr) = mnew
      endif
      prvptr = mnew
c     # keep track of min and max location of grids at this level
      iregst(levnew)  = MIN(iregst(levnew), node(ndilo,mnew))
      iregend(levnew) = MAX(iregend(levnew),node(ndihi,mnew))

c     ##  on to next cluster
 69     ibase  = ibase + numptc(icl)
      icl = icl + 1
      if (icl .le. nclust) go to 70
c
c    ##  clean up. for all grids check final size.
      call birect(newstl(levnew))

 99   continue
c    ## may have npts 0 but array was allocated due to initially flagged points
c    ## that were not allowed for proper nesting or other reasons. in this case
c    ## the array was still allocated, so need to test further to see if colating
c    ## array space needs to be reclaimed
      if (nptmax .gt. 0) call reclam(index, nptmax)
c
      call system_clock(clock_finish,clock_rate)
      timeGrdfitAll = timeGrdfitAll + clock_finish - clock_start

      return
      end

