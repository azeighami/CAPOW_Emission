# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scenarios = ['all_tax','co2_tax','no_tax','snp_tax']

for s in scenarios:
    filename = s + '/co2_damages.csv'
    df_data = pd.read_csv(filename,header=0,index_col=0)
    
    idx = scenarios.index(s)
    
    if idx < 1:
        A = df_data.iloc[:,0]
    else:
        B = df_data.iloc[:,0]
        A = np.column_stack((A,B))

plt.figure()        
plt.plot(A)
plt.legend(scenarios)
plt.title('CO2 Damages ($)')
plt.ylabel('Damages ($)')
plt.xlabel('Day of the Year')
plt.savefig('fig1.png',dpi=500)

plt.figure()      
plt.boxplot(A)
plt.title('CO2 Damages ($)')
plt.xticks([1,2,3,4],scenarios)
plt.ylabel('CO2 Damages ($)')
plt.savefig('fig2.png',dpi=500)

plt.figure()
M = np.mean(A,axis=0)      
plt.bar([0,1,2,3],M)
plt.title('CO2 Damages ($)')
plt.xticks([0,1,2,3],scenarios)
plt.ylabel('CO2 Damages ($)')
plt.savefig('fig3.png',dpi=500)


for s in scenarios:
    filename = s + '/snp_damages.csv'
    df_data = pd.read_csv(filename,header=0,index_col=0)
    
    idx = scenarios.index(s)
    
    if idx < 1:
        C = df_data.iloc[:,0]
    else:
        D = df_data.iloc[:,0]
        C = np.column_stack((C,D))

plt.figure()        
plt.plot(C)
plt.legend(scenarios)
plt.title('Local Air Damages ($)')
plt.ylabel('Local Damages ($)')
plt.xlabel('Day of the Year')
plt.savefig('fig4.png',dpi=500)

plt.figure()      
plt.boxplot(C)
plt.title('Local Air Damages ($)')
plt.xticks([1,2,3,4],scenarios)
plt.ylabel('Local Damages ($)')
plt.savefig('fig5.png',dpi=500)

plt.figure()
M = np.mean(C,axis=0)      
plt.bar([0,1,2,3],M)
plt.title('Local Air Damages ($)')
plt.xticks([0,1,2,3],scenarios)
plt.ylabel('Local Damages ($)')
plt.savefig('fig6.png',dpi=500)

E = A + C
plt.figure()        
plt.plot(E)
plt.legend(scenarios)
plt.title('Total Air Damages ($)')
plt.ylabel('Damages ($)')
plt.xlabel('Day of the Year')
plt.savefig('fig7.png',dpi=500)

plt.figure()      
plt.boxplot(E)
plt.title('Total Air Damages ($)')
plt.xticks([1,2,3,4],scenarios)
plt.ylabel('Total Damages ($)')
plt.savefig('fig8.png',dpi=500)

plt.figure()
M = np.mean(E,axis=0)      
plt.bar([0,1,2,3],M)
plt.title('Total Air Damages ($)')
plt.xticks([0,1,2,3],scenarios)
plt.ylabel('Total Damages ($)')
plt.savefig('fig9.png',dpi=500)
    
