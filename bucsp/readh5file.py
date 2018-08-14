#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:51:11 2018
@author: ashaki
"""
import h5py
import sys

i = 0
d = {}
options = []
def print_hdf5_file_structure(file_name) :
    """Prints the HDF5 file structure"""
    file = h5py.File(file_name, 'r') # open read-only
    item = file #["/Configure:0000/Run:0000"]
    print_hdf5_item_structure(item)
    file.close()
 
def print_hdf5_item_structure(g, offset='    ') :
    """Prints the input file/group/dataset (g) name and begin iterations on its content"""
    if   isinstance(g,h5py.File) :
        print (g.file, g.name)
        #x.extend(g.file)
 
    elif isinstance(g,h5py.Dataset) and not isinstance(g,h5py.Group)  :
        print  (g.name) #, g.dtype
        d['label'] = g.name.rsplit("/", 1)[1]
        d['value'] = g.name
     
        options.append(d.copy())

    elif isinstance(g,h5py.Group):
        print (g.name)
        
    else :
        print ('WARNING: UNKNOWN ITEM IN HDF5 FILE', g.name)
        sys.exit ( "EXECUTION IS TERMINATED" )
 
    if isinstance(g, h5py.File) or isinstance(g, h5py.Group) :
        for key,val in dict(g).items() :
            subg = val
            #print (offset, key) #,"   ", subg.name #, val, subg.len(), type(subg),
            print_hdf5_item_structure(subg, offset + '    ')
            
def return_options(file_name):  #this is done to return the options variable 
    print_hdf5_file_structure(file_name)
    return options
 
#if __name__ == "__main__" :
options = return_options('/home/ashaki/Downloads/mlh170821i.004.hdf5')
#    sys.exit ( "End of test" )