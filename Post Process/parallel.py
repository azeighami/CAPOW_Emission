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

#Initialize lists to store average annual values in each region for each needed year
scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
stochastic_column = ['CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']
column_name = ['CO2_Damage', 'SNP_Damage', 'Shadow_Price','CA_load', 'PNW_Load','CA_Hydropower','PNW_Hydropower','Path66_flow','CA_Wind_Power','PNW_Wind_Power', 'Solar_Power']

PNW_wind = CA_wind = solar_daily = daily_load = CA_hydro = PNW_hydro = PNW_daily_load = CA_daily_load = Path66_flow = pd.DataFrame([])
CO2_damage = SNP_damage = Shadow_price = pd.DataFrame(np.zeros((364,4)), columns= scenarios)
CO2_damage_temp = SNP_damage_temp = pd.DataFrame(np.zeros((364,4)), columns=scenarios)
Shadow_price_temp = pd.DataFrame([])


#Loop through 100 sim years 
# directory = [1, 2, 3, 4, 5]
directory = [3]
sim_years = 100

index = pd.date_range('1/1/2000', periods=876000, freq='H')
index_shadow = pd.date_range('1/1/2000', periods=8736, freq='H')
index_daily = pd.date_range('1/1/2000', periods=36500, freq='D')




# Reading the synthetic weather data ##
for i in directory:  
        
    try:
        wind_temp = pd.read_csv('{}/Stochastic_engine/Synthetic_wind_power/wind_power_sim.csv'.format(str(i)), index_col=0).set_index (index)
        solar_temp = pd.read_csv('{}/Stochastic_engine/Synthetic_solar_power/solar_power_sim.csv'.format(str(i)), index_col=0).set_index (index)
        CA_hydro_temp = pd.read_excel('{}/Stochastic_engine/CA_hydropower/CA_hydro_daily.xlsx'.format(str(i)), index_col=0).set_index (index_daily)
        PNW_hydro_temp = pd.read_excel('{}/Stochastic_engine/PNW_hydro/PNW_hydro_daily.xlsx'.format(str(i)), index_col=0).set_index (index_daily)
        load_path = pd.read_csv('{}/Stochastic_engine/Synthetic_demand_pathflows/Load_Path_Sim.csv'.format(str(i)), index_col=0).set_index (index_daily)
        hourly_load = pd.read_csv('{}/Stochastic_engine/Synthetic_demand_pathflows/Sim_hourly_load.csv'.format(str(i)), index_col=0).set_index (index)
                    
    except:
        print('Year {} weather data not found'.format(str(100*i )))
        
    
    PNW_wind_temp = pd.DataFrame(wind_temp.iloc[:,1].resample("A").sum())
    CA_wind_temp = pd.DataFrame(wind_temp.iloc[:,2].resample("A").sum())
    solar_daily_temp = solar_temp.resample("A").sum()
    daily_load_temp = hourly_load.resample("A").sum()
    PNW_daily_load_temp = pd.DataFrame(daily_load_temp.iloc[:,1]).resample("A").sum()
    CA_daily_load_temp = pd.DataFrame(daily_load_temp.iloc[:,2] + daily_load_temp.iloc[:,3] + daily_load_temp.iloc[:,4] + daily_load_temp.iloc[:,5]).resample("A").sum()
    Path66_flow_temp = pd.DataFrame(load_path.iloc [:,9]).resample("A").sum()
    CA_hydro_temp_daily = pd.DataFrame(CA_hydro_temp.iloc[:,0] + CA_hydro_temp.iloc[:,1]).resample("A").sum()
        
    PNW_wind = PNW_wind.append (PNW_wind_temp, ignore_index=True)
    CA_wind = CA_wind.append (CA_wind_temp, ignore_index=True)
    solar_daily = solar_daily.append(solar_daily_temp, ignore_index=True)
    PNW_daily_load = PNW_daily_load.append(PNW_daily_load_temp, ignore_index=True)
    CA_daily_load = CA_daily_load.append(CA_daily_load_temp, ignore_index=True)
    Path66_flow = Path66_flow.append(Path66_flow_temp, ignore_index=True)
    CA_hydro = CA_hydro.append(CA_hydro_temp_daily, ignore_index=True)
    PNW_hydro = PNW_hydro.append(PNW_hydro_temp, ignore_index=True)
    
    
# PNW_wind.to_csv (r'PNW_wind.csv', index = False, header=True)
# CA_wind.to_csv (r'CA_wind.csv', index = False, header=True)
# solar_daily.to_csv (r'solar_daily.csv', index = False, header=True)
# PNW_daily_load.to_csv (r'PNW_daily_load.csv', index = False, header=True)
# CA_daily_load.to_csv (r'CA_daily_load.csv', index = False, header=True)
# Path66_flow.to_csv (r'Path66_flow.csv', index = False, header=True)
# CA_hydro.to_csv (r'CA_hydro.csv', index = False, header=True)
# PNW_hydro.to_csv (r'PNW_hydro.csv', index = False, header=True)    

