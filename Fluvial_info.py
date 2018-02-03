# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:05:26 2017

@author: s1217815
"""

import numpy as np

import matplotlib.pyplot as plt

import os


import math

for fname in ('Fango.txt','Taravo.txt','Tavignano.txt'):
    data=np.loadtxt(fname)
    filename=os.path.splitext(fname)
    distance=data[:,3]
    elevation=data[:,4]
    
    location_distance= data[:,11]
    location_elevation= data[:,12]
    location_active = data[:,18]
    location_bankfull = data[:,19]
    location_slope = data[:,17]
    
    
    xmax=np.max(distance)
    ymax=np.max(elevation)
    plt.ylim((0,ymax+(ymax/10)))
    plt.xlim((0,xmax+100))
    plt.plot(distance,elevation,'b-',linewidth=2,zorder=1)
    plt.scatter(location_distance,location_elevation,c='yellow',marker='D',s=50,zorder=2)
    plt.xlabel('Distance upstream from outlet (m)', fontsize=20)
    plt.ylabel('Elevation (m)', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    
    plt.savefig(filename[0]+'_Long_Profile.png', bbox_inches='tight')
    
    plt.close()
    #remove all values == 0 and then plot for drainage area
    data[ data==0 ] = np.nan
    drainage=data[:,6]
    distance=data[:,3]
    location_drainage= data[:,14] 
    plt.plot(distance,drainage, 'b-', linewidth=2,zorder=1)
    plt.scatter(location_distance,location_drainage,c='yellow',marker='D',s=50,zorder=2)
    plt.xlabel('Distance upstream from outlet (m)', fontsize=20)
    plt.ylabel('Drainage area ($m^2$)',fontsize=20)
    xmin=np.min(distance)
    xmax=np.max(distance)
    ymax=np.max(drainage)
    ymin=np.min(drainage)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=20)
    plt.autoscale(enable=True, axis='x', tight=True) 
    plt.savefig('Drainage_Area_for_the_' +filename[0]+'.png', bbox_inches='tight')
       
    plt.close()
    
    
    #map of area
    latitude=data[:,0]
    longitude=data[:,1]
    location_latitude= data[:,8]
    location_longitude= data[:,9]
    plt.plot(longitude,latitude, 'b-', linewidth=2)
    plt.scatter(location_longitude,location_latitude,c='r',marker='o',s=6)
    plt.xlabel('Eastings', fontsize=20)
    plt.ylabel('Northings',fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title('Map view of the '+filename[0],fontsize=18)
    plt.savefig('Map_of_' +filename[0]+'.png', bbox_inches='tight')
    plt.close()
    
    data=np.loadtxt(fname)
    
    
   
    
 