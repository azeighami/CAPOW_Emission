# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:29:46 2020

@author: jawessel
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats  
from pandas.plotting import parallel_coordinates

#Initialize lists to store average annual values in each region for each needed year
ca_price_2020, ca_co2_2020, ca_load_2020, ca_hydro_2020, ca_solar_2020, ca_wind_2020 = [], [], [], [], [], []
pnw_price_2020, pnw_co2_2020, pnw_load_2020, pnw_hydro_2020, pnw_solar_2020, pnw_wind_2020 = [], [], [], [], [], []
ca_price_2025, ca_co2_2025, ca_load_2025, ca_hydro_2025, ca_solar_2025, ca_wind_2025 = [], [], [], [], [], []
pnw_price_2025, pnw_co2_2025, pnw_load_2025, pnw_hydro_2025, pnw_solar_2025, pnw_wind_2025 = [], [], [], [], [], []
ca_price_2030, ca_co2_2030, ca_load_2030, ca_hydro_2030, ca_solar_2030, ca_wind_2030 = [], [], [], [], [], []
pnw_price_2030, pnw_co2_2030, pnw_load_2030, pnw_hydro_2030, pnw_solar_2030, pnw_wind_2030 = [], [], [], [], [], []
ca_price_2035, ca_co2_2035, ca_load_2035, ca_hydro_2035, ca_solar_2035, ca_wind_2035 = [], [], [], [], [], []
pnw_price_2035, pnw_co2_2035, pnw_load_2035, pnw_hydro_2035, pnw_solar_2035, pnw_wind_2035 = [], [], [], [], [], []
ca_price_2040, ca_co2_2040, ca_load_2040, ca_hydro_2040, ca_solar_2040, ca_wind_2040 = [], [], [], [], [], []
pnw_price_2040, pnw_co2_2040, pnw_load_2040, pnw_hydro_2040, pnw_solar_2040, pnw_wind_2040 = [], [], [], [], [], []
ca_price_2045, ca_co2_2045, ca_load_2045, ca_hydro_2045, ca_solar_2045, ca_wind_2045 = [], [], [], [], [], []
pnw_price_2045, pnw_co2_2045, pnw_load_2045, pnw_hydro_2045, pnw_solar_2045, pnw_wind_2045 = [], [], [], [], [], []
ca_price_2050, ca_co2_2050, ca_load_2050, ca_hydro_2050, ca_solar_2050, ca_wind_2050 = [], [], [], [], [], []
pnw_price_2050, pnw_co2_2050, pnw_load_2050, pnw_hydro_2050, pnw_solar_2050, pnw_wind_2050 = [], [], [], [], [], []

column_names = ['Price','CO2 Emissions','Load','Hydropower','Solar Power','Wind Power']

wind_data = pd.read_csv('../../CAPOW_jaw/Stochastic_engine/Synthetic_wind_power/wind_power_sim.csv')
solar_data = pd.read_csv('../../CAPOW_jaw/Stochastic_engine/Synthetic_solar_power/solar_power_sim.csv')

#Loop through 100 sim years 
years = np.arange(2020,2055,5)
pathways = ['MID_','BAT_','EV_','LOWRECOST_','HIGHRECOST_']
path = 'LOWRECOST_'
sim_years = 100
d = 250
cmap = 'coolwarm'

for i in years:  
    for j in range(sim_years):
           
        ### CA ###
        try:
            ca_price = pd.read_csv('data/{}{}/CA{}/shadow_price_treated.csv'.format(path,str(i),str(j)))
            ca_co2 = pd.read_csv('data/{}{}/CA{}/TotalCO2.txt'.format(path,str(i),str(j)))
            ca_load = pd.read_csv('Sim_hourly_load_{}{}.csv'.format(path,str(i)))
            mwh_1 = pd.read_csv('data/{}{}/CA{}/mwh_1.csv'.format(path,str(i),str(j)))
            mwh_2 = pd.read_csv('data/{}{}/CA{}/mwh_2.csv'.format(path,str(i),str(j)))
            mwh_3 = pd.read_csv('data/{}{}/CA{}/mwh_3.csv'.format(path,str(i),str(j)))
#            ca_solar = pd.read_csv('data/{}{}/CA{}/solar_out.csv'.format(path,str(i),str(j)))
#            ca_wind = pd.read_csv('data/{}{}/CA{}/wind_out.csv'.format(path,str(i),str(j)))
            
            if i == 2020:
                ca_price_2020.append(ca_price['Value'].mean())
                ca_co2_2020.append(ca_co2.iloc[0,0])
                ca_load_2020.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2020 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2020.append(temp_ca_hydro_2020['Value'].mean())
