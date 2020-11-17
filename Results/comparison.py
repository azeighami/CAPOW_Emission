# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:18:52 2020

@author: mzeigha
"""


from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scenarios = ['all_tax','CO2','no_tax','SNP']
seasons = ['Spring' , 'Summer' , 'Fall' , 'Winter']

index = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
for s in range (4):
    for ss in range (4):
        index[i] = seasons[s]+"_"+scenarios[ss]
        i=i+1


for s in scenarios:
    filename = s + '/CA0/co2_damages.csv'
    df_data = pd.read_csv(filename,header=0,index_col=0)
    
    idx = scenarios.index(s)
    
    if idx < 1:
        A = df_data.iloc[:,0]
    else:
        B = df_data.iloc[:,0]
        A = np.column_stack((A,B))
 


Winter = np.zeros((91,4)) 
Spring = A[59:150,:]
Summer = A[150:241,:]
Fall = A[241:332,:]
Winter[0:32,:] = A[332:,:]
Winter[32:,:] = A[0:59,:]
ss= np.column_stack((Spring,Summer,Fall,Winter))

# for s in range (4):
#     plt.figure()        
#     plt.plot(Spring[:,s])
#     plt.plot(Summer[:,s])
#     plt.plot(Fall[:,s])
#     plt.plot(Winter[:,s])
#     plt.legend(seasons,loc=4)
#     plt.title('CO2 Damages ($) '+ scenarios[s])
#     plt.ylabel('Damages ($)')
#     plt.xlabel('Day of the Year')
#     plt.savefig('fig'+str(s+1)+'.png',dpi=500)

    
plt.figure()      
plt.boxplot(ss)   
plt.title('CO2 Damages ($) ')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], index , rotation=90)
plt.ylabel('CO2 Damages ($)')
plt.savefig('fig5.png', bbox_inches= "tight" , dpi=500)

plt.figure()
M = np.mean(ss,axis=0)          
plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],M)
plt.title('CO2 Damages ($)')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], index , rotation=90)
plt.ylabel('CO2 Damages ($)')
plt.savefig('fig6.png',bbox_inches= "tight",dpi=500)

#########################################################################


for s in scenarios:
    filename = s + '/CA0/snp_damages.csv'
    df_data = pd.read_csv(filename,header=0,index_col=0)
    
    idx = scenarios.index(s)
    
    if idx < 1:
        C = df_data.iloc[:,0]
    else:
        D = df_data.iloc[:,0]
        C = np.column_stack((C,D))
        
Winter2 = np.zeros((91,4)) 
Spring2 = C[59:150,:]
Summer2 = C[150:241,:]
Fall2 = C[241:332,:]
Winter2[0:32,:] = C[332:,:]
Winter2[32:,:] = C[0:59,:]
zz = np.column_stack((Spring2,Summer2,Fall2,Winter2))        

for s in range (4):
    plt.figure()        
    plt.plot(Spring[:,s])
    plt.plot(Summer[:,s])
    plt.plot(Fall[:,s])
    plt.plot(Winter[:,s])
    plt.legend(seasons,loc=4)
    plt.title('Local Air Damages ($) '+ scenarios[s])
    plt.ylabel('Local Damages ($)')
    plt.xlabel('Day of the Year')
    plt.savefig('fig'+str(s+7)+'.png',dpi=500)

    
plt.figure()      
plt.boxplot(zz)   
plt.title('Local Air Damages ($) ')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], index , rotation=90)
plt.ylabel('Local Damages ($)')
plt.savefig('fig11.png',bbox_inches= "tight", dpi=500)

plt.figure()
M = np.mean(zz,axis=0)          
plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],M)
plt.title('Local Air Damages ($)')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], index , rotation=90)
plt.ylabel('Local Damages ($)')
plt.savefig('fig12.png',bbox_inches= "tight", dpi=500)
#########################################################################

spr = Spring+Spring2
summ = Summer + Summer2
fa = Fall+Fall2
win=Winter+Winter2

for s in range (4):
    plt.figure()        
    plt.plot(spr[:,s])
    plt.plot(summ[:,s])
    plt.plot(fa[:,s])
    plt.plot(win[:,s])
    plt.legend(seasons,loc=4)
    plt.title('Total Air Damages ($) '+ scenarios[s])
    plt.ylabel('Local Damages ($)')
    plt.xlabel('Day of the Year')
    plt.savefig('fig'+str(s+13)+'.png',dpi=500)


xx=ss+zz
plt.figure()      
plt.boxplot(xx)   
plt.title('Total Air Damages ($)')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], index , rotation=90)
plt.ylabel('Total Damages ($)')
plt.savefig('fig17.png',bbox_inches= "tight", dpi=500)

plt.figure()
M = np.mean(xx,axis=0)          
plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],M)
plt.title('Total Air Damages ($)')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], index , rotation=90)
plt.ylabel('Total Damages ($)')
plt.savefig('fig18.png',bbox_inches= "tight", dpi=500)
   
    