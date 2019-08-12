# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:58:02 2019

@author: iontrap
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\100.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
a = np.array(df).ravel().tolist()

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\200.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
a1 = np.array(df1).ravel().tolist()


df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\300.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
b = np.array(df2).ravel().tolist()

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\400.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column
b1 = np.array(df3).ravel().tolist()


df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\500.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column
c = np.array(df4).ravel().tolist()

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\600.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column
c1 = np.array(df5).ravel().tolist()


df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\700.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column
d = np.array(df6).ravel().tolist()

df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\800.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column
d1 = np.array(df7).ravel().tolist()


df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\900.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column
e = np.array(df8).ravel().tolist()

df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Gain_test_with_noise\2019_08_12\1000.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column
e1 = np.array(df9).ravel().tolist()


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


fi = plt.figure('Histogram for Background 10 ms exposure 100 gain')
fi.suptitle('Histogram for Background 10 ms exposure 100 gain', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 40, label = '100 Gain')
axe.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.03, 190, 13])
axe.plot(lnspc, fit_function(lnspc,*popt), 'r', label="100 Gain Gauss Fit")
axe.legend(fontsize = 16)


fi1 = plt.figure('Histogram for Background 10 ms exposure 200 gain')
fi1.suptitle('Histogram for Background 10 ms exposure 200 gain', fontsize=20)
axe1 = fi1.add_subplot(111)
x1, bins1, p1 = axe1.hist(a1, density=True, bins = 30, label = '200 Gain')
axe1.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.05, 190, 13])
axe1.plot(lnspc, fit_function(lnspc,*popt1), 'r', label="200 Gain Gauss Fit")
axe1.legend(fontsize = 16)


fi2 = plt.figure('Histogram for Background 10 ms exposure 300 gain')
fi2.suptitle('Histogram for Background 10 ms exposure 300 gain', fontsize=20)
axe2 = fi2.add_subplot(111)
x2, bins2, p2 = axe2.hist(b, density=True, bins = 55, label = '300 Gain')
axe2.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters2 = np.array([0.5 * (bins2[i] + bins2[i+1]) for i in range(len(bins2)-1)])
popt2, pcov2 = curve_fit(fit_function, xdata=binscenters2, ydata=x2, p0 = [0.037, 190, 13])
axe2.plot(lnspc, fit_function(lnspc,*popt2), 'r', label="300 Gain Gauss Fit")
axe2.legend(fontsize = 16)


fi3 = plt.figure('Histogram for Background 10 ms exposure 400 gain')
fi3.suptitle('Histogram for Background 10 ms exposure 400 gain', fontsize=20)
axe3 = fi3.add_subplot(111)
x3, bins3, p3 = axe3.hist(b1, density=True, bins = 70, label = '400 Gain')
axe3.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters3 = np.array([0.5 * (bins3[i] + bins3[i+1]) for i in range(len(bins3)-1)])
popt3, pcov3 = curve_fit(fit_function, xdata=binscenters3, ydata=x3, p0 = [0.036, 190, 13])
axe3.plot(lnspc, fit_function(lnspc,*popt3), 'r', label="400 Gain Gauss Fit")
axe3.legend(fontsize = 16)


fi4 = plt.figure('Histogram for Background 10 ms exposure 500 gain')
fi4.suptitle('Histogram for Background 10 ms exposure 500 gain', fontsize=20)
axe4 = fi4.add_subplot(111)
x4, bins4, p4 = axe4.hist(c, density=True, bins = 80, label = '500 Gain')
axe4.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters4 = np.array([0.5 * (bins4[i] + bins4[i+1]) for i in range(len(bins4)-1)])
popt4, pcov4 = curve_fit(fit_function, xdata=binscenters4, ydata=x4, p0 = [0.03, 190, 13])
axe4.plot(lnspc, fit_function(lnspc,*popt4), 'r', label="500 Gain Gauss Fit")
axe4.legend(fontsize = 16)


