#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:51:11 2018
@author: ashaki
"""
import h5py

i = 0
d = {}
groups = []
p = {}
datasets = []
def print_hdf5_file_structure(file_name) :
    """Prints the HDF5 file structure"""
    with h5py.File(file_name, 'r') as f:
        item = f #["/Configure:0000/Run:0000"]
        print_hdf5_item_structure(item)

 
def print_hdf5_item_structure(g, offset='    ') :
    """Prints the input file/group/dataset (g) name and begin iterations on its content"""
    if isinstance(g,h5py.File):
        print (g.file, g.name)
        #x.extend(g.file)
    elif isinstance(g,h5py.Dataset) and not isinstance(g,h5py.Group):
        #, g.dtype
        d['label'] = g.name.rsplit("/", 1)[1]
        d['value'] =g.name.rsplit("/", 1)[1]
        groups.append(d.copy())
    elif isinstance(g,h5py.Group):
        if ("Parameters" in g.name.rsplit("/", 1)[1]):
            p['label'] = g.name.rsplit("/", 2)[1] + "/" + g.name.rsplit("/", 1)[1]
            p['value'] = g.name
            datasets.append(p.copy())
    else:
        raise KeyError('UNKNOWN ITEM IN HDF5 FILE')
 
    if isinstance(g, h5py.File) or isinstance(g, h5py.Group) :
        for key,val in dict(g).items() :
            subg = val
            #print (offset, key) #,"   ", subg.name #, val, subg.len(), type(subg),
            print_hdf5_item_structure(subg, offset + '    ')
            
def return_options(file_name):  #this is done to return the options variable 
    print_hdf5_file_structure(file_name)
    return groups, datasets
 
#if __name__ == "__main__" :
#groups, datasets = return_options('/home/ashaki/Downloads/mlh170821i.004.hdf5')
#    print( "End of test" )
