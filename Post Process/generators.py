# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:37:57 2021

@author: mzeigha
"""


import pandas as pd
import numpy as np

scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
directory = [1, 2, 3, 4, 5]
sim_years = 100
generators = pd.read_csv('generators.csv')

# scenarios = ['all_tax' ]
# directory = [3]
# sim_years = 2
# generators = ['AGRICO_6_PL3N5']

Day = pd.RangeIndex(8736)
production = pd.DataFrame([])
production_df = pd.DataFrame([])


for s in scenarios:
    production = pd.DataFrame([])
    production_df = pd.DataFrame([])
    for i in directory:
        for j in range (sim_years):
        
            mwh1 = mwh2 = mwh3 = mwh1_simp = mwh2_simp = mwh3_simp = mwh_simp = pd.DataFrame([])
            
            mwh1 = pd.read_csv('{}/UCED/LR/{}/CA{}/mwh_1.csv'.format(str(i), s, str(j)), index_col=0)
            mwh2 = pd.read_csv('{}/UCED/LR/{}/CA{}/mwh_2.csv'.format(str(i), s, str(j)), index_col=0)
            mwh3 = pd.read_csv('{}/UCED/LR/{}/CA{}/mwh_3.csv'.format(str(i), s, str(j)), index_col=0)
            

            mwh1_simp = mwh1.groupby(['Generator', 'Time'],as_index=True)['Value'].mean()
            mwh2_simp = mwh2.groupby(['Generator', 'Time'],as_index=True)['Value'].mean()
            mwh3_simp = mwh3.groupby(['Generator', 'Time'],as_index=True)['Value'].mean()
            
            mwh_simp = mwh1_simp + mwh2_simp + mwh3_simp
            
            for gen in generators.index:
                P = generators.loc[gen,'name']
                mwh_temp = pd.DataFrame(mwh_simp[P])
                mwh_temp['Day'] = Day//24
                mwh_avg = mwh_temp.groupby(["Day"])['Value'].mean()
                production.loc[:, P] = mwh_avg
                production['Year'] = (i-1)*100 + j
        
            production_df = production_df.append(production)
    
    if s == 'all_tax':
        production_df_all_tax = production_df
    elif s== 'CO2':
        production_df_CO2 = production_df
    elif s== 'no_tax':
        production_df_no_tax = production_df
    elif s== 'SNP':
        production_df_SNP = production_df
        
production_df_all_tax.to_csv (r'production_df_all_tax.csv', index = False, header=True) 
production_df_CO2.to_csv (r'production_df_CO2.csv', index = False, header=True) 
production_df_no_tax.to_csv (r'production_df_no_tax.csv', index = False, header=True) 
production_df_SNP.to_csv (r'production_df_SNP.csv', index = False, header=True) 
        

