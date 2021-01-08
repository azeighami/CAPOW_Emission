# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:38:35 2021

@author: mzeigha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  
from pandas.plotting import parallel_coordinates


column_name = ['CO2_Damage', 'SNP_Damage', 'Shadow_Price','CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']
scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']

CO2_SP_df = pd.DataFrame([] , columns = column_name)
CO2_SP_df_daily = CO2_SP_df_daily2 = pd.DataFrame([] , columns = column_name)

index = pd.date_range('1/1/2000', periods=36500, freq='D')

stochastic_percentile_df = pd.read_csv ('stochastic_percentile_df.csv')    
CO2_damage_percentile_df = pd.read_csv ('CO2_damage_percentile_df.csv')    
SNP_damage_percentile_df = pd.read_csv ('SNP_damage_percentile_df.csv')
Shadow_price_percentile_df= pd.read_csv (r'Shadow_price_percentile_df.csv')    
cmap = 'coolwarm'



#CO2 damages 

for k in scenarios:
    CO2_SP_df = CO2_SP_df2 = pd.concat([CO2_damage_percentile_df.loc[:,k], SNP_damage_percentile_df.loc[:,k], Shadow_price_percentile_df.loc [:,k] , stochastic_percentile_df] , axis = 1)
    CO2_SP_df.columns = column_name
    CO2_SP_df2.columns = column_name
    

            
#     ## Categorize to high and low
#     for i in range(len(CO2_SP_df)):
#         if CO2_SP_df.loc[i,'CO2_Damage'] <= 10:
#             CO2_SP_df.loc[i,'Dataset'] = 'Low'
#         elif CO2_SP_df.loc[i,'CO2_Damage'] >= 90:
#             CO2_SP_df.loc[i,'Dataset'] = 'High'
#         else:
#             CO2_SP_df.loc[i,'Dataset'] = 'None'
# ################################################################
# #Finding the highst and lowest             
#         if CO2_SP_df2.loc[i,'CO2_Damage'] == CO2_SP_df2['CO2_Damage'].min():
#             CO2_SP_df2.loc[i,'Dataset'] = 'Lowest'
            
#         if CO2_SP_df2.loc[i,'CO2_Damage'] == CO2_SP_df2['CO2_Damage'].max():
#             CO2_SP_df2.loc[i,'Dataset'] = 'Highest'
           
            
#     # CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Highest" , 'Dataset' ] = 'High'        
#     # CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Lowest" , 'Dataset' ] = 'low'        
            
            
#     CO2_SP_df_high = CO2_SP_df.loc[CO2_SP_df['Dataset'] == 'High']
#     CO2_SP_df_low = CO2_SP_df.loc[CO2_SP_df['Dataset'] == 'Low']
    
    
#     #find the highest and lowest
    
#     CO2_SP_df2_high = CO2_SP_df2.loc[CO2_SP_df['Dataset'] == 'Highest']
#     CO2_SP_df2_low = CO2_SP_df2.loc[CO2_SP_df['Dataset'] == 'Lowest']
    
    
#     ####make the parallel plot
#     plt.style.use('seaborn-white')
#     plt.figure()
#     parallel_coordinates(CO2_SP_df,'Dataset',color=('#c9c9c9','#ffa31a','#0000ff','#e6004c','#00cc99'),lw=1)
#     parallel_coordinates(CO2_SP_df2_high,'Dataset',color=('#00cc99'),lw=3)   
#     parallel_coordinates(CO2_SP_df2_low,'Dataset',color=('#e6004c'),lw=3)      
#     plt.legend(loc = 'upper left', fontsize = 'large', bbox_to_anchor=(1.05, 1))
#     # plt.annotate('${}'.format(str(np.round(np.max(CO2_SP_df),2))),(-1,98),annotation_clip=False, fontweight='black')
#     # plt.annotate('${}'.format(str(np.round(np.min(CO2_SP_df),2))),(-1,-2),annotation_clip=False,fontweight='black')
#     plt.ylabel('Percentile')
#     plt.xticks([0,1,2,3,4,5,6,7,8,9,10], column_name , rotation=90)
#     plt.title('Damages of {} Tax Scenario Parallel Plot'.format(k))
#     plt.savefig('Dameges_{}.png'.format(k), bbox_inches='tight',dpi=250)
#     plt.clf()
    
    
    
