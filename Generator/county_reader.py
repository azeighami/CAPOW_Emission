# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:07:34 2022

@author: mzeigha
"""

import pandas as pd
import numpy as np


egrid = pd.read_csv('eGRID Plants.csv', dtype = str)
gen = pd.read_csv('generator_final_DOE.csv')


#%%
for i in gen.index:
    a = egrid[egrid['ORISPL']==str(gen.loc[i,'DOE'])]
    
    
    try:
        gen.loc[i,'county2'] = a.iloc[0,16] + a.iloc[0,17]
    except Exception:
        pass
        
