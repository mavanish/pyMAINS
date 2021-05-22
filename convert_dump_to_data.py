# -*- coding: utf-8 -*-
"""
Created on Wed May 12:25:48 2021

@author: Avanish @ pyMAINS
"""
import pandas as pd
from collections import Counter
import numpy as np
import os

'''
For reading dump files with header as follows 
----
ITEM: TIMESTEP
1000
ITEM: NUMBER OF ATOMS
28654560
ITEM: BOX BOUNDS pp pp pp
0 334.626 
0 339.032
266.978 3279.17
ITEM: ATOMS id type x y z vx vy vz c_2[1] c_2[2] c_2[3] c_3 c_4 
6555 1 49.8856 1.47846 269.395 -4.62697 -2.8043 10.9163 885723 -3.44425e+06 -1.72503e+06 21.6796 5 
------

Line 39 (read_csv) we skip 9 lines while reading through pandas as these are header
'''
filename='lammps_file.dump'

with open(filename) as myfile:
    head = [next(myfile) for x in range(9)]
ntime=int(float(head[1].split()[0]))
natom=int(float(head[3].split()[0]))
xmin,xmax= [float(i) for i in head[5].split()]
ymin,ymax= [float(i) for i in head[6].split()]
zmin,zmax= [float(i) for i in head[7].split()]

df=pd.read_csv(filename,sep='\s+',header=None,skiprows=9) #9 rows skipped based on the lammps dump file please confirm for your case
df.columns=head[8].split()[2:]

'''
Define mass and type if you want. Do not change the varaible name as given below for that t and m.

Coz if condition is used for writing masses 

For example

m=[55.35,61.68]
t=[1,2]

Must define ntype, type of atoms in the dump file, 
possible ways 
          if atom type is column in dump file
            ntype=df.type.value_counts().shape[0]
          if manually input t array
            ntype=len(t)
          or just define ntype below
            ntype=2 # kept default 1
------

'''
m=[]
t=[]
ntype=1 #see comment above from line 52-59

'''
Writing data file 
'''    
with open('filename.dat', 'w') as f:
    f.write('#Data file created or converted using pyMAINS\n')
    f.write('\n')
    f.write('  {} atoms\n'.format(str(natom)))
    f.write('\t {} atom types\n'.format(str(ntype)))
    f.write('{} {} xlo xhi\n'.format(str(xmin),str(xmax)))
    f.write('{} {} ylo yhi\n'.format(str(ymin),str(ymax)))
    f.write('{} {} zlo zhi\n'.format(str(zmin),str(zmax)))
    f.write('\n')
    if len(m)!=0:
        f.write('Masses\n')
        f.write('\n')
        for k in range(len(m)):
            f.write('        {}   {}    # A{} \n'.format(str(t[k]),str(m[k]),str(k)))
        f.write('\n')
    f.write('Atoms\n')
    f.write('\n')
df.to_csv('filename.dat',sep='\t',float_format=None,columns=['id','type','x','y','z'],index=False,header=False,mode='a')
      