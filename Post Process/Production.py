# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:14:38 2021

@author: mzeigha
"""

import pandas as pd
import numpy as np

production_df_all_tax = pd.read_csv ('Production/production_df_all_tax.csv').drop(columns = ['Year'])
# production_df_CO2 = pd.read_csv ('Production/production_df_CO2.csv').drop(columns = ['Year'])
# production_df_no_tax = pd.read_csv ('Production/production_df_no_tax.csv').drop(columns = ['Year'])
# production_df_SNP = pd.read_csv ('Production/production_df_SNP.csv').drop(columns = ['Year'])

Total_Cap = 33759.32

# Total generation
production_df_all_tax['Total_generation'] = production_df_all_tax.sum(axis=1)
# production_df_CO2['Total_generation'] = production_df_CO2.sum(axis=1)
# production_df_no_tax['Total_generation'] = production_df_no_tax.sum(axis=1)
# production_df_SNP['Total_generation'] = production_df_SNP.sum(axis=1)


# Slack
production_df_all_tax['Slack'] = production_df_all_tax['SLACK1'] + production_df_all_tax['SLACK2'] + production_df_all_tax['SLACK3'] + production_df_all_tax['SLACK4']
# production_df_CO2['Slack'] = production_df_CO2['SLACK1'] + production_df_CO2['SLACK2'] + production_df_CO2['SLACK3'] + production_df_CO2['SLACK4']
# production_df_no_tax['Slack'] = production_df_no_tax['SLACK1'] + production_df_no_tax['SLACK2'] + production_df_no_tax['SLACK3'] + production_df_no_tax['SLACK4']
# production_df_SNP['Slack'] = production_df_SNP['SLACK1'] + production_df_SNP['SLACK2'] + production_df_SNP['SLACK3'] + production_df_SNP['SLACK4']

# Imports
production_df_all_tax['Imports'] = production_df_all_tax['P46I_SCE'] + production_df_all_tax['P46I_SDGE'] 
+ production_df_all_tax['P66I'] + production_df_all_tax['P61I'] +production_df_all_tax['P45I']
+ production_df_all_tax['P24I'] + production_df_all_tax['P42I'] 

# production_df_CO2['Imports'] = production_df_CO2['P46I_SCE'] + production_df_CO2['P46I_SDGE'] 
# + production_df_CO2['P66I'] + production_df_CO2['P61I'] +production_df_CO2['P45I']
# + production_df_CO2['P24I'] + production_df_CO2['P42I'] 

# production_df_no_tax['Imports'] = production_df_no_tax['P46I_SCE'] + production_df_no_tax['P46I_SDGE'] 
# + production_df_no_tax['P66I'] + production_df_no_tax['P61I'] +production_df_no_tax['P45I']
# + production_df_no_tax['P24I'] + production_df_no_tax['P42I'] 

# production_df_SNP['Imports'] = production_df_SNP['P46I_SCE'] + production_df_SNP['P46I_SDGE'] 
# + production_df_SNP['P66I'] + production_df_SNP['P61I'] +production_df_SNP['P45I']
# + production_df_SNP['P24I'] + production_df_SNP['P42I'] 


# Hydro
production_df_all_tax['Hydro'] = production_df_all_tax['SCE_hydro'] + production_df_all_tax['PGEV_hydro']
# production_df_CO2['Hydro'] = production_df_CO2['SCE_hydro'] + production_df_CO2['PGEV_hydro']
# production_df_no_tax['Hydro'] = production_df_no_tax['SCE_hydro'] + production_df_no_tax['PGEV_hydro']
# production_df_SNP['Hydro'] = production_df_SNP['SCE_hydro'] + production_df_SNP['PGEV_hydro']

# PSH
production_df_all_tax['PSH'] = production_df_all_tax['HELMS_PS'] + production_df_all_tax['EASTWOOD_PS'] + production_df_all_tax['HODGES_PS']
# production_df_CO2['PSH'] = production_df_CO2['HELMS_PS'] + production_df_CO2['EASTWOOD_PS'] + production_df_CO2['HODGES_PS']
# production_df_no_tax['PSH'] = production_df_no_tax['HELMS_PS'] + production_df_no_tax['EASTWOOD_PS'] + production_df_no_tax['HODGES_PS']
# production_df_SNP['PSH'] = production_df_SNP['HELMS_PS'] + production_df_SNP['EASTWOOD_PS'] + production_df_SNP['HODGES_PS']

# Working percentage
production_df_all_tax['In_service'] = production_df_all_tax['Total_generation']/Total_Cap
# production_df_CO2['In_service'] = production_df_CO2['Total_generation']/Total_Cap
# production_df_no_tax['In_service'] = production_df_no_tax['Total_generation']/Total_Cap
# production_df_SNP['In_service'] = production_df_SNP['Total_generation']/Total_Cap



# >0.6 of capacity in service

all_tax = production_df_all_tax[production_df_all_tax['In_service'] >.9]
# CO2 = production_df_CO2[production_df_CO2['In_service'] >.6]
# no_tax = production_df_no_tax[production_df_no_tax['In_service'] >.6]
# SNP = production_df_SNP[production_df_SNP['In_service'] >.6]


# all_tax.to_csv ('Productionall_tax.csv', header=True) 
# CO2.to_csv ('ProductionCO2.csv', header=True) 
# no_tax.to_csv ('Productionno_tax.csv', header=True) 
# SNP.to_csv ('ProductionSNP.csv', header=True) 