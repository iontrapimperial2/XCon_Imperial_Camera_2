# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:20:45 2019

@author: iontrap
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from math import erf, sqrt

a = []


for num in range(1,101,1):
    x = list(range(num*5, (100*5), 1))
    y = x +list(range(0, (num-1)*5,1))
    
    #unbinned
    df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Read_noise_test\unbinned2.txt', header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
    a2 = df.drop(y)
    a.append(sum(np.array(a2).ravel().tolist()))
    
    
#binned
df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Read_noise_test\binned2.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
b = np.array(df2).ravel().tolist()


#unbinned
fi = plt.figure('Histogram 250x250 ambient light unbinned')
fi.suptitle('Histogram 250x250 ambient light unbinned', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 50, label = 'unbinned distribution')

axe.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(a))
m, s = stats.norm.fit(a) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe.plot(lnspc, pdf_g, 'r', label="unbinned distribution fit") # plot it
axe.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


#binned
fi1 = plt.figure('Histogram 250x250 ambient light binned')
fi1.suptitle('Histogram 250x250 ambient light binned', fontsize=20)
axe1 = fi1.add_subplot(111)
x1, bins1, p1 = axe1.hist(b, density=True, bins = 50, label = 'binned distribution')

axe1.tick_params(axis='both', labelsize = 16)
xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(b) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe1.plot(lnspc1, pdf_g1, 'g', label="binned distribution fit") 
axe1.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

plt.show()