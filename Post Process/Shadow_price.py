# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:34:33 2021

@author: mzeigha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
Time = damage = pd.DataFrame([])

shadow_temp = pd.read_csv('shadow_price.csv')
# CO2_damage_df = pd.read_csv('Results/CO2_damage.csv')
SNP_damage_df = pd.read_csv('Results/SNP_damage.csv')

Time["Hour"] = pd.RangeIndex(len(shadow_temp))
# Time['Day'] = pd.RangeIndex(len(SNP_damage_df))


shadow_temp["Year"] = Time["Hour"]//(364*24)
shadow_temp["Day"] = Time["Hour"]//24 - 364*shadow_temp["Year"]
shadow_temp["Day2"] = 365*shadow_temp["Year"] + shadow_temp["Day"]

# all_tax = shadow_temp[shadow_temp['all_tax'] >200].reset_index().drop(columns = 'index')

# for s in scenarios:
#     # for i in range(len(all_tax)):
#     #     damage.loc[i,s] = SNP_damage_df.loc[all_tax.loc[i,'Day2'], s]
#     #     print (i)
    

#     count = shadow_temp[shadow_temp[s] >200].groupby(['Day']).count()

#     plt.scatter(pd.RangeIndex(364), count[s] , alpha=0.5)
#     plt.title('{} slack variable distribution'.format(s))
#     plt.xlabel('Day of the Year')
#     plt.ylabel('#times slack variable kicked in')
#     plt.savefig('Plots/{} slack variable.png'.format(s), bbox_inches='tight',dpi=250)
#     plt.show()



all_tax = shadow_temp[shadow_temp['all_tax'] >200]
CO2 = shadow_temp[shadow_temp['CO2'] >200]
no_tax = shadow_temp[shadow_temp['no_tax'] >200]
SNP = shadow_temp[shadow_temp['SNP'] >200]