# # ## Reading the CO2 and Local air damages data ##
# for i in directory:
#     for j in range (sim_years):
#         for s in scenarios:
        
            
#             try:
#                 CO2_damage_temp.loc[:,s] = pd.read_csv('{}/UCED/LR/{}/CA{}/co2_damages.csv'.format(str(i), s, str(j)), index_col=0)
#                 SNP_damage_temp.loc[:,s] = pd.read_csv('{}/UCED/LR/{}/CA{}/snp_damages.csv'.format(str(i), s, str(j)), index_col=0)
                

                
#                 shadow_temp = pd.read_csv('{}/UCED/LR/{}/CA{}/shadow_price.csv'.format(str(i), s, str(j)), index_col=0)
#                 shadow_temp.loc[shadow_temp['Value'] >1000 , 'Value' ] = 1000
#                 shadow_hourly = shadow_temp.groupby(['Time'] , as_index=True).mean()
#                 shadow_hourly.index = index_shadow
#                 Shadow_price_temp = shadow_hourly.resample("D").mean()
#                 Shadow_price_temp.reset_index(drop=True, inplace=True)
#                 Shadow_price[s] = Shadow_price_temp
                
#             except:
#                 print('Damages for {} tax scenario of year {} was not found'.format( s, str(100*i +j )))  
            
#         CO2_damage_temp.loc [364,:] = CO2_damage_temp.loc [363,:]
#         SNP_damage_temp.loc [364,:] = SNP_damage_temp.loc [363,:]
#         Shadow_price.loc [364,:] = Shadow_price.loc [363,:]
        
#         CO2_damage_df = CO2_damage_df.append(CO2_damage_temp)
#         SNP_damage_df = SNP_damage_df.append(SNP_damage_temp)
#         Shadow_price_df = Shadow_price_df.append(Shadow_price)
        
# CO2_damage_df.index = index_daily
# SNP_damage_df.index = index_daily
# Shadow_price_df.index = index_daily

# CO2_damage_df = CO2_damage_df.resample('A').sum()
# SNP_damage_df = SNP_damage_df.resample('A').sum()
# Shadow_price_df = Shadow_price_df.resample('A').mean()
        
# # # # CO2_damage_df.to_csv (r'CO2_damage.csv', index = False, header=True)    
# # # # SNP_damage_df.to_csv (r'SNP_damage.csv', index = False, header=True)
# # # Shadow_price_df.to_csv (r'Shadow_price_df.csv', index = False, header=True)
        
# stochastic_df = pd.DataFrame([] , columns = column_name)
# stochastic_percentile_df = pd.DataFrame([])

# CO2_damage_percentile_df = pd.DataFrame([])
# SNP_damage_percentile_df = pd.DataFrame([])
# Shadow_price_percentile_df = pd.DataFrame([])

# stochastic_df.iloc[:,0] = CA_daily_load.iloc[:,0] 
# stochastic_df.iloc[:,1] = PNW_daily_load.iloc[:,0] 
# stochastic_df.iloc[:,2] = CA_hydro.iloc[:,0] 
# stochastic_df.iloc[:,3] = PNW_hydro.iloc[:,0] 
# stochastic_df.iloc[:,4] = Path66_flow.iloc[:,0] 
# stochastic_df.iloc[:,5] = CA_wind.iloc[:,0]
# stochastic_df.iloc[:,6] = PNW_wind.iloc[:,0]
# stochastic_df.iloc[:,7] = solar_daily.iloc[:,0]


# for j in range(8):
#     for i in range(len(stochastic_df)):
#         stochastic_percentile_df.loc[i,j] = stats.percentileofscore(stochastic_df.values[:,j], stochastic_df.values[i,j])
#     print (j)
# print (stochastic_percentile_df)


# for j in range(4):
#     for i in range(len(CO2_damage_df)):
#         CO2_damage_percentile_df.loc[i,j] = stats.percentileofscore(CO2_damage_df.values[:,j], CO2_damage_df.values[i,j])
#     print (j)
# print (CO2_damage_percentile_df)  

      
# for j in range(4):
#     for i in range(len(SNP_damage_df)):
#         SNP_damage_percentile_df.loc[i,j] = stats.percentileofscore(SNP_damage_df.values[:,j], SNP_damage_df.values[i,j])
#     print (j)
# print (SNP_damage_percentile_df)

# for j in range(4):
#     for i in range(len(Shadow_price_df)):
#         Shadow_price_percentile_df.loc[i,j] = stats.percentileofscore(Shadow_price_df.values[:,j], Shadow_price_df.values[i,j])
#     print (j)
# print (Shadow_price_percentile_df)

# stochastic_percentile_df.columns = column_name
# CO2_damage_percentile_df.columns = scenarios
# SNP_damage_percentile_df.columns = scenarios
# Shadow_price_percentile_df.columns = scenarios

# stochastic_percentile_df.to_csv (r'stochastic_percentile_df.csv', index = False, header=True)    
# CO2_damage_percentile_df.to_csv (r'CO2_damage_percentile_df.csv', index = False, header=True)    
# SNP_damage_percentile_df.to_csv (r'SNP_damage_percentile_df.csv', index = False, header=True)    
# Shadow_price_percentile_df.to_csv (r'Shadow_price_percentile_df.csv', index = False, header=True)    








