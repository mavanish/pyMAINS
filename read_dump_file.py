# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:25:48 2020

@author: Avanish @ pyMAINS
"""

import pandas as pd
from collections import Counter
import numpy as np

#Following version reads dump file with 23 Million atoms in 1m23s
# A=[]
# with open('lammps_file.dump', 'r') as file:
#     for line in file:
#         A.append(line.split())    
# B=A[9:]
# C=A[:9]
# df=pd.DataFrame(B,columns=A[8][2:],dtype=float)

#Following version reads dump file with 23 Million atoms in 19s, 
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


# Do your magic here

# cu=df[df.type==1.0].index
# df.loc[cu,'avani']=2.0

# fe=df[df.type==2.0].index
# df.loc[fe,'avani']=1.0

# cc=df.avani.value_counts()
# cc.shape[0]
# C=C2

with open('filename.dump', 'w') as f:
    f.write('ITEM: TIMESTEP\n')
    f.write('{}\n'.format(str(int(float(ntime)))))
    f.write('ITEM: NUMBER OF ATOMS\n')
    f.write('{}\n'.format(str(natom)))
    f.write('ITEM: BOX BOUNDS pp pp pp\n')
    f.write('{} {}\n'.format(str(xmin),str(xmax)))
    f.write('{} {}\n'.format(str(ymin),str(ymax)))
    f.write('{} {}\n'.format(str(zmin),str(zmax)))
    f.write('ITEM: ATOMS id type x y z \n')  #Chnage the column name here           
df.to_csv('filename.dump',sep='\t',float_format=None,index=False,header=False,mode='a')
f.close()
