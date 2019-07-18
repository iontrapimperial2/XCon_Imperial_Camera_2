# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:55:59 2019

@author: iontrap/YWu
"""

import matplotlib.pyplot as plt
from scipy import stats

closed = [192.1, 192.1, 191.5, 192.2, 193.6, 192.8, 192.1, 193.2, 192.6, 191.9, 192.8, 193.3, 192.6,
         192.0, 192.9, 191.5, 192.0, 193.3, 193.0, 191.6]#207.8, 
closed_std = [11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8,
            11.8, 11.8, 11.8, 11.8, 11.8, 11.8, 11.8]#11.3,
'''
open_ = [193.7, 194.3, 195.0, 196.0, 196.4, 195.1, 194.6, 195.2, 195.5, 194.6, 196.6, 196.1, 197.2, 
         196.8, 197.1, 198.0, 198.1, 198.5, 199.1, 199.4, 199.6, 200.0, 200.3, 201.0, 201.9, 204.2, 207.3, 
         208.2, 210.8, 216.8, 223.2, 229.2, 238.2, 248.9, 260.7, 279.0]
open_std = [11.7, 11.7, 11.7, 11.7, 11.7, 11.7, 11.7, 11.7, 11.8, 11.7, 11.8, 11.8, 11.8,
            11.8, 11.9, 11.9, 12.0, 12.0, 12.0, 12.3, 12.4, 12.7, 12.7, 13.1, 13.9, 14.8, 15.8,
            16.3, 17.9, 21.6, 24.9, 29.3, 34.8, 42.2, 51.5, 64.0]
'''
open_ = [195.1, 201.8, 207.4, 210.9, 217.5, 220.6, 224.5, 229.2, 234.2, 238.0, 
         244.5, 248.6, 252.3, 257.0, 260.6, 264.5, 269.7, 274.5, 278.8, 284.1]
open_std = [12.3, 13.7, 15.8, 18.1, 20.6, 23.5, 26.3, 29.3, 32.1, 35.2, 
            38.1, 41.2, 44.3, 47.2, 50.0, 53.3, 56.4, 59.4, 62.6, 66.1]

gain = range(50, 1050, 50)

slope, intercept, r_value, p_value, std_err = stats.linregress(gain,closed)
line = slope*gain+intercept

slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(gain,open_)
line1 = slope1*gain+intercept1


fig = plt.figure('Mean Count per Pixel vs EMCCD Gain with Shutter Closed')
fig.suptitle('Mean Count per Pixel vs EMCCD Gain with Shutter Closed (Background Noise)', fontsize = 20)
ax = fig.add_subplot(111)
ax.errorbar(gain, closed, yerr=closed_std, fmt = 'x')
ax.plot (gain, line)
plt.xlabel('EMCCD Gain',fontsize=18)
plt.ylabel('Mean Count per pixel',fontsize=18)
ax.tick_params(axis='both', labelsize = 16)


fig1 = plt.figure('Mean Count per Pixel vs EMCCD Gain with Shutter Opened (Ambient light)')
fig1.suptitle('Mean Count per Pixel vs EMCCD Gain with Shutter Opened (Ambient light)', fontsize = 20)
ax1 = fig1.add_subplot(111)
ax1.errorbar(gain, open_, yerr=open_std, fmt = 'x')
ax1.plot (gain, line1)
plt.xlabel('EMCCD Gain',fontsize=18)
plt.ylabel('Mean Count per pixel',fontsize=18)
ax1.tick_params(axis='both', labelsize = 16)


plt.show()