# for k in range (4):
#     SNP_SP_df = SNP_SP_df2 = pd.concat([SNP_damage_percentile_df.iloc[:,k] , stochastic_percentile_df ] , axis = 1)
#     SNP_SP_df.columns = column_name
#     SNP_SP_df2.columns = column_name
    
#     # Categorize to high and low
#     for i in range(len(SNP_SP_df)):
#         if SNP_SP_df.loc[i,'Damage'] <= 10:
#             SNP_SP_df.loc[i,'Dataset'] = 'Low'
#         elif SNP_SP_df.loc[i,'Damage'] >= 90:
#             SNP_SP_df.loc[i,'Dataset'] = 'High'
#         else:
#             SNP_SP_df.loc[i,'Dataset'] = 'None'
            
#         if SNP_SP_df2.loc[i,'Damage'] == SNP_SP_df['Damage'].min():
#             SNP_SP_df2.loc[i,'Dataset'] = 'Lowest'
            
#         if SNP_SP_df2.loc[i,'Damage'] == SNP_SP_df['Damage'].max():
#             SNP_SP_df2.loc[i,'Dataset'] = 'Highest'
           
            
            
#     SNP_SP_df_high = SNP_SP_df.loc[SNP_SP_df['Dataset'] == 'High']
#     SNP_SP_df_low = SNP_SP_df.loc[SNP_SP_df['Dataset'] == 'Low']
    
    
#     #find the highest and lowest
    
#     SNP_SP_df2_high = SNP_SP_df2.loc[SNP_SP_df['Dataset'] == 'Highest']
#     SNP_SP_df2_low = SNP_SP_df2.loc[SNP_SP_df['Dataset'] == 'Lowest']
    
    
#     # make the parallel plot
#     plt.style.use('seaborn-white')
#     plt.figure()
#     parallel_coordinates(SNP_SP_df,'Dataset',color=('#c9c9c9','#ffa31a','#0000ff','#e6004c','#00cc99'))
#     parallel_coordinates(SNP_SP_df2_high,'Dataset',color=('#00cc99'),lw=3)   
#     parallel_coordinates(SNP_SP_df2_low,'Dataset',color=('#e6004c'),lw=3)      
#     plt.legend(loc = 'upper left', fontsize = 'large', bbox_to_anchor=(1.05, 1))
#     # plt.annotate('${}'.format(str(np.round(np.max(CO2_SP_df),2))),(-1,98),annotation_clip=False, fontweight='black')
#     # plt.annotate('${}'.format(str(np.round(np.min(CO2_SP_df),2))),(-1,-2),annotation_clip=False,fontweight='black')
#     plt.ylabel('Percentile')
#     plt.xticks([0,1,2,3,4,5,6,7,8,9], column_name , rotation=90)
#     plt.title('SNP Damages of {} Tax Scenario Parallel Plot'.format(scenarios[k]))
#     plt.savefig('Dameges_{}.png'.format(scenarios[k]), bbox_inches='tight',dpi=250)
#     plt.clf()
    
    

      #### Color Map    
    CO2_SP_df['Rank'] = CO2_SP_df['CO2_Damage']
    
    plt.style.use('seaborn-white')
    plt.figure()
    parallel_coordinates(CO2_SP_df.sort_values(by='CO2_Damage'),'Rank',colormap=cmap)
    plt.legend('')
    # plt.annotate('${}'.format(str(np.round(np.max(ca_price_2020),2))),(-1,98),annotation_clip=False, fontweight='black')
    # plt.annotate('${}'.format(str(np.round(np.min(ca_price_2020),2))),(-1,-2),annotation_clip=False,fontweight='black')
    plt.ylabel('Percentile')
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10], column_name , rotation=90)
    plt.title('Damages of {} Tax Scenario Parallel Plot'.format(k))
    plt.savefig('ColorMap_Dameges_{}.png'.format(k), bbox_inches='tight',dpi=250)
    plt.clf()
    
    