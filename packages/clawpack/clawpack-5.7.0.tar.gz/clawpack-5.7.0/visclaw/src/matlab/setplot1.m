%  SETPLOT1 sets user defined plotting parameters
%
%      User defined Matlab script for setting various Clawpack plotting
%      parameters.  This script is called by PLOTCLAW1.  A default
%      version of this script can be found in claw/matlab/setplot1.m and
%      copied to users working directory and modifed to set things up
%      differently.
%
%      Parameters that can be set with SETPLOT1
%
%        OutputFlag        - set to 'ascii' (default) to read ascii output
%                                from files fort.qXXXX where XXXX is Frame #
%                            or to 'hdf' to read hdf output files.
%                                from files fort.qXXXX.hdf
%                            set to 'aux' to read aux array values from
%                                fort.aXXXX instead of q from fort.qXXXX
%                                These files are created only if
%                                outaux = .true.  in out2.f
%
%        OutputDir         - set to '.' to read data from current working
%                                directory (default) or set to path
%                                to output directory.
%
%        PlotStyle           - used in plot command for line color and type.
%        mq                  - which component of q to plot
%        UserVariable        - Set to 1 to specify a user defined variable.
%        UserVariableFile    - name of m-file mapping data to q
%        MappedGrid          - set to 1 if mapc2p.m exists for nonuniform
%                              grid
%        MaxFrames           - max number of frames
%
%      All parameters can be modified by typing 'k' at the PLOTCLAW1 prompt.
%
%      See PLOTCLAW1.

mq = 1;                       % which component(s) of q to plot
UserVariable = 0;             % set to 1 to specify a user-defined variable
UserVariableFile = ' ';       % name of m-file mapping data to q
MappedGrid = 0;               % set to 1 if mapc2p.m exists for nonuniform grid
PlotStyle = setplotstyle('b-');  % used in plot command for line color and type
MaxFrames = 1000;                % max number of frames to loop over
