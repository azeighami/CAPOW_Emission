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
scenarios_label = ['All' , 'CO2' , 'No', 'SNP']


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
Path66 = np.array(stochastic_df['Path66_flow']).reshape((500,365))

# #D is the number of varibles in this case is 5
# #N is Y,size/D+2
# #N=500/7

D=5
N=71

# for sen in scenarios:
    
#     Y = np.array(SNP_damage_df[sen]).reshape((500,365))
#     Y_var = np.zeros(363)
    
#     for i in range(0,363):
#         Y_var[i]=np.var(Y[0:i])
         
#     S1=np.zeros((363,5))
#     S2=np.zeros((363,5))
#     S3=np.zeros((363,5))
#     St=np.zeros((363,5))
    
#     S_cal=np.zeros((363,5))
#     S=np.zeros((363,D))
#     for i in range(0,363):
                
#         x1=CA_load[:,i]        
#         x2=Hydro_CA[:,i]
#         x3=Path66[:,i]
#         x4=Wind[:,i]
#         x5=Solar[:,i]
#         labels=['CA Load', 'CA Hydro', 'Imports', 'CA Wind', 'CA Solar']
      
#         X=np.zeros((500,6))
#         X[:,0]=x1
#         X[:,1]=x2
#         X[:,2]=x3
#         X[:,3]=x4
#         X[:,4]=x5
#         X[:,5]=Y[:,i]
        
#         problem = {
#             'num_vars': 5,
#             'names': ['x1', 'x2', 'x3','x4','x5'],
#             'bounds': [[np.min(x1), np.max(x1)],
#                         [np.min(x2), np.max(x2)],
#                         [np.min(x3), np.max(x3)],
#                         [np.min(x4), np.max(x4)],
#                         [np.min(x5), np.max(x5)]]
#         }

#         S_delta=delta.analyze(problem,X,Y[:,i]*24,print_to_console=False)
#         S3[i,:]=S_delta['delta']
    
#     plt.figure()
#     plt.stackplot(range(0,363),S3[:,0],S3[:,1],S3[:,2],S3[:,3],S3[:,4],alpha=0.8 , labels=labels)
#     plt.title('The Sensitivity Analysis of Damages of {} Tax Scenario'.format(scenarios_label[scenarios.index(sen)]))
#     plt.legend(loc='right', bbox_to_anchor=(1.3, 0.5),ncol=1, fancybox=True, shadow=True)
#     plt.savefig('Plots/Sensitivity Analysis {} Tax scenario.png'.format(scenarios_label[scenarios.index(sen)]) , bbox_inches='tight',dpi=250)
       
#     print (sen)

    
# print ('Second')    





for sen in scenarios:
    
    Y = np.array(Shadow_price_df [sen]).reshape((500,365))    
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
                

        x1=CA_load[:,i]        
        x2=Hydro_CA[:,i]
        x3=Path66[:,i]
        x4=Wind[:,i]
        x5=Solar[:,i]
        labels=['CA Load' , 'CA Hydro' ,'Imports' , 'CA Wind', 'CA Solar']
      
        X=np.zeros((500,6))
        X[:,0]=x1
        X[:,1]=x2
        X[:,2]=x3
        X[:,3]=x4
        X[:,4]=x5
        X[:,5]=Y[:,i]
        
        problem = {
            'num_vars': 5,
            'names': ['x1', 'x2', 'x3','x4','x5'],
            'bounds': [[np.min(x1), np.max(x1)],
                        [np.min(x2), np.max(x2)],
                        [np.min(x3), np.max(x3)],
                        [np.min(x4), np.max(x4)],
                        [np.min(x5), np.max(x5)]]
        }

        S_delta=delta.analyze(problem,X,Y[:,i]*24,print_to_console=False)
        S3[i,:]=S_delta['delta']
    
    plt.figure()
    plt.stackplot(range(0,363),S3[:,0],S3[:,1],S3[:,2],S3[:,3],S3[:,4],alpha=0.8 , labels=labels)
    plt.title('The Sensitivity Analysis of Shadow Price, {} Tax Scenario'.format(scenarios_label[scenarios.index(sen)]))
    plt.legend(loc='right', bbox_to_anchor=(1.3, 0.5),ncol=1, fancybox=True, shadow=True)
    plt.savefig('Plots/Sensitivity Analysis of Shadow Price, {} Tax scenario.png'.format(scenarios_label[scenarios.index(sen)]) , bbox_inches='tight',dpi=250)
       
    print (sen)







# for sen in scenarios:
    
#     Y = np.array(SNP_damage_df[sen]).reshape((500,365))
#     Y_var = np.zeros(363)
    
#     for i in range(0,363):
#         Y_var[i]=np.var(Y[0:i])
         
#     S1=np.zeros((363,5))
#     S2=np.zeros((363,5))
#     S3=np.zeros((363,5))
#     St=np.zeros((363,5))
    
#     S_cal=np.zeros((363,5))
#     S=np.zeros((363,D))
#     for i in range(0,363):
                
# ######################## Including Shadow Price in the analysis 
#         x1=Shadow_Price[:,i]
#         x2=Hydro_CA[:,i]
#         x3=Hydro_PNW[:,i]
#         x4=Wind[:,i]        
#         x5=Path66[:,i]
#         labels=['Shadow_Price' ,'CA Hydro' , 'PNW Hydro' , 'CA Wind', 'Imports']
# ####################### Including CA_load in analysis 
#         # x1=CA_load[:,i]        
#         # x2=Hydro_CA[:,i]
#         # x3=Hydro_PNW[:,i]
#         # x4=Wind[:,i]
#         # x5=Path66[:,i]
#         # labels=['CA Load', 'CA Hydro' , 'PNW Hydro' , 'CA Wind', 'CA Solar', 'Imports']
      
#         X=np.zeros((500,6))
#         X[:,0]=x1
#         X[:,1]=x2
#         X[:,2]=x3
#         X[:,3]=x4
#         X[:,4]=x5
#         X[:,5]=Y[:,i]
        
#         problem = {
#             'num_vars': 5,
#             'names': ['x1', 'x2', 'x3','x4','x5'],
#             'bounds': [[np.min(x1), np.max(x1)],
#                         [np.min(x2), np.max(x2)],
#                         [np.min(x3), np.max(x3)],
#                         [np.min(x4), np.max(x4)],
#                         [np.min(x5), np.max(x5)]]
#         }

#         S_delta=delta.analyze(problem,X,Y[:,i]*24,print_to_console=False)
#         S3[i,:]=S_delta['delta']
    
#     plt.figure()
#     plt.stackplot(range(0,363),S3[:,0],S3[:,1],S3[:,2],S3[:,3],S3[:,4],alpha=0.8 , labels=labels)
#     plt.title('The Sensitivity Analysis of Damages of {} Tax Scenario'.format(scenarios_label[scenarios.index(sen)]))
#     plt.legend(loc='right', bbox_to_anchor=(1.35, 0.5),ncol=1, fancybox=True, shadow=True)
#     plt.savefig('Plots/Sensitivity Analysis {} Tax scenario(price).png'.format(scenarios_label[scenarios.index(sen)]) , bbox_inches='tight',dpi=250)
    
#     print(sen)
    