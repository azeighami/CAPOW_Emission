# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:15:10 2020

@author: mzeigha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  
from pandas.plotting import parallel_coordinates
import seaborn as sns


#####Initializing
scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
stochastic_column = ['CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']
column_name = ['CO2_damage','SNP_Damage', 'Shadow_Price','CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']

stochastic_percentile_df = pd.DataFrame([])
CO2_damage_percentile_df = pd.DataFrame([])
SNP_damage_percentile_df = pd.DataFrame([])
Shadow_price_percentile_df = pd.DataFrame([])
Day = pd.DataFrame([])


#The color map theme 
cmap = 'coolwarm'

#### Reading the "Daily results" of simulation 
stochastic_df = pd.read_csv('Results/Stochastic_df.csv')
CO2_damage_df = pd.read_csv('Results/CO2_damage.csv')
SNP_damage_df = pd.read_csv('Results/SNP_damage.csv')
Shadow_price_df = pd.read_csv('Results/Shadow_price.csv')


########### Converting the Daily data to yearly

Day["Day"] = pd.RangeIndex(182500)

stochastic_df["Year"] = Day["Day"]//365
CO2_damage_df["Year"] = Day["Day"]//365
SNP_damage_df["Year"] = Day["Day"]//365
Shadow_price_df["Year"] = Day["Day"]//365


stochastic_df = stochastic_df.groupby(['Year']).sum()
CO2_damage_df = CO2_damage_df.groupby(['Year']).sum()
SNP_damage_df = SNP_damage_df.groupby(['Year']).sum()
Shadow_price_df = Shadow_price_df.groupby(['Year']).mean()


# #####Building the percentile dataframe for each of results dataframe 

for j in range(8):
    print (j)
    for i in range(len(stochastic_df)):
        stochastic_percentile_df.loc[i,j] = stats.percentileofscore(stochastic_df.values[:,j], stochastic_df.values[i,j])
print (stochastic_percentile_df)


for j in range(4):
    print (j)
    for i in range(len(CO2_damage_df)):
        CO2_damage_percentile_df.loc[i,j] = stats.percentileofscore(CO2_damage_df.values[:,j], CO2_damage_df.values[i,j])
print (CO2_damage_percentile_df)  

      
for j in range(4):
    print (j)
    for i in range(len(SNP_damage_df)):
        SNP_damage_percentile_df.loc[i,j] = stats.percentileofscore(SNP_damage_df.values[:,j], SNP_damage_df.values[i,j])
print (SNP_damage_percentile_df)

for j in range(4):
    print (j)
    for i in range(len(Shadow_price_df)):
        Shadow_price_percentile_df.loc[i,j] = stats.percentileofscore(Shadow_price_df.values[:,j], Shadow_price_df.values[i,j])
print (Shadow_price_percentile_df)

stochastic_percentile_df.columns = stochastic_column
CO2_damage_percentile_df.columns = scenarios
SNP_damage_percentile_df.columns = scenarios
Shadow_price_percentile_df.columns = scenarios

########## Saving the DataFrames
# ##stochastic_percentile_df.to_csv (r'stochastic_percentile_df.csv', index = False, header=True)    
# ##CO2_damage_percentile_df.to_csv (r'CO2_damage_percentile_df.csv', index = False, header=True)    
# ##SNP_damage_percentile_df.to_csv (r'SNP_damage_percentile_df.csv', index = False, header=True)
# ##Shadow_price_percentile_df.to_csv (r'Shadow_price_percentile_df.csv', index = False, header=True)



# ########## Reading the DataFrames
# ##stochastic_percentile_df = pd.read_csv('stochastic_percentile_df.csv')
# ##CO2_damage_percentile_df = pd.read_csv('CO2_damage_percentile_df.csv')
# ##SNP_damage_percentile_df = pd.read_csv('SNP_damage_percentile_df.csv')
# ##Shadow_price_percentile_df = pd.read_csv('Shadow_price_percentile_df.csv')
 


for k in scenarios:
    plot_df = plot_df2 = pd.concat([CO2_damage_percentile_df.loc[:,k],SNP_damage_percentile_df.loc[:,k], Shadow_price_percentile_df.loc [:,k] , stochastic_percentile_df] , axis = 1)
    plot_df.columns = column_name
    plot_df2.columns = column_name
    
    plot_df = plot_df.drop(columns = ['PNW_Load','Path66_flow' , 'PNW_Wind_Power'])
    plot_df2 = plot_df2.drop(columns = ['PNW_Load','Path66_flow' , 'PNW_Wind_Power'])

            
#     ##### Categorize to high and low
#     for i in range(len(plot_df)):
#         if plot_df.loc[i,'SNP_Damage'] <= 10:
#             plot_df.loc[i,'Dataset'] = 'Low'
#         elif plot_df.loc[i,'SNP_Damage'] >= 90:
#             plot_df.loc[i,'Dataset'] = 'High'
#         else:
#             plot_df.loc[i,'Dataset'] = 'None'
# ################################################################
# ######Finding the highst and lowest             
#         if plot_df2.loc[i,'SNP_Damage'] == plot_df2['SNP_Damage'].min():
#             plot_df2.loc[i,'Dataset'] = 'Lowest'
            
