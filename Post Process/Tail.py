# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:05:46 2021

@author: mzeigha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
from scipy import stats  



scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
scenarios_label = ['All' , 'CO2' , 'No', 'SNP']
stochastic_column = ['CA Load', 'PNW Load','CA Hydropower','PNW Hydropower','Path66 Flow','CA Wind Power','PNW Wind Power', 'CA Solar Power']
column_name = ['Difference', 'Shadow Price','CA Load', 'PNW Load','CA Hydropower','PNW Hydropower','Path66 Flow','CA Wind Power','PNW Wind Power', 'CA Solar Power']


# stochastic_df = pd.read_csv('Results/Stochastic_df.csv')
# CO2_damage_df = pd.read_csv('Results/CO2_damage.csv')
# SNP_damage_df = pd.read_csv('Results/SNP_damage.csv')
# Shadow_price_df = pd.read_csv('Results/Shadow_price.csv')

stochastic_percentile_df = pd.read_csv('Daily Percentile/stochastic_percentile_df.csv')
CO2_damage_percentile_df = pd.read_csv('Daily Percentile/CO2_damage_percentile_df.csv')
SNP_damage_percentile_df = pd.read_csv('Daily Percentile/SNP_damage_percentile_df.csv')
Shadow_price_percentile_df = pd.read_csv('Daily Percentile/Shadow_price_percentile_df.csv')
diff_percentile = pd.read_csv('Daily Percentile/diff_percentile.csv')

##############################################################################

# diff = SNP_damage_df['no_tax'] - SNP_damage_df['SNP']
# diff_percentile = np.zeros(len(diff))

# for i in range(len(diff)):
#         diff_percentile[i] = stats.percentileofscore(diff.values, diff.values[i])

##############################################################################

    
tail = pd.concat([diff_percentile, Shadow_price_percentile_df.loc [:,'SNP'] , stochastic_percentile_df] , axis = 1)
tail.columns = column_name

tail = tail[tail['Difference'] >= 99]

plot_df = tail.reset_index()    
plot_df = plot_df.drop(columns = ['index','PNW Load','Path66 Flow' , 'PNW Wind Power'])

#     ##### Categorize to high and low
for i in range(len(plot_df)):
    if plot_df.loc[i,'Difference'] <= 99.1:
        plot_df.loc[i,'Dataset'] = 'Low'
    elif plot_df.loc[i,'Difference'] >= 9.9:
        plot_df.loc[i,'Dataset'] = 'High'
    else:
        plot_df.loc[i,'Dataset'] = 'None'
# ################################################################
# ######Finding the highst and lowest             
    if plot_df.loc[i,'Difference'] == plot_df['Difference'].min():
        plot_df.loc[i,'Dataset'] = 'Lowest'
        
    if plot_df.loc[i,'Difference'] == plot_df['Difference'].max():
        plot_df.loc[i,'Dataset'] = 'Highest'
       
        
# CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Highest" , 'Dataset' ] = 'High'        
# CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Lowest" , 'Dataset' ] = 'low'        
        
        
plot_df_high = plot_df.loc[plot_df['Dataset'] == 'High']
plot_df_low = plot_df.loc[plot_df['Dataset'] == 'Low']
plot_df_none = plot_df.loc[plot_df['Dataset'] == 'None']


#find the highest and lowest

plot_df_highest = plot_df.loc[plot_df['Dataset'] == 'Highest']
plot_df_lowest = plot_df.loc[plot_df['Dataset'] == 'Lowest']


###make the parallel plot
plt.style.use('seaborn-white')
plt.figure()
parallel_coordinates(plot_df_none,'Dataset',color='#c9c9c9', alpha = 0.25, lw=1) 
parallel_coordinates(plot_df_high,'Dataset',color= '#ffa31a', alpha = 0.5, lw=1)
parallel_coordinates(plot_df_low,'Dataset',color='#0000ff', alpha = 0.5, lw=1)
parallel_coordinates(plot_df_highest,'Dataset',color=('#00cc99'),lw=3)   
parallel_coordinates(plot_df_lowest,'Dataset',color=('#e6004c'),lw=3)      
plt.legend(loc = 'upper left', fontsize = 'large', bbox_to_anchor=(1.05, 1))
plt.ylabel('Percentile')
plt.xticks( rotation=90)
plt.title('99th Percentile Difference in SNP Tax and No Tax Daily Damages Scenarios Parallel Plot')
plt.savefig('Plots/99th Percentile Difference.png', bbox_inches='tight',dpi=250)
# plt.clf()