#                ca_solar_2020.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2020.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2020.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2020.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())

            if i == 2025:
                ca_price_2025.append(ca_price['Value'].mean())
                ca_co2_2025.append(ca_co2.iloc[0,0])
                ca_load_2025.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2025 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2025.append(temp_ca_hydro_2025['Value'].mean())
#                ca_solar_2025.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2025.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2025.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2025.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                
            if i == 2030:
                ca_price_2030.append(ca_price['Value'].mean())
                ca_co2_2030.append(ca_co2.iloc[0,0])
                ca_load_2030.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2030 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2030.append(temp_ca_hydro_2030['Value'].mean())
#                ca_solar_2030.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2030.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2030.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2030.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())

            if i == 2035:
                ca_price_2035.append(ca_price['Value'].mean())
                ca_co2_2035.append(ca_co2.iloc[0,0])
                ca_load_2035.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2035 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2035.append(temp_ca_hydro_2035['Value'].mean())
#                ca_solar_2035.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2035.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2035.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2035.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())

            if i == 2040:
                ca_price_2040.append(ca_price['Value'].mean())
                ca_co2_2040.append(ca_co2.iloc[0,0])
                ca_load_2040.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2040 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2040.append(temp_ca_hydro_2040['Value'].mean())
#                ca_solar_2040.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2040.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2040.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2040.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())

            if i == 2045:
                ca_price_2045.append(ca_price['Value'].mean())
                ca_co2_2045.append(ca_co2.iloc[0,0])
                ca_load_2045.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum())
                temp_ca_hydro_2045 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                ca_hydro_2045.append(temp_ca_hydro_2045['Value'].mean())
#                ca_solar_2045.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2045.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2045.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2045.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())                
                
            if i == 2050:
                ca_price_2050.append(ca_price['Value'].mean())
                ca_co2_2050.append(ca_co2.iloc[0,0])
                ca_load_2050.append(ca_load.iloc[j*8760:8760*(j+1),3:7].mean().sum()) 
                temp_ca_hydro_2050 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum() 
                ca_hydro_2050.append(temp_ca_hydro_2050['Value'].mean())  
#                ca_solar_2050.append(ca_solar.groupby('Zone')['Value'].mean().sum())
#                ca_wind_2050.append(ca_wind.groupby('Zone')['Value'].mean().sum())
                ca_solar_2050.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())
                ca_wind_2050.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_CAISO'.format(path,str(i))].sum())

        except:
            print('{}{} Year {} CA not found'.format(path,str(i),str(j)))
            
        ### PNW ###    
        try:
            pnw_price = pd.read_csv('data/{}{}/PNW{}/shadow_price_treated.csv'.format(path,str(i),str(j)))
            pnw_co2 = pd.read_csv('data/{}{}/PNW{}/TotalCO2.txt'.format(path,str(i),str(j)))
            pnw_load = pd.read_csv('Sim_hourly_load_{}{}.csv'.format(path,str(i)))
            mwh_1 = pd.read_csv('data/{}{}/PNW{}/mwh_1.csv'.format(path,str(i),str(j)))
            mwh_2 = pd.read_csv('data/{}{}/PNW{}/mwh_2.csv'.format(path,str(i),str(j)))
            mwh_3 = pd.read_csv('data/{}{}/PNW{}/mwh_3.csv'.format(path,str(i),str(j)))
#            pnw_solar = pd.read_csv('data/{}{}/PNW{}/solar_out.csv'.format(path,str(i),str(j)))
#            pnw_wind = pd.read_csv('data/{}{}/PNW{}/wind_out.csv'.format(path,str(i),str(j)))
            
            if i == 2020:
                pnw_price_2020.append(pnw_price['Value'].mean())
                pnw_co2_2020.append(pnw_co2.iloc[0,0])
                pnw_load_2020.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2020 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2020.append(temp_pnw_hydro_2020['Value'].mean())
#                pnw_solar_2020.append(pnw_solar['Value'].mean())
#                pnw_wind_2020.append(pnw_wind['Value'].mean())
                pnw_solar_2020.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2020.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                
            if i == 2025:
                pnw_price_2025.append(pnw_price['Value'].mean())
                pnw_co2_2025.append(pnw_co2.iloc[0,0])
                pnw_load_2025.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2025 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2025.append(temp_pnw_hydro_2025['Value'].mean())
