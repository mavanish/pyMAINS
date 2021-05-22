# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:07:17 2020

@author: Avanish @ pyMAINS
"""


import pandas as pd
from collections import Counter
import numpy as np
import os

for i in range(21):
#    print ('dump.tensile.{}'.format(i*1000))

    A=[]
    with open('dump.tensile.{}'.format(i*1000), 'r') as file2:
        for line in file2:
            A.append(line.split())
    B=A[9:]
    C=A[:9]
    
    df=pd.DataFrame(B,columns=A[8][2:],dtype=float)
    
    fe=df[df.type==1].index
    cu=df[df.type==2].index
    
    df.type=df.type.astype(int)
    df.id=df.id.astype(int)
    
    dffe=df.loc[fe].reset_index(drop=True)
    
    dfcu=df.loc[cu].reset_index(drop=True)
    dfcu['type'].replace(2,1, inplace=True)
    
    
    cc=df.type.value_counts()
    cc.shape[0]
    
    os.makedirs('./{}ps/CuFe'.format(i)) 
        
    with open('{}ps/CuFe/CuFe-{}ps.dat'.format(i,i), 'w') as f:
        f.write('#Data file created or converted using pyMAINS\n')
        f.write('\n')
        f.write('  {} atoms\n'.format(str(C[3][0])))
        f.write('\t {} atom types\n'.format(str(cc.shape[0])))
        f.write('{} {} xlo xhi\n'.format(str(C[5][0]),str(C[5][1])))
        f.write('{} {} ylo yhi\n'.format(str(C[6][0]),str(C[6][1])))
        f.write('{} {} zlo zhi\n'.format(str(C[7][0]),str(C[7][1])))
        f.write('\n')
        f.write('Masses\n')
        f.write('\n')
        f.write('       1   55.84500000    # Fe\n')
        f.write('       2   63.54600000    # Cu\n')
        f.write('\n')
        f.write('Atoms # atomic\n')
        f.write('\n')
    df.to_csv('{}ps/CuFe/CuFe-{}ps.dat'.format(i,i),sep=' ',float_format=None,columns=['id','type','x','y','z'],index=False,header=False,mode='a')
    
    
    os.makedirs('./{}ps/Fe'.format(i)) 
     
       
    with open('{}ps/Fe/Fe-{}ps.dat'.format(i,i), 'w') as f:
        f.write('#Data file created or converted using pyMAINS\n')
        f.write('\n')
        f.write('  {} atoms\n'.format(str(dffe.shape[0])))
        f.write('\t 1 atom types\n')
        f.write('{} {} xlo xhi\n'.format(str(C[5][0]),str(C[5][1])))
        f.write('{} {} ylo yhi\n'.format(str(C[6][0]),str(C[6][1])))
        f.write('{} {} zlo zhi\n'.format(str(C[7][0]),str(C[7][1])))
        f.write('\n')
        f.write('Masses\n')
        f.write('\n')
        f.write('        1   55.84500000    # Fe\n')
        f.write('\n')
        f.write('Atoms # atomic\n')
        f.write('\n')
    dffe.to_csv('{}ps/Fe/Fe-{}ps.dat'.format(i,i),sep=' ',float_format=None,columns=['id','type','x','y','z'],index=False,header=False,mode='a')
    
    os.makedirs('./{}ps/Cu'.format(i)) 
            
    with open('{}ps/Cu/Cu-{}ps.dat'.format(i,i), 'w') as f:
        f.write('#Data file created or converted using pyMAINS\n')
        f.write('\n')
        f.write('  {} atoms\n'.format(str(dfcu.shape[0])))
        f.write('\t 1 atom types\n')
        f.write('{} {} xlo xhi\n'.format(str(C[5][0]),str(C[5][1])))
        f.write('{} {} ylo yhi\n'.format(str(C[6][0]),str(C[6][1])))
        f.write('{} {} zlo zhi\n'.format(str(C[7][0]),str(C[7][1])))
        f.write('\n')
        f.write('Masses\n')
        f.write('\n')
        f.write('        1   63.54600000    # Cu\n')
        f.write('\n')
        f.write('Atoms # atomic\n')
        f.write('\n')
    dfcu.to_csv('{}ps/Cu/Cu-{}ps.dat'.format(i,i),sep=' ',float_format=None,columns=['id','type','x','y','z'],index=False,header=False,mode='a')
          
    
