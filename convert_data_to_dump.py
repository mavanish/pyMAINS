# -*- coding: utf-8 -*-
"""
Created on Wed May 12:25:48 2021

@author: Avanish @ pyMAINS

data  -> dump

data -> data 
"""
import pandas as pd
from collections import Counter
import numpy as np
import os

'''
For reading data files with header as follows 

Example:
----
#Data file created or converted using pyMAINS

  4000 atoms
	 2 atom types
0.00000000 36.14900000 xlo xhi
0.00000000 36.14900000 ylo yhi
0.00000000 36.14900000 zlo zhi

Masses

        1   55.84500000    # Fe
        2   63.54600000    # Cu

Atoms

1.0 2.0 0.0 0.0 0.0

------

'''
ntime=0
filename='file.dat'

with open(filename) as myfile:
    head = [next(myfile) for x in range(16)]

ind=head.index('Atoms\n')

natom=int(float(head[2].split()[0]))
ntype=int(float(head[3].split()[0]))

xmin,xmax,a,b= [i for i in head[4].split()]
ymin,ymax,a,b= [i for i in head[5].split()]
zmin,zmax,a,b= [i for i in head[6].split()]

xmin,xmax=float(xmin),float(xmax)
ymin,ymax=float(ymin),float(ymax)
zmin,zmax=float(zmin),float(zmax)

df=pd.read_csv(filename,sep='\s+',header=None,skiprows=ind+2) 
df.columns=['id','type','x','y','z']
df.id=df.id.astype(int)
df.type=df.type.astype(int)

subs = 'Mass'
res = [j for j in head if subs in j]

m=[]
t=[]

if len(res)!=0:
    ifmass=head.index(res[0])
    print('Mass is provided for %d system' % ntype)
    for i in range(ifmass+2,ind-1):
        t.append(head[i].split()[0])
        m.append(head[i].split()[1])

else:
    print('Mass is not defnied in the data file')




'''
Writing dump file
'''
with open('filename.dump', 'w') as f:
    f.write('ITEM: TIMESTEP\n')
    f.write('{}\n'.format(str(int(float(ntime)))))
    f.write('ITEM: NUMBER OF ATOMS\n')
    f.write('{}\n'.format(str(natom)))
    f.write('ITEM: BOX BOUNDS pp pp pp\n')
    f.write('{} {}\n'.format(str(xmin),str(xmax)))
    f.write('{} {}\n'.format(str(ymin),str(ymax)))
    f.write('{} {}\n'.format(str(zmin),str(zmax)))
    f.write('ITEM: ATOMS id type x y z\n')  #Chnage the column name here if needed          
df.to_csv('filename.dump',sep='\t',float_format=None,index=False,header=False,mode='a')
f.close()


'''
Define mass and type if you want. Do not change the varaible name as given below for that t and m.

Coz if condition is used for writing masses 

For example

m=[55.35,61.68]
t=[1,2]

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
    if len(res)!=0:
        f.write('Masses\n')
        f.write('\n')
        for k in range(len(m)):
            f.write('        {}   {}    # A{} \n'.format(str(t[k]),str(m[k]),str(k)))
        f.write('\n')
    f.write('Atoms\n')
    f.write('\n')
df.to_csv('filename.dat',sep='\t',float_format=None,columns=['id','type','x','y','z'],index=False,header=False,mode='a')
      
    