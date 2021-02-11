# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:40:51 2019

@author: jkern
"""

import numpy as np
import pandas as pd


#% Formulates piecewise linear approximizations of power plant cost functions
#% based on average heat rate data from EPA eGRID (2014), an NREL report
#% (Lew, D. et al. Wind and Solar Impacts on Fossil-fuel Generators (2012), and some 
#% plant specific data from units in CAISO (Klein report). 

# Heat rate profiles
P=pd.read_excel('heat_rate_curves.xlsx',sheet_name='new_prof')

#Read eGRID data
units = pd.read_excel('generator_final.xlsx',header=0)

#Avg. heat rate curves for each power plant
A_HR = np.zeros((len(units),10))

#%Total fuel consumption curves for each power plant
F = np.zeros((len(units),10))

#%No Load costs
No_Load = np.zeros((len(units),1))

# heat rate curve
I_HR = np.zeros((len(units),9))

#HR segments
HR_segments = np.zeros((len(units),3))

# #match CAISO data with eGRID data
# eGRID = pd.read_excel('egrid_data.xlsx',sheet_name='CAISO',header=0)

#%Add average heat rate to zero-centered profiles
for i in range(0,len(units)):
    
    # plant_name = str(units.loc[i,'Plant name'])
    
    # #try to find unit in eGrid data
    # capfactor = units.loc[i,'Capacity Factor']

    # if capfactor < 0.3:
    #     cf = .5
    # else:
    #     cf  = capfactor
    
    cf =0.8
        
    # cf = np.round(cf,decimals=1)
    # print(plant_name, cf)
        
    if units.loc[i,'typ'] == 'ngcc':
        code = 'CC'
    elif units.loc[i,'typ'] == 'ngct':
        code = 'CT'        
    elif units.loc[i,'typ'] == 'ngst':
        code = 'ST' 
    elif units.loc[i,'typ'] == 'oil':
        code = 'CT'         

    #load appropriate heat rate curve, adjust for plant's cf
    curve = P.loc[:,code].values
    adder = curve - P.loc[P['% of Max']==cf,code].values            
    A_HR[i,:] = adder + units.loc[i,'AVG_HR']
    
#    Calculate total fuel consumption curve
    MW = np.linspace(.1,1.0,10)*units.loc[i,'netcap']
    F[i,:] = np.multiply(MW,A_HR[i,:])
    
#    % Calculate no-load costs
    p = np.polyfit(MW,F[i,:],2)
    No_Load[i] = p[2]
    
#    %Calculate incremental heat rate curve
    for j in range(0,9):
        I_HR[i,j] = (F[i,j+1]-F[i,j])/(MW[j+1]-MW[j])

    
#    %Linear function describing HR = f(MW)
    r = np.polyfit(MW[1:],I_HR[i,:],1)
    
#    %Three HR segments
    HR_segments[i,0] = r[0]*.3*units.loc[i,'netcap'] + r[1]
    HR_segments[i,1] = r[0]*.7*units.loc[i,'netcap'] + r[1]
    HR_segments[i,2] = r[0]*.9*units.loc[i,'netcap'] + r[1]


#Output
df_HR = pd.DataFrame(HR_segments)
df_HR.to_excel('HR_segments.xlsx')
df_noLoad = pd.DataFrame(No_Load)
df_noLoad.to_excel('NoLoad.xlsx')
