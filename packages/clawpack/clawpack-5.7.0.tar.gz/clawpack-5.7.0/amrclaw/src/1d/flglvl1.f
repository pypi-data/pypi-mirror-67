c
c -----------------------------------------------------------
c
      subroutine flglvl1(nvar,naux,lcheck,nxpts,index,lbase,npts,
     &                   start_time)
c
      use amr_module
      implicit double precision (a-h,o-z)
      integer clock_start, clock_finish, clock_rate
c
c :::::::::::::::::::: FLGLVL :::::::::::::::::::::::::::::::::
c
c flglvl = controls the error estimation/flagging bad pts. for
c          an entire level of grids.  returns pointer into alloc
c          where the (x) coordinations of the flagged pts. are.
c input parameters:
c           lcheck = level to be flagged
c output parameters:
c           nxpts = no. of flagged pts. total
c           index  = starting index in alloc of the flagged pts.
c                    (which occupy 1*nxpts locations).
c
c ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
c
c
      nxpts = 0
      numbad = 0


c     flag arrays- based on either spatial gradients (and/or user defined
c                  criteria),  or Richardson error estimation,
c                  or user-defined regions
    
      call system_clock(clock_start,clock_rate)
      call flagger(nvar,naux,lcheck,start_time)
      call system_clock(clock_finish,clock_rate)
      timeFlagger = timeFlagger + clock_finish - clock_start


c     buffer the flagged cells (done for each grid patch of flags)
c     also project flags from finer levels onto this level to ensure
c     proper nesting. Finally compute proper domain for each patch
      call system_clock(clock_start,clock_rate)
      call bufnst1(nvar,naux,numbad,lcheck,lbase)
      call system_clock(clock_finish,clock_rate)
      timeBufnst = timeBufnst + clock_finish - clock_start


      nxpts = nxpts + numbad
c
c  colate flagged pts into flagged points array
c  new version needs to check for proper nesting at this point
c  also needs to sort,  so can remove duplicates.
c
      if (nxpts .gt. 0) then
c        build domain flags for each grid at level lcheck, instead of
c        previous approach using domain flags over entire  domain
c         call domgrid(lbase,lcheck)   ! will need since there are flagged pts  NOW IN BUFNST2
c
c in new version, there are bad cells but nxpts isnt true count any longer
c since there are duplicates, and proper nesting not yet checked
           index = igetsp(nxpts)
           call colate1(alloc(index),nxpts,lcheck,npts,lbase)
      else
         npts = 0  !npts is number of unique flagged points after removing duplicates
         call freeFlags(lcheck)   ! otherwise storage freed in colate1. perhaps always do it here
      endif

      return
      end
c
c ---------------------------------------------------------------------------------
c
       subroutine freeFlags(lcheck)

       use amr_module
       implicit double precision (a-h, o-z)

       mptr = lstart(lcheck)
 10          continue
             locamrflags = node(storeflags,mptr)
             locdomflags = node(domflags_base,mptr)
             locdom2 = node(domflags2,mptr)

             nx     = node(ndihi,mptr) - node(ndilo,mptr) + 1
             mbuff = max(nghost,ibuff+1)
             mibuff = nx + 2*mbuff

             ibytesPerDP = 8
             nwords = (mibuff)/ibytesPerDP+1
             call reclam(locdomflags, nwords)
             call reclam(locdom2, nwords)
             call reclam(locamrflags,mibuff)

        mptr = node(levelptr, mptr)
        if (mptr .ne. 0) go to 10

       return
       end
