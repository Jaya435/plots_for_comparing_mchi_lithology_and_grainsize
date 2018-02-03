# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 10:46:24 2017

@author: s1217815
"""

from __future__ import division

import numpy as np

import matplotlib.pyplot as plt

import os

def suplabel(axis,label,label_prop=None,
             labelpad=5,
             ha='center',va='center'):
    ''' Add super ylabel or xlabel to the figure
    Similar to matplotlib.suptitle
    axis       - string: "x" or "y"
    label      - string
    label_prop - keyword dictionary for Text
    labelpad   - padding from the axis (default: 5)
    ha         - horizontal alignment (default: "center")
    va         - vertical alignment (default: "center")
    '''
    fig = plt.gcf()
    xmin = []
    ymin = []
    for ax in fig.axes:
        xmin.append(ax.get_position().xmin)
        ymin.append(ax.get_position().ymin)
    xmin,ymin = min(xmin),min(ymin)
    dpi = fig.dpi
    if axis.lower() == "y":
        rotation=90.
        x = xmin-float(labelpad)/dpi
        y = 0.5
    elif axis.lower() == 'x':
        rotation = 0.
        x = 0.5
        y = ymin - float(labelpad)/dpi
    else:
        raise Exception("Unexpected axis: x or y")
    if label_prop is None: 
        label_prop = dict()
    plt.text(x,y,label,rotation=rotation,fontsize=22,
               transform=fig.transFigure,
               ha=ha,va=va,
               **label_prop)

y = (50,50,50,50)
y2 = np.linspace(0,84,4)
y3 = np.linspace(0,50,4)
y4 = (84,84,84,84)
#empty arrays to be modified
median_gsd50e=[]
median_gsd50g=[]
median_gsd84e=[]
median_gsd84g=[]
d50eplus=[]
d50eminus=[]
d84eplus=[]
d84eminus=[]
labels=[]
#insert your own txt files continaing GSD information here
for fname2 in ('c0504.txt', 'c0501.txt','c0602.txt', 'c0603.txt', 'c0604.txt', 'c0703.txt', 'c0705.txt'):
    data=np.loadtxt(fname2)
    filename=os.path.splitext(fname2) 
    dphie=data[:,2] # = grain size of ERDAS imagine grain size data data
    cumule=data[:,4] # = cumulative percentage for the erdas imagine GSD
    dphig=data[:,6] # = grain size of transect data
    cumulg=data[:,8] #= cumulative percentage of transect GSD
    dphieplus=[] #array will be created for max error
    dphieminus=[] #array will be created for min error
    ind=[]
    cumuleplus=[]  #positive error on photometric
    cumuleminus=[] #negative error on photometic
    #following code to find the maximum value of an array and then values
    #within 0.1 of said value. 
    #Then finds the index and the corresponding
    #cumulative percentage value so it can be plotted.
    #it does the same for the minimum value as well 
    #lines are then plotted either side of the main curve as grey dashed lines
    #in order to show the range on the data

    max_dphie=np.max(dphie)
    
    for x in (dphie):
        if (max_dphie - 0.2) < x < (max_dphie+0.2):
            dphieplus.append(x)
    
    a=np.array(dphie)
    b=np.array(dphieplus)
    dphieplus= np.append(a,b)
    dphieplus=sorted(dphieplus)
    t=len(dphieplus)
    for i in range(1,t+1):
        r=(i / t)*100
        cumuleplus.append(r)
    cumuleplus=list(reversed(cumuleplus))
    dphieplus=list(reversed(dphieplus))
    
    dphieminus= [x for x in a if x not in b]
    dphieminus=sorted(dphieminus)
    s=len(dphieminus)
    for j in range(1,s+1):
        v=(j / s)*100
        cumuleminus.append(v)
    cumuleminus=list(reversed(cumuleminus))
    dphieminus=list(reversed(dphieminus))
    fig = plt.figure(figsize=(15,10))
    #plot of photometric methods with the range included on the data
    max_value = plt.plot(dphieplus,cumuleplus,'k-.',linewidth=4)  
    reality = plt.plot(dphie,cumule,linewidth=6,label='Photometric grain size')
    min_value = plt.plot(dphieminus,cumuleminus,'k-.',linewidth=4)
    
    plt.plot(dphig,cumulg,'--',linewidth=6, label='Transect grain size')
    testD84 = 1
    testD50=1
    #next bit of code is used to calculate the D50 and D84 median grain sizes.
    for i in range(len(dphie)):
        if cumule[i]<=84 and testD84==1:
            D84=((84-cumule[i])*(dphie[i-1]-dphie[i])/(cumule[i-1]-cumule[i]))+dphie[i]
            testD84=0
        elif cumule[i]<=50 and testD50==1:
            D50=((50-cumule[i])*(dphie[i-1]-dphie[i])/(cumule[i-1]-cumule[i]))+dphie[i]
            testD50=0
    testD84=1
    testD50=1
    for i in range(len(dphieplus)):
        if cumuleplus[i]<=84 and testD84==1:
            D84plus=((84-cumuleplus[i])*(dphieplus[i-1]-dphieplus[i])/(cumuleplus[i-1]-cumuleplus[i]))+dphieplus[i]
            testD84=0
        elif cumuleplus[i]<=50 and testD50==1:
            D50plus=((50-cumuleplus[i])*(dphieplus[i-1]-dphieplus[i])/(cumuleplus[i-1]-cumuleplus[i]))+dphieplus[i]
            testD50=0
    testD84=1
    testD50=1
    for i in range(len(dphieminus)):
        if cumuleminus[i]<=84 and testD84==1:
            D84minus=((84-cumuleminus[i])*(dphieminus[i-1]-dphieminus[i])/(cumuleminus[i-1]-cumuleminus[i]))+dphieminus[i]
            testD84=0
        elif cumuleminus[i]<=50 and testD50==1:
            D50minus=((50-cumuleminus[i])*(dphieminus[i-1]-dphieminus[i])/(cumuleminus[i-1]-cumuleminus[i]))+dphieminus[i]
            testD50=0
        testgD84 = 1
        testgD50 = 1 
    for i in range(len(dphig)):
        if cumulg[i]<=84 and testgD84==1:
            D84g=((84-cumulg[i])*(dphig[i-1]-dphig[i])/(cumulg[i-1]-cumulg[i]))+dphig[i]
            testgD84=0
        elif cumulg[i]<=50 and testgD50==1:
            D50g=((50-cumulg[i])*(dphig[i-1]-dphig[i])/(cumulg[i-1]-cumulg[i]))+dphig[i]
            testgD50=0
    testD84 = 1
    testD50=1
    plt.plot(D84,84,'bo',label='Photometric D84 = '+str(round(D84,3)))
    plt.plot(D50,50,'ro',label='Photometric D50 = '+str(round(D50,3)))
    m50ea = np.linspace(0,D50,4)
    m84ea = np.linspace(0,D84,4)
    m84ed = (D84,D84,D84,D84)
    m50ed = (D50,D50,D50,D50)
    m50ga = np.linspace(0,D50g,4)
    m84ga = np.linspace(0,D84g,4)
    m84gd = (D84g,D84g,D84g,D84g)
    m50gd = (D50g,D50g,D50g,D50g)
    #this code plots both types of GSDs, however I would like to include error bars
    #and shows where the median and D84 values correspond to
    plt.plot(D84g,84,'go',label='Transect D84 = '+str(round(D84g,3)))
    plt.plot(D50g,50,'ko',label='Transect D50 = '+str(round(D50g,3)))
    plt.plot(m50ea,y,'r--',linewidth=4)
    plt.plot(m50ga,y,'k--',linewidth=4)
    plt.plot(m50gd,y3,'k--',linewidth=4)
    plt.plot(m50ed,y3,'r--',linewidth=4)
    plt.plot(m84ea,y4,'b--',linewidth=4)
    plt.plot(m84ga,y4,'g--',linewidth=4)
    plt.plot(m84ed,y2,'b--',linewidth=4)
    plt.plot(m84gd,y2,'g--',linewidth=4)
    plt.legend(loc=2, prop={'size': 25})
    plt.yticks(np.arange(0,110,10),fontsize=40)
    plt.xticks(fontsize=40)
    plt.xlabel('Grain size (-phi)', fontsize=40)
    plt.ylabel('Percentage finer than...', fontsize=40)
    plt.savefig(filename[0]+'.png', bbox_inches='tight')
    plt.close()
    #next section creates arrays for plotting a combined graph with errorbars
    median_gsd50e.append(D50)
    median_gsd84e.append(D84)
    d50eplus.append(D50plus)
    d84eplus.append(D84plus)
    d50eminus.append(D50minus)
    d84eminus.append(D84minus)
    median_gsd50g.append(D50g)
    median_gsd84g.append(D84g)
    labels.append(filename[0])


yerr50=list(zip(d50eminus,d50eplus))
yerr84=list(zip(d84eminus,d84eplus))
yerr50=np.array(yerr50)
yerr84=np.array(yerr84)
f=np.array(median_gsd50e)
g=np.array(median_gsd84e) 
top50=(d50eplus-f)
bot50=abs(d50eminus-f)
top84=(d50eplus-g)
bot84=(d50eminus-g)
yerr50=np.array(yerr50).T
yerr84=np.array(yerr84).T  


fig = plt.figure(figsize=(18,8))
#loads the distance upstream where GSD was recorded
data2=np.loadtxt('taravo_distance_downstream.txt',skiprows=1)
#plots grain size for the photometric method, no error on data
ax1 = plt.subplot(311)
mgsd50g = ax1.scatter(data2,median_gsd50g,c='g',marker='o',s=25)
mgs84g = ax1.scatter(data2,median_gsd84g,c='r',marker='o',s=25)
for label, x, y in zip(labels, data2, median_gsd50g):
    plt.annotate(
    label,
    xy=(x, y), xytext=(20, -20),
    textcoords='offset points', ha='right', va='bottom',
    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
    arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.scatter(data2,median_gsd50g,s=0,c='r',marker='D')
ax2 = plt.subplot(312,sharex=ax1, sharey=ax1)
#median GSD for the photometric method with errorbars
mgsd50e = ax2.errorbar(data2,f, yerr=[(bot50),(top50)],fmt='r.',label='Photometric D50',ms=8,marker='x')
ax = plt.subplot(313, sharex=ax1, sharey=ax1)
#D84 GSD for the photometric method
mgs84e = ax.errorbar(data2,g, yerr=[(bot84),(top84)],fmt='b.',label='Photometric D84',ms=8,marker='x')

ax1.legend((mgsd50g,mgs84g),
          ('Transect D50','Transect D84'),
            scatterpoints=1,loc='lower right', 
            ncol=1,prop={'size': 16},shadow=True)
legend2 = ax2.legend(loc='upper left', shadow=True,prop={'size': 16})            
legend=ax.legend(loc='upper left', shadow=True,prop={'size': 16})  
plt.setp(ax.get_xticklabels(), fontsize=20)
plt.setp(ax.get_yticklabels(), fontsize=16)
plt.setp(ax1.get_xticklabels(), visible=False)
plt.setp(ax1.get_yticklabels(), fontsize=16)             
plt.setp(ax2.get_xticklabels(), visible=False)  
plt.setp(ax2.get_yticklabels(), fontsize=16) 
xmax=np.max(data2)
xmin=0
plt.xlim(xmin-(xmax*0.01),xmax+(xmax*0.01))
plt.xlabel('Distance upstream from outlet (m)', fontsize=22)
suplabel("y",'Grain size (-phi)',labelpad=2.5) 
plt.subplots_adjust(wspace=0.1, hspace=0.1)
fig1 = plt.gcf()
fig1.savefig('Taravo_median2.png', dpi=100,bbox_inches='tight',pad_inches=0.7)
#produces a table with the median and D84 information containted within
median_table =  np.column_stack((data2,bot50,f, top50,bot84,g, top84,median_gsd50g,median_gsd84g))
np.savetxt('taravo_median_table.txt',median_table,delimiter=' ')



