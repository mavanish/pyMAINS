# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:31:06 2020

@author: avanish from pyMAINS
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

A=[]
D=[]
with open('log.lammps', 'r') as file2:
    for i, line in enumerate(file2,1):
        A.append(line.split())
        if line.startswith("Step"):
            st_line=i
            print(i)
#            D.append(line.split())  
        if line.startswith("run"):
            add_line=int(line.split()[1])
#            D.append(line.split()) 
        if line.startswith("thermo "):
            thermo=int(line.split()[1])
            
end_line=(add_line/thermo)+st_line
B=A[st_line:int(end_line+1)]

df=pd.DataFrame(B,columns=A[st_line-1],dtype=float)

print(df.Temp[-101:].mean(),df.Temp[-101:].mean())




plt.plot()
