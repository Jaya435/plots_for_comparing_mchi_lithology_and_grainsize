# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:57:16 2018

@author: s1217815
"""

import matplotlib
matplotlib.use("Agg")                                                                                                          

import matplotlib.pyplot as plt
import pandas as pd




#reads csv file relating to basin data
df = pd.read_csv("t:\\lithology_python\\corsica_PP_chi_data_0.45.csv")
print(df.columns.values)
#change these values depending on which basins you are interested in
fango = df[df["basin_key"]==50]
taravo= df[df["basin_key"]==94]
tavig = df[df["basin_key"]==62]
n=["Fango","Taravo","Tavignano"]

z=0 #used for saving filenames
sp=221 #used for denoting which plot


#iterating through each basin
for x in (fango,taravo,tavig):
    
    #disects the data into sections relating to indicidual lithologies
    df_1=x[x["corsica_PP_geol"]==1] #Siliclastic
    df_2=x[x["corsica_PP_geol"]==2] #volcano
    df_3=x[x["corsica_PP_geol"]==3] #grantic
    df_4=x[x["corsica_PP_geol"]==4] #rhyolitic
    df_5=x[x["corsica_PP_geol"]==5] #alluvium
    df_6=x[x["corsica_PP_geol"]==6] #silicasltic and chemical
    df_7=x[x["corsica_PP_geol"]==7] #ultramafic
    df_8=x[x["corsica_PP_geol"]==8] #metamorphic
    df_9=x[x["corsica_PP_geol"]==9] #carbonatic
    #chooses which data to plot
    data_to_plot = [df_1["m_chi"],df_2["m_chi"],df_3["m_chi"],df_4["m_chi"], df_5["m_chi"],df_6["m_chi"],df_7["m_chi"],df_8["m_chi"],df_9["m_chi"]]
    #data_to_plot = [df_3["m_chi"],df_4["m_chi"],df_8["m_chi"]]
    
    
    rock_type = ["Siliclastic", "Volcano \nSequence", "Granitic", "Rhyolitic", "Alluvium","Siliclastic\n and Chemical","Ultramafic", "Metamorphic", "Carbonatic"]
    #rock_type = ["Granitic", "Rhyolitic", "Metamorphic"]
    

    #((ax1),(ax2),(ax3)) = axes
    fig=plt.figure(1,figsize=(11.69,8.27))
    fig.subplots_adjust(top=0.92, left=0.07, right=0.97,
                    hspace=0.3, wspace=0.3)
    ax=fig.add_subplot(sp)

    bp=ax.boxplot(data_to_plot,patch_artist=True)
    ax.set_xticklabels(rock_type,rotation='45',fontsize=11)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_ylabel('M_$\chi$',fontsize=20,rotation='90')
    ax.set_ylim([0,600])
    
## change outline color, fill color and linewidth of the boxes
    for box in bp['boxes']:
# change outline color
        box.set( color='#7570b3', linewidth=2)
# change fill color
        box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)
    #fig.savefig(str(n[z])+'_boxplot_all_corse.png',bbox_inches='tight') 
    
   
    z=z+1
    sp=sp+1
plt.savefig('all_litho_boxplot_all_corse.png',bbox_inches='tight')