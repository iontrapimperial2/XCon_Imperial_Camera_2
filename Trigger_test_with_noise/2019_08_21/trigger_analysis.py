# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:58:02 2019

@author: iontrap
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
a = []
a1 = []
for i in range(1,11,1):
    df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Trigger_test_with_noise\2019_08_21\internal' + str(i) + '.txt', header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
    a = a + np.array(df).ravel().tolist()
    
    df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Trigger_test_with_noise\2019_08_21\external' + str(i) + '.txt', header = None)
    df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
    df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
    a1 = a1 + np.array(df1).ravel().tolist()




'''
print(np.mean(a), np.std(a))
print(np.mean(a1), np.std(a1))
print(np.mean(b), np.std(b))
print(np.mean(b1), np.std(b1))
print(np.mean(c), np.std(c))
print(np.mean(c1), np.std(c1))
print(np.mean(d), np.std(d))
print(np.mean(d1), np.std(d1))
print(np.mean(e), np.std(e))
print(np.mean(e1), np.std(e1))
'''
#Gaussian function for fitting
def fit_function(x,A, mu, sigma):
    return A*np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2))


fi = plt.figure('Histogram for Trigger Comparison with Background Noise')
fi.suptitle('Histogram for Trigger Comparison with Background Noise', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 255, label = 'Internal Trigger')
axe.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
axe.set_xlim(125, 360)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.03, 190, 13])
axe.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Internal Trigger Gauss Fit")
#axe.legend(fontsize = 16)


#fi1 = plt.figure('Histogram for Background 10 ms exposure 200 gain 1MHz Readout')
#fi1.suptitle('Histogram for Background 10 ms exposure 200 gain 1MHz Readout', fontsize=20)
#axe1 = fi1.add_subplot(111)
x1, bins1, p1 = axe.hist(a1, density=True, bins = 272, label = 'External Trigger')
#axe1.tick_params(axis='both', labelsize = 16)
#plt.xlabel('Count reading', fontsize=18)
#plt.ylabel('Probability Density', fontsize=18)
#axe1.set_xlim(125, 275)
# =============================================================================
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# #lnspc = np.linspace(xmin, xmax, 10000)
# lnspc = np.linspace(0, xmax, 10000)
# 
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
# popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.05, 203, 30])
# axe.plot(lnspc, fit_function(lnspc,*popt1), 'g', label="External Trigger Gauss Fit")
# =============================================================================

axe.legend(fontsize = 16)

plt.figure()
plt.plot(binscenters,x , '.',label = 'Internal Trigger')
plt.plot(binscenters1,x1 ,'.', label = 'External Trigger')
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)



#axe.legend(fontsize = 16)
''''''
plt.show()