#                pnw_solar_2025.append(pnw_solar['Value'].mean())
#                pnw_wind_2025.append(pnw_wind['Value'].mean())
                pnw_solar_2025.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2025.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())

            if i == 2030:
                pnw_price_2030.append(pnw_price['Value'].mean())
                pnw_co2_2030.append(pnw_co2.iloc[0,0])
                pnw_load_2030.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2030 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2030.append(temp_pnw_hydro_2030['Value'].mean())
#                pnw_solar_2030.append(pnw_solar['Value'].mean())
#                pnw_wind_2030.append(pnw_wind['Value'].mean())
                pnw_solar_2030.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2030.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())

            if i == 2035:
                pnw_price_2035.append(pnw_price['Value'].mean())
                pnw_co2_2035.append(pnw_co2.iloc[0,0])
                pnw_load_2035.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2035 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2035.append(temp_pnw_hydro_2035['Value'].mean())
#                pnw_solar_2035.append(pnw_solar['Value'].mean())
#                pnw_wind_2035.append(pnw_wind['Value'].mean())
                pnw_solar_2035.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2035.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())

            if i == 2040:
                pnw_price_2040.append(pnw_price['Value'].mean())
                pnw_co2_2040.append(pnw_co2.iloc[0,0])
                pnw_load_2040.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2040 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2040.append(temp_pnw_hydro_2040['Value'].mean())
#                pnw_solar_2040.append(pnw_solar['Value'].mean())
#                pnw_wind_2040.append(pnw_wind['Value'].mean())
                pnw_solar_2040.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2040.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())

            if i == 2045:
                pnw_price_2045.append(pnw_price['Value'].mean())
                pnw_co2_2045.append(pnw_co2.iloc[0,0])
                pnw_load_2045.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2045 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum()
                pnw_hydro_2045.append(temp_pnw_hydro_2045['Value'].mean())
#                pnw_solar_2045.append(pnw_solar['Value'].mean())
#                pnw_wind_2045.append(pnw_wind['Value'].mean())
                pnw_solar_2045.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2045.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                
            if i == 2050:
                pnw_price_2050.append(pnw_price['Value'].mean())
                pnw_co2_2050.append(pnw_co2.iloc[0,0])
                pnw_load_2050.append(pnw_load.iloc[j*8760:8760*(j+1),2].mean())
                temp_pnw_hydro_2050 = mwh_1[(mwh_1['Type']=='Hydro') | (mwh_1['Type']=='PSH')]\
                    .append(mwh_2[(mwh_2['Type']=='Hydro') | (mwh_2['Type']=='PSH')])\
                    .append(mwh_3[(mwh_3['Type']=='Hydro') | (mwh_3['Type']=='PSH')]).groupby('Time').sum() 
                pnw_hydro_2050.append(temp_pnw_hydro_2050['Value'].mean())
#                pnw_solar_2050.append(pnw_solar['Value'].mean())
#                pnw_wind_2050.append(pnw_wind['Value'].mean())
                pnw_solar_2050.append(solar_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())
                pnw_wind_2050.append(wind_data.iloc[j*8760:8760*(j+1)]['{}{}_PNW'.format(path,str(i))].sum())

        except:
            print('{}{} Year {} PNW not found'.format(path,str(i),str(j)))
            
        print('Sim Year {} in Year {} complete'.format(str(j+1),str(i)))

###############################################################################

#Create dataframes by grouping together all completed lists of data
pp_ca_data_2020 = pd.DataFrame(columns = column_names)
pp_ca_data_2020['Price'] = ca_price_2020
pp_ca_data_2020['CO2 Emissions'] = ca_co2_2020
pp_ca_data_2020['Load'] = ca_load_2020
pp_ca_data_2020['Hydropower'] = ca_hydro_2020
pp_ca_data_2020['Solar Power'] = ca_solar_2020
pp_ca_data_2020['Wind Power'] = ca_wind_2020
pc_ca_2020=np.zeros((len(pp_ca_data_2020),6))

pp_ca_data_2025 = pd.DataFrame(columns = column_names)
pp_ca_data_2025['Price'] = ca_price_2025
pp_ca_data_2025['CO2 Emissions'] = ca_co2_2025
pp_ca_data_2025['Load'] = ca_load_2025
pp_ca_data_2025['Hydropower'] = ca_hydro_2025
pp_ca_data_2025['Solar Power'] = ca_solar_2025
pp_ca_data_2025['Wind Power'] = ca_wind_2025
pc_ca_2025=np.zeros((len(pp_ca_data_2025),6))

