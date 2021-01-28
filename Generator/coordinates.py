# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:49:37 2020

@author: mzeigha
"""


import pandas as pd



eGRID = pd.read_csv ('eGRID Plants.csv' , index_col = 0)
generator = pd.read_csv("generator_final_DOE.csv")


for i in generator.index:
    for j in eGRID.index:
        if generator.loc[i,'DOE'] == eGRID.loc[j,'ORISPL']:
            generator.loc[i,'FIPSCNTY'] = eGRID.loc[j,'FIPSCNTY']
            generator.loc[i,'CNTYNAME'] = eGRID.loc[j,'CNTYNAME']

          
            
generator.to_csv (r'generator_final_DOE.csv', index = False, header=True)