#         if plot_df2.loc[i,'SNP_Damage'] == plot_df2['SNP_Damage'].max():
#             plot_df2.loc[i,'Dataset'] = 'Highest'
           
            
#     # CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Highest" , 'Dataset' ] = 'High'        
#     # CO2_SP_df.loc[CO2_SP_df['Dataset'] == "Lowest" , 'Dataset' ] = 'low'        
            
            
#     plot_df_high = plot_df.loc[plot_df['Dataset'] == 'High']
#     plot_df_low = plot_df.loc[plot_df['Dataset'] == 'Low']
#     plot_df_none = plot_df.loc[plot_df['Dataset'] == 'None']
    
    
#     #find the highest and lowest
    
#     plot_df2_high = plot_df2.loc[plot_df2['Dataset'] == 'Highest']
#     plot_df2_low = plot_df2.loc[plot_df2['Dataset'] == 'Lowest']
    
    
#     ###make the parallel plot
#     plt.style.use('seaborn-white')
#     plt.figure()
#     parallel_coordinates(plot_df_none,'Dataset',color='#c9c9c9', alpha = 0.25, lw=1) 
#     parallel_coordinates(plot_df_high,'Dataset',color= '#ffa31a', alpha = 0.5, lw=1)
#     parallel_coordinates(plot_df_low,'Dataset',color='#0000ff', alpha = 0.5, lw=1)
#     parallel_coordinates(plot_df2_high,'Dataset',color=('#00cc99'),lw=3)   
#     parallel_coordinates(plot_df2_low,'Dataset',color=('#e6004c'),lw=3)      
#     plt.legend(loc = 'upper left', fontsize = 'large', bbox_to_anchor=(1.05, 1))
#     # plt.annotate('${}'.format(str(np.round(np.max(CO2_SP_df),2))),(-1,98),annotation_clip=False, fontweight='black')
#     # plt.annotate('${}'.format(str(np.round(np.min(CO2_SP_df),2))),(-1,-2),annotation_clip=False,fontweight='black')
#     plt.ylabel('Percentile')
#     plt.xticks( rotation=90)
#     plt.title('Damages of {} Tax Scenario Parallel Plot'.format(k))
#     plt.savefig('Plots/Dameges_{}.png'.format(k), bbox_inches='tight',dpi=250)
#     plt.clf()
    
    
    


####################################### Color Map 
    # plot_df = plot_df.drop(columns = ['Dataset'])        
    # plot_df['Rank'] = plot_df['SNP_Damage']
    
    # plt.style.use('seaborn-white')
    # plt.figure()
    # parallel_coordinates(plot_df.sort_values(by='SNP_Damage'),'Rank',colormap=cmap)
    # plt.legend('')
    # # plt.annotate('${}'.format(str(np.round(np.max(ca_price_2020),2))),(-1,98),annotation_clip=False, fontweight='black')
    # # plt.annotate('${}'.format(str(np.round(np.min(ca_price_2020),2))),(-1,-2),annotation_clip=False,fontweight='black')
    # plt.ylabel('Percentile')
    # plt.xticks(rotation=90)
    # plt.title('Damages of {} Tax Scenario Parallel Plot'.format(k))
    # plt.savefig('Plots/ColorMap_Dameges_{}.png'.format(k), bbox_inches='tight',dpi=250)
    # plt.clf()
    

####### Histogram 

SNP_diff_all = pd.DataFrame (SNP_damage_df.loc[:,'all_tax'] - SNP_damage_df.loc[:,'SNP'])
SNP_diff_no = pd.DataFrame ( SNP_damage_df.loc[:,'no_tax'] - SNP_damage_df.loc[:,'SNP'])

# sns.distplot(SNP_diff_all,SNP_diff_no, hist = False, kde = True,
#                   kde_kws = {'linewidth': 3},
#                   label = "All Tax vs. SNP Tax")

sns.distplot(SNP_diff_no, hist = False, kde = True,
                  kde_kws = {'linewidth': 3},
                  label = "No Tax vs. SNP Tax")
    
plt.title('Damage Distribution Dencity')
plt.xlabel('No Tax vs. SNP Tax Damages')
plt.ylabel('Density')
plt.savefig('Plots/No Tax vs. SNP Tax Damages.png', bbox_inches='tight',dpi=250)
plt.clf()




sns.distplot(SNP_diff_all,SNP_diff_no, hist = False, kde = True,
                  kde_kws = {'linewidth': 3},
                  label = "All Tax vs. SNP Tax")

plt.title('Damage Distribution Dencity')
plt.xlabel('All Tax vs. SNP Tax Damages')
plt.ylabel('Density')
plt.savefig('Plots/All Tax vs. SNP Tax Damages.png', bbox_inches='tight',dpi=250)
plt.clf()