pp_ca_data_2030 = pd.DataFrame(columns = column_names)
pp_ca_data_2030['Price'] = ca_price_2030
pp_ca_data_2030['CO2 Emissions'] = ca_co2_2030
pp_ca_data_2030['Load'] = ca_load_2030
pp_ca_data_2030['Hydropower'] = ca_hydro_2030
pp_ca_data_2030['Solar Power'] = ca_solar_2030
pp_ca_data_2030['Wind Power'] = ca_wind_2030
pc_ca_2030=np.zeros((len(pp_ca_data_2030),6))

pp_ca_data_2035 = pd.DataFrame(columns = column_names)
pp_ca_data_2035['Price'] = ca_price_2035
pp_ca_data_2035['CO2 Emissions'] = ca_co2_2035
pp_ca_data_2035['Load'] = ca_load_2035
pp_ca_data_2035['Hydropower'] = ca_hydro_2035
pp_ca_data_2035['Solar Power'] = ca_solar_2035
pp_ca_data_2035['Wind Power'] = ca_wind_2035
pc_ca_2035=np.zeros((len(pp_ca_data_2035),6))

pp_ca_data_2040 = pd.DataFrame(columns = column_names)
pp_ca_data_2040['Price'] = ca_price_2040
pp_ca_data_2040['CO2 Emissions'] = ca_co2_2040
pp_ca_data_2040['Load'] = ca_load_2040
pp_ca_data_2040['Hydropower'] = ca_hydro_2040
pp_ca_data_2040['Solar Power'] = ca_solar_2040
pp_ca_data_2040['Wind Power'] = ca_wind_2040
pc_ca_2040=np.zeros((len(pp_ca_data_2040),6))

pp_ca_data_2045 = pd.DataFrame(columns = column_names)
pp_ca_data_2045['Price'] = ca_price_2045
pp_ca_data_2045['CO2 Emissions'] = ca_co2_2045
pp_ca_data_2045['Load'] = ca_load_2045
pp_ca_data_2045['Hydropower'] = ca_hydro_2045
pp_ca_data_2045['Solar Power'] = ca_solar_2045
pp_ca_data_2045['Wind Power'] = ca_wind_2045
pc_ca_2045=np.zeros((len(pp_ca_data_2045),6))

pp_ca_data_2050 = pd.DataFrame(columns = column_names)
pp_ca_data_2050['Price'] = ca_price_2050
pp_ca_data_2050['CO2 Emissions'] = ca_co2_2050
pp_ca_data_2050['Load'] = ca_load_2050
pp_ca_data_2050['Hydropower'] = ca_hydro_2050
pp_ca_data_2050['Solar Power'] = ca_solar_2050
pp_ca_data_2050['Wind Power'] = ca_wind_2050
pc_ca_2050=np.zeros((len(pp_ca_data_2050),6))

pp_pnw_data_2020 = pd.DataFrame(columns = column_names)
pp_pnw_data_2020['Price'] = pnw_price_2020
pp_pnw_data_2020['CO2 Emissions'] = pnw_co2_2020
pp_pnw_data_2020['Load'] = pnw_load_2020
pp_pnw_data_2020['Hydropower'] = pnw_hydro_2020
pp_pnw_data_2020['Solar Power'] = pnw_solar_2020
pp_pnw_data_2020['Wind Power'] = pnw_wind_2020
pc_pnw_2020=np.zeros((len(pp_pnw_data_2020),6))

pp_pnw_data_2025 = pd.DataFrame(columns = column_names)
pp_pnw_data_2025['Price'] = pnw_price_2025
pp_pnw_data_2025['CO2 Emissions'] = pnw_co2_2025
pp_pnw_data_2025['Load'] = pnw_load_2025
pp_pnw_data_2025['Hydropower'] = pnw_hydro_2025
pp_pnw_data_2025['Solar Power'] = pnw_solar_2025
pp_pnw_data_2025['Wind Power'] = pnw_wind_2025
pc_pnw_2025=np.zeros((len(pp_pnw_data_2025),6))

pp_pnw_data_2030 = pd.DataFrame(columns = column_names)
pp_pnw_data_2030['Price'] = pnw_price_2030
pp_pnw_data_2030['CO2 Emissions'] = pnw_co2_2030
pp_pnw_data_2030['Load'] = pnw_load_2030
pp_pnw_data_2030['Hydropower'] = pnw_hydro_2030
pp_pnw_data_2030['Solar Power'] = pnw_solar_2030
pp_pnw_data_2030['Wind Power'] = pnw_wind_2030
pc_pnw_2030=np.zeros((len(pp_pnw_data_2030),6))

