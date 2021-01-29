# -*- coding: utf-8 -*-

"""
Created on Mon Jan 11 14:08:02 2021

@author: mzeigha
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def process(data):

    means = np.median(data, axis= 0)
    
    ######    # colormap = cm.RdBu_r # change this for the colormap of choice
    colormap = plt.cm.RdBu_r # change this for the colormap of choice
    percentiles = [0,1,5,10,25,50,75,90,95,99,100]
    
    L = int(len(percentiles))
    
    SDist=np.zeros((365,L))
    for i in range(L):
        for t in range(365):
          SDist[t,i]=np.percentile(data[:,t],percentiles[i])
    SDist[:,5]=means
    
    half = int((len(percentiles)-1)/2)
    
    return half,percentiles,colormap,SDist

# ###############################################################################
damages = pd.read_csv('Results/SNP_damage.csv')
scenarios = ['all_tax' , 'CO2', 'no_tax', 'SNP']
scenarios_label = ['All' , 'CO2' , 'No', 'SNP']


for sen in scenarios:
    
    hist = np.array(damages[sen]).reshape((500,365))
    
    half,percentiles,colormap,SDist = process(hist)
    
    # plt.rcParams['font.weight']='bold'
    plt.figure(figsize=(20,5))
    ax1=plt.subplot2grid((1,2),(0,0))
    
    ax1.set_facecolor('white')
    plt.style.use('seaborn-paper')
    ax1.plot(np.arange(0,365,1), SDist[:,half],color='black',label='Median')
   
    for i in range(len(percentiles)-1):
    
        if i <5:
            index= str(percentiles[i]) + 'th percentile'
        else:
            index= str(percentiles[i+1]) + 'th percentile'
        ax1.fill_between(np.arange(0,365,1), SDist[:,i],SDist[:,i+1],color=colormap(i/len(percentiles)),label= index)
    
    ax1.set_xlabel('Day of the year', fontsize=14,fontweight='bold')
    ax1.set_ylabel('Damages ($)',fontsize=14,fontweight='bold')
    ax1.set_visible(True)
    ax1.legend(loc='right', bbox_to_anchor=(1.25, 0.5),ncol=1, fancybox=True, shadow=True,fontsize='medium')
    plt.style.use('seaborn-paper')
    ax1.tick_params(labelsize=12)
    ax1.set_facecolor('white')
    plt.title('Local Damage Distribution of {} Tax Scenario'.format(scenarios_label[scenarios.index(sen)]))
    plt.savefig('Plots/Local Damage Distribution of {} scenario.png'.format(sen) , bbox_inches='tight',dpi=250)