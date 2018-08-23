import numpy as np   
import os
import h5py
from datetime import datetime
from typing import List, Tuple
from pathlib import Path

group = '/Data/Array Layout/Array with kinst=32 and mdtyp=115 and pl=0.00048 /2D Parameters'
groupsplit = group.rsplit("/" , 1)[0]
dataset = 'ne'
field = group + '/' + dataset

#fileapi = '/Data/Array Layout/Array with kinst=32 and mdtyp=115 and pl=0.00048 /2D Parameters/ne'
def returningdata2(filename: Path, fileapi,
				   rnglim: Tuple[float, float]=None, 
				   tlim: Tuple[datetime, datetime]=None):

    filename = Path(filename).expanduser()

#filename = '/Users/ashakigumbs/Documents/Research_Semeter_Group/madmatlab/Zenith+single-pulse+basic+parameters.hdf5'

     
    with h5py.File(filename, 'r') as f: 
        tandrng = fileapi.rsplit("/", 2)[0]
        rng = f[tandrng + '/range'][:]
        tut = f[tandrng + '/timestamps'][:]
        data = f[fileapi][:]
        newtime = [datetime.utcfromtimestamp(t) for t in tut]
        

    if rnglim is None and tlim is None:
        return newtime, rng, data

newtime, rng, data = returningdata2('~/Downloads/mlh170821i.004.hdf5', field)
