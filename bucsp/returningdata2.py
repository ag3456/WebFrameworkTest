import numpy as np   # gives Matlab-like N-dimensional array functionality
import os
import h5py  # read/write HDF5 files
from datetime import datetime
from typing import List, Tuple  # typing is the Python type hinting module

fileapi = '/Data/Array Layout/Array with kinst=32 and mdtyp=115 and pl=0.00048 /2D Parameters/ne'
def returningdata2(filename, fileapi,
				 rnglim: Tuple[float, float]=None, 
				 tlim: Tuple[datetime, datetime]=None):


#filename = '/Users/ashakigumbs/Documents/Research_Semeter_Group/madmatlab/Zenith+single-pulse+basic+parameters.hdf5'


     with h5py.File(filename, 'r') as f:  
        rng = f['/Data/Array Layout/Array with kinst=32 and mdtyp=115 and pl=0.00048 /range'][:]
        tut = f['/Data/Array Layout/Array with kinst=32 and mdtyp=115 and pl=0.00048 /timestamps'][:]
        data = f[fileapi][:]
        newtime = [datetime.utcfromtimestamp(t) for t in tut]
        

     if rnglim is None and tlim is None:
          return newtime, rng, data

t,rng,data = returningdata2('/home/ashaki/Downloads/mlh170821i.004.hdf5', fileapi)