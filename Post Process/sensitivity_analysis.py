# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 14:45:53 2021

@author: mzeigha
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SALib.analyze import sobol
from SALib.analyze import dgsm
from SALib.analyze import ff
from SALib.analyze import delta
#This section is for the sensitivity test

#Define Variables

scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
stochastic_column = ['CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']
column_name = ['SNP_Damage', 'Shadow_Price','CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']


#### Reading the "Daily results" of simulation 
stochastic_df = pd.read_csv('Results/Stochastic_df.csv')
CO2_damage_df = pd.read_csv('Results/CO2_damage.csv')
SNP_damage_df = pd.read_csv('Results/SNP_damage.csv')
Shadow_price_df = pd.read_csv('Results/Shadow_price.csv')


"""
x1 load
x2 Hydro CA
x3 Path 66
x4 Wind
x5 Solar

Y local air damages

"""
##

### thay have to be rearrange to 500*365 dataframes 

Shadow_Price = np.array(Shadow_price_df ['SNP']).reshape((500,365))
Hydro_CA = np.array(stochastic_df['CA_Hydropower']).reshape((500,365))
Hydro_PNW = np.array(stochastic_df['PNW_Hydropower']).reshape((500,365))
Wind = np.array(stochastic_df['CA_Wind_Power']).reshape((500,365))
Solar = np.array(stochastic_df['Solar_Power']).reshape((500,365))
CA_load = np.array(stochastic_df['CA_load']).reshape((500,365))


# #D is the number of varibles in this case is 5
# #N is Y,size/D+2
# #N=500/7

D=5
N=71

Y = np.array(SNP_damage_df['SNP']).reshape((500,365))


Y_var = np.zeros(363)

for i in range(0,363):
    Y_var[i]=np.var(Y[0:i])
    
    
S1=np.zeros((363,5))
S2=np.zeros((363,5))
S3=np.zeros((363,5))
St=np.zeros((363,5))

S_cal=np.zeros((363,5))
S=np.zeros((363,D))
for i in range(0,363):
    x5=CA_load[:,i]
    x1=Hydro_CA[:,i]
    x2=Hydro_PNW[:,i]
    x3=Wind[:,i]
    x4=Solar[:,i]
    
    X=np.zeros((500,6))
    X[:,0]=x1
    X[:,1]=x2
    X[:,2]=x3
    X[:,3]=x4
    X[:,4]=x5
    X[:,5]=Y[:,i]
    
#    A, B, AB, BA = separate_output_values(Y[:1197,i], D, N, calc_second_order=False)
#    for k in range(0,5):
#        V=X[:,k]
#        hist,bins=np.histogram(V,bins=40)
#        E=np.zeros(39)
#        S[i,k] = total_order(A, AB[:, k], B)/Y_var[i]
#        for j in range(0,39):
#            Temp=X[X[:,k]>=bins[j]]
#            Temp=Temp[Temp[:,k]<=bins[j+1]]
#            E[j]=np.mean(Temp[:,5])
#        S_cal[i,k]=np.nanvar(E)/Y_var[i]
#    
#     
    problem = {
        'num_vars': 5,
        'names': ['x1', 'x2', 'x3','x4','x5'],
        'bounds': [[np.min(x1), np.max(x1)],
                    [np.min(x2), np.max(x2)],
                    [np.min(x3), np.max(x3)],
                    [np.min(x4), np.max(x4)],
                    [np.min(x5), np.max(x5)]]
    }
#    Si = sobol.analyze(problem, Y[:,i]*24)
    

#    Si2=dgsm.analyze(problem,X,Y[:,i]*24,print_to_console=True)
#    S1[i,:]=Si['S1']
#    St[i,:]=Si['ST']
    
    S_delta=delta.analyze(problem,X,Y[:,i]*24,print_to_console=False)
    S3[i,:]=S_delta['delta']
#    for j in range(0,4):
#        S2[i,j]=Si['S2'][0,j+1]

       
plt.figure()
plt.stackplot(range(0,363),S3[:,0],S3[:,1],S3[:,2],S3[:,3],S3[:,4],alpha=0.7)    


S_scaled= np.array([Y_var[i] *S3[i,:] for i in range(363)])
S_scaled_rest=Y_var-np.sum(S_scaled,axis=1)
S3_rest=1-np.sum(S3,axis=1)

plt.figure()
plt.style.use('seaborn-paper')
plt.stackplot(range(0,363),S_scaled[:,0],S_scaled[:,2],S_scaled[:,1],S_scaled[:,3],S_scaled[:,4],S_scaled_rest,colors=['red','g','b','c','orange','k'])
lw=10
plt.plot([],[],color='red', label='CA Hydro', linewidth=lw)

plt.plot([],[],color='b', label='PNW Hydro', linewidth=lw)
plt.plot([],[],color='g', label='Wind', linewidth=lw)
plt.plot([],[],color='c', label='Solar', linewidth=lw)
plt.plot([],[],color='orange', label='CA_load', linewidth=lw)

plt.plot([],[],color='black', label='Interactive', linewidth=lw)
plt.box(on=False)
plt.legend(loc='upper center', bbox_to_anchor=(0.55, 1),ncol=8, fancybox=True, shadow=True,fontsize='xx-large')


plt.figure()
plt.stackplot(range(0,363),S3[:,0],S3[:,2],S3[:,1],S3[:,3],S3[:,4],S3_rest,colors=['red','g','b','c','orange','k'],alpha=1)