pp_pnw_data_2035 = pd.DataFrame(columns = column_names)
pp_pnw_data_2035['Price'] = pnw_price_2035
pp_pnw_data_2035['CO2 Emissions'] = pnw_co2_2035
pp_pnw_data_2035['Load'] = pnw_load_2035
pp_pnw_data_2035['Hydropower'] = pnw_hydro_2035
pp_pnw_data_2035['Solar Power'] = pnw_solar_2035
pp_pnw_data_2035['Wind Power'] = pnw_wind_2035
pc_pnw_2035=np.zeros((len(pp_pnw_data_2035),6))

pp_pnw_data_2040 = pd.DataFrame(columns = column_names)
pp_pnw_data_2040['Price'] = pnw_price_2040
pp_pnw_data_2040['CO2 Emissions'] = pnw_co2_2040
pp_pnw_data_2040['Load'] = pnw_load_2040
pp_pnw_data_2040['Hydropower'] = pnw_hydro_2040
pp_pnw_data_2040['Solar Power'] = pnw_solar_2040
pp_pnw_data_2040['Wind Power'] = pnw_wind_2040
pc_pnw_2040=np.zeros((len(pp_pnw_data_2040),6))

pp_pnw_data_2045 = pd.DataFrame(columns = column_names)
pp_pnw_data_2045['Price'] = pnw_price_2045
pp_pnw_data_2045['CO2 Emissions'] = pnw_co2_2045
pp_pnw_data_2045['Load'] = pnw_load_2045
pp_pnw_data_2045['Hydropower'] = pnw_hydro_2045
pp_pnw_data_2045['Solar Power'] = pnw_solar_2045
pp_pnw_data_2045['Wind Power'] = pnw_wind_2045
pc_pnw_2045=np.zeros((len(pp_pnw_data_2045),6))

pp_pnw_data_2050 = pd.DataFrame(columns = column_names)
pp_pnw_data_2050['Price'] = pnw_price_2050
pp_pnw_data_2050['CO2 Emissions'] = pnw_co2_2050
pp_pnw_data_2050['Load'] = pnw_load_2050
pp_pnw_data_2050['Hydropower'] = pnw_hydro_2050
pp_pnw_data_2050['Solar Power'] = pnw_solar_2050
pp_pnw_data_2050['Wind Power'] = pnw_wind_2050
pc_pnw_2050=np.zeros((len(pp_pnw_data_2050),6))

###############################################################################

#Take percentiles of each column and load into new dataframes
for j in range(6):
    for i in range(len(pp_ca_data_2020)):
        pc_ca_2020[i,j] = stats.percentileofscore(pp_ca_data_2020.values[:,j], pp_ca_data_2020.values[i,j])


###############################################################################
        
pc_ca_2020_df = pd.DataFrame(pc_ca_2020, columns = column_names)


pc_ca_2020_df['Rank'] = pc_ca_2020_df['Price']


#Create parallel plots for each year, for CA and PNW ###RERUN FIRST BLOCK TO 2045
# 0000ff = blue, e6004c = red, 00cc99 = green, ffa31a = orange
plt.style.use('seaborn-white')
plt.figure()
parallel_coordinates(pc_ca_2020_df.sort_values(by='Price'),'Rank',colormap=cmap)
#parallel_coordinates(pc_ca_2020_df[pc_ca_2020_df['Dataset']=='None'],'Dataset',color=('#c9c9c9'))
#parallel_coordinates(pc_ca_2020_df[pc_ca_2020_df['Dataset']=='Low'],'Dataset',color=('#0000ff'))
#parallel_coordinates(pc_ca_2020_df[pc_ca_2020_df['Dataset']=='High'],'Dataset',color=('#ffa31a'))
#parallel_coordinates(pc_ca_2020_df2_low,'Dataset',color=('#00cc99'),lw=3)  
#parallel_coordinates(pc_ca_2020_df2_high,'Dataset',color=('#e6004c'),lw=3)       
#plt.legend(loc = 'upper left', fontsize = 'large', bbox_to_anchor=(1.05, 1))
plt.legend('')
plt.annotate('${}'.format(str(np.round(np.max(ca_price_2020),2))),(-1,98),annotation_clip=False, fontweight='black')
plt.annotate('${}'.format(str(np.round(np.min(ca_price_2020),2))),(-1,-2),annotation_clip=False,fontweight='black')
plt.ylabel('Percentile')
plt.title('{}2020 California Parallel Plot'.format(path))
plt.savefig('figs/parallel_cmap_{}ca_2020.png'.format(path), bbox_inches='tight',dpi=d)
plt.clf()

