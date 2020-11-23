# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 09:43:52 2020

@author: mzeigha
"""


from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

scenarios = ['CO2','no_tax','SNP', 'all_tax']
average = np.zeros(4) 
for s in range (4):
    
    filename = scenarios[s] + '/CA0/shadow_price.csv'
    shadow_price = pd.read_csv(filename,header=0,index_col=0)
    
    shadow_price = shadow_price[shadow_price.Value < 150]
    average[s] = shadow_price['Value'].mean()
    
plt.figure()         
plt.bar([0,1,2,3],average)
plt.title('Average Shadow Price')
plt.xticks([0,1,2,3], scenarios , rotation=90)
plt.ylabel('Average Price ($)')
plt.savefig('fig12.png',bbox_inches= "tight", dpi=500)
    