fi5 = plt.figure('Histogram for Background 10 ms exposure 600 gain')
fi5.suptitle('Histogram for Background 10 ms exposure 600 gain', fontsize=20)
axe5 = fi5.add_subplot(111)
x5, bins5, p5 = axe5.hist(c1, density=True, bins = 100, label = '600 Gain')
axe5.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters5 = np.array([0.5 * (bins5[i] + bins5[i+1]) for i in range(len(bins5)-1)])
popt5, pcov5 = curve_fit(fit_function, xdata=binscenters5, ydata=x5, p0 = [0.02, 190, 13])
axe5.plot(lnspc, fit_function(lnspc,*popt5), 'r', label="600 Gain Gauss Fit")
axe5.legend(fontsize = 16)


fi6 = plt.figure('Histogram for Background 10 ms exposure 700 gain')
fi6.suptitle('Histogram for Background 10 ms exposure 700 gain', fontsize=20)
axe6 = fi6.add_subplot(111)
x6, bins6, p6 = axe6.hist(d, density=True, bins = 140, label = '700 Gain')
axe6.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters6 = np.array([0.5 * (bins6[i] + bins6[i+1]) for i in range(len(bins6)-1)])
popt6, pcov6 = curve_fit(fit_function, xdata=binscenters6, ydata=x6, p0 = [0.023, 190, 13])
axe6.plot(lnspc, fit_function(lnspc,*popt6), 'r', label="700 Gain Gauss Fit")
axe6.legend(fontsize = 16)


fi7 = plt.figure('Histogram for Background 10 ms exposure 800 gain')
fi7.suptitle('Histogram for Background 10 ms exposure 800 gain', fontsize=20)
axe7 = fi7.add_subplot(111)
x7, bins7, p7 = axe7.hist(d1, density=True, bins = 180, label = '800 Gain')
axe7.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters7 = np.array([0.5 * (bins7[i] + bins7[i+1]) for i in range(len(bins7)-1)])
popt7, pcov7 = curve_fit(fit_function, xdata=binscenters7, ydata=x7, p0 = [0.037, 190, 13])
axe7.plot(lnspc, fit_function(lnspc,*popt7), 'r', label="800 Gain Gauss Fit")
axe7.legend(fontsize = 16)


fi8 = plt.figure('Histogram for Background 10 ms exposure 900 gain')
fi8.suptitle('Histogram for Background 10 ms exposure 900 gain', fontsize=20)
axe8 = fi8.add_subplot(111)
x8, bins8, p8 = axe8.hist(e, density=True, bins = 175, label = '900 Gain')
axe8.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters8 = np.array([0.5 * (bins8[i] + bins8[i+1]) for i in range(len(bins8)-1)])
popt8, pcov8 = curve_fit(fit_function, xdata=binscenters8, ydata=x8, p0 = [0.037, 190, 13])
axe8.plot(lnspc, fit_function(lnspc,*popt7), 'r', label="900 Gain Gauss Fit")
axe8.legend(fontsize = 16)


fi9 = plt.figure('Histogram for Background 10 ms exposure 1000 gain')
fi9.suptitle('Histogram for Background 10 ms exposure 1000 gain', fontsize=20)
axe9 = fi9.add_subplot(111)
x9, bins9, p9 = axe9.hist(e1, density=True, bins = 200, label = '1000 Gain')
axe9.tick_params(axis='both', labelsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)
lnspc = np.linspace(0, xmax, 10000)

binscenters9 = np.array([0.5 * (bins9[i] + bins9[i+1]) for i in range(len(bins9)-1)])
popt9, pcov9 = curve_fit(fit_function, xdata=binscenters9, ydata=x9, p0 = [0.033, 190, 13])
axe9.plot(lnspc, fit_function(lnspc,*popt9), 'r', label="1000 Gain Gauss Fit")
axe9.legend(fontsize = 16)


#axe.legend(fontsize = 16)
''''''
plt.show()










