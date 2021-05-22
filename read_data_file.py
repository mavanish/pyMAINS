# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:25:48 2020

@author: Avanish @ pyMAINS
"""

import pandas as pd
from collections import Counter
import numpy as np

#Following version reads data file with 23 Million atoms in 1m23s
A2=[]
with open('Cu-Fe.lmp', 'r') as file2:
    for line in file2:
        A2.append(line.split())    
B2=A2[16:]
C2=A2[:16]

df2=pd.DataFrame(B2,columns=['id','type','x','y','z'],dtype=float)

# Do your magic here

# cu=df[df.type==1.0].index
# df.loc[cu,'avani']=2.0

# fe=df[df.type==2.0].index
# df.loc[fe,'avani']=1.0

# cc=df.avani.value_counts()
# cc.shape[0]
# C=C2

with open('filename.dat', 'w') as f:
    f.write('#Data file created or converted using pyMAINS\n')
    f.write('\n')
    f.write('  {} atoms\n'.format(str(C[2][0])))
    f.write('\t {} atom types\n'.format(str(cc.shape[0])))
    f.write('{} {} xlo xhi\n'.format(str(C[5][0]),str(C[5][1])))
    f.write('{} {} ylo yhi\n'.format(str(C[6][0]),str(C[6][1])))
    f.write('{} {} zlo zhi\n'.format(str(C[7][0]),str(C[7][1])))
    f.write('\n')
    f.write('Masses\n')
    f.write('\n')
    f.write('        1   55.84500000    # Fe\n')
    f.write('        2   63.54600000    # Cu\n')
    f.write('\n')
    f.write('Atoms\n')
    f.write('\n')
df.to_csv('filename.dat',sep=' ',float_format=None,columns=['id','avani','x','y','z'],index=False,header=False,mode='a')
   