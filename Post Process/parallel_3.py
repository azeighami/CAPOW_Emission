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
import seaborn as sns


scenarios = ['all_tax', 'CO2', 'no_tax', 'SNP']
directory = [3]
sim_years = 100

CO2_damage_df = SNP_damage_df = pd.DataFrame([])
CO2_damage_temp = SNP_damage_temp = pd.DataFrame(np.zeros((364,4)), columns=scenarios)

CO2_diff = SNP_diff = pd.DataFrame([])

for i in directory:
    for j in range (sim_years):
        for s in scenarios:
        
            
            try:
                CO2_damage_temp.loc[:,s] = pd.read_csv('{}/UCED/LR/{}/CA{}/co2_damages.csv'.format(str(i), s, str(j)), index_col=0)
                SNP_damage_temp.loc[:,s] = pd.read_csv('{}/UCED/LR/{}/CA{}/snp_damages.csv'.format(str(i), s, str(j)), index_col=0)
                

            except:
                print('Damages for {} tax scenario of year {} was not found'.format( s, str(100*i +j )))  
            
        CO2_damage_temp.loc [364,:] = CO2_damage_temp.loc [363,:]
        SNP_damage_temp.loc [364,:] = SNP_damage_temp.loc [363,:]
        
        CO2_damage_df = CO2_damage_df.append(CO2_damage_temp)
        SNP_damage_df = SNP_damage_df.append(SNP_damage_temp)

CO2_diff = pd.DataFrame (CO2_damage_df.iloc[:,2] - CO2_damage_df.iloc[:,3])
SNP_diff = pd.DataFrame (SNP_damage_df.iloc[:,2] - SNP_damage_df.iloc[:,3])

sns.distplot(CO2_diff, hist = False, kde = True,
                 kde_kws = {'linewidth': 3},
                 label = "CO2 Damage")
    
# Plot formatting
plt.legend(prop={'size': 16}, title = 'Airline')
plt.title('The difference between SNP damage in no_tanx and SNP tax scenario')
plt.xlabel('CO2 Damage')
plt.ylabel('Density')