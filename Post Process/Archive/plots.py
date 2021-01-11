# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:33:47 2020

@author: YSu
"""

#%% Boxplot

fig,ax=plt.subplots()
bp=ax.boxplot(Average_rate_2018,showfliers=False, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#4098db', linewidth=2)
    # change fill color
    box.set( facecolor = '#4098db' )
#
### change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#4098db', linewidth=2)
#
### change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#4098db', linewidth=2)
#
### change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#00f2ff', linewidth=2)

ax2=ax.twinx()

ax2.plot(range(1,21),Coefficient_of_variance_2018,color='#4098db')
ax2.set_ylim(0.03,0.0525)
ax.patch.set_edgecolor('black')  
ax.patch.set_linewidth('1') 
#ax2.plot(range(1,21),Co
#%% Probablistic distribution 

def process(data):
    
    

    means = np.median(data,axis=1)
    std=data.std(1)
    perc=np.zeros((2,363))
    for i in range(0,363):
    
        perc[0,i]=means[i]-np.percentile(data[i,:],25)
        perc[1,i]=np.percentile(data[i,:],75)-means[i]


    colormap = cm.RdBu_r # change this for the colormap of choice
    percentiles = [0,1,5,10,25,50,75,90,95,99,100]
    
    half = int((len(percentiles)-1)/2)
    L = int(len(percentiles))
    
    SDist=np.zeros((363,L))
    for i in range(L):
        for t in range(363):
          SDist[t,i]=np.percentile(data[t,:],percentiles[i])
    SDist[:,5]=means
    
    return half,percentiles,colormap,SDist,std

half,percentiles,colormap,SDist,std=process(hist)
half_syn,percentiles_syn,colormap_syn,SDist_syn,std_syn=process(syn)


plt.rcParams['font.weight']='bold'

plt.figure()
ax1=plt.subplot2grid((1,2),(0,0))
ax2=plt.subplot2grid((1,2),(0,1))
#ax3=plt.subplot2grid((2,2),(0,1),rowspan=1)

ax2.plot(np.arange(0,363,1), SDist_syn[:,half],color='black',label='Median')
for i in range(len(percentiles)-1):
    if i <6:
        index= str(percentiles_syn[i-1]) + ' percentiles'
    else:
        index= str(percentiles_syn[i+1]) + ' percentiles'
    ax2.fill_between(np.arange(0,363,1), SDist_syn[:,i],SDist_syn[:,i+1],color=colormap_syn(i/len(percentiles)),label= index)
    
    



#ax1.set_facecolor('white')
plt.style.use('seaborn-paper')


ax1.plot(np.arange(0,363,1), SDist[:,half],color='black',label='Median')
for i in range(len(percentiles)-1):

    if i <5:
        index= str(percentiles_syn[i]) + ' percentiles'
    else:
        index= str(percentiles_syn[i+1]) + ' percentiles'
    ax1.fill_between(np.arange(0,363,1), SDist[:,i],SDist[:,i+1],color=colormap(i/len(percentiles)),label= index)

#ax1.set_title("SampleData", fontsize=15)
ax1.tick_params(labelsize=14)
#ax2.set_xlabel('Day of the year', fontsize=15,fontweight='bold')
ax1.set_visible(True)
ax1.set_ylim(0,100)
ax1.legend(loc='best', bbox_to_anchor=(0.75, 1.1),ncol=2, fancybox=True, shadow=True,fontsize='medium')

ax2.set_facecolor('white')
plt.style.use('seaborn-paper')

ax2.set_ylim(0,100)

ax2.tick_params(labelsize=14)


ax1.set_facecolor('white')



#%% Parallel plots


from scipy import stats     
pc_data=np.zeros((1188,7))      

for i in range(1188):
    for j in range(7):
        pc_data[i,j]=stats.percentileofscore(raw_df.values[:,j],raw_df.values[i,j])
column_names=['Price','Emission','Temperature','Streamflow CA','Streamflow PNW','Irradiance','Windspeed']

pc_df=pd.DataFrame(pc_data,columns=column_names)

for i in range(1188):
    if pc_df.loc[i,'Price']<=5:
        pc_df.loc[i,'Dataset']='Low'
    elif pc_df.loc[i,'Price']>=95:
        pc_df.loc[i,'Dataset']='High'
    else:
        pc_df.loc[i,'Dataset']='None'

pc_df_high=pc_df.loc[pc_df['Dataset']== 'High'] 
pc_df_low=pc_df.loc[pc_df['Dataset']== 'Low'] 

pc_df2=pd.DataFrame(pc_data,columns=column_names)

for i in range(1188):
    if pc_df2.loc[i,'Price']<=0.09:
        pc_df2.loc[i,'Dataset']='Lowest'
    elif pc_df2.loc[i,'Price']>=100:
        pc_df2.loc[i,'Dataset']='Highest'
    else:
        pc_df2.loc[i,'Dataset']='None'
        
pc_df2_high=pc_df2.loc[pc_df2['Dataset']== 'Highest'] 
pc_df2_low=pc_df2.loc[pc_df2['Dataset']== 'Lowest'] 
from pandas.plotting import parallel_coordinates
plt.style.use('seaborn-white')
plt.figure()
parallel_coordinates(pc_df,'Dataset',color=('#ffa31a', '#4d4d4d10','#0000ff','#e6004c','#00cc99'))
parallel_coordinates(pc_df2_high,'Dataset',color=('#00cc99'),lw=6)   
parallel_coordinates(pc_df2_low,'Dataset',color=('#e6004c'),lw=6)      
plt.legend([])