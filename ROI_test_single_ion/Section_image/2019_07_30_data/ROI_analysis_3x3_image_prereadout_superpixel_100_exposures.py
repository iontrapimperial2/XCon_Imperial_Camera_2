# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich, YWu
"""
   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
from math import erf, sqrt





#1 sec
df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\1s.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
a = np.array(df).ravel().tolist()

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\1s.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
a1 = np.array(df1).ravel().tolist()

#0.5 sec
df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\05s.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
b = np.array(df2).ravel().tolist()

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\05s.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column
b1 = np.array(df3).ravel().tolist()

#0.1 sec
df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\01s.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column
c = np.array(df4).ravel().tolist()

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\01s.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column
c1 = np.array(df5).ravel().tolist()

#50 ms
df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\50ms.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column
d = np.array(df6).ravel().tolist()

df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\50ms.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column
d1 = np.array(df7).ravel().tolist()

#40 ms
df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\40ms.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column
e = np.array(df8).ravel().tolist()

df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\40ms.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column
e1 = np.array(df9).ravel().tolist()

#30 ms
df10 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\30ms.txt', header = None)
df10.drop(df10.columns[-1], axis=1, inplace=True)  #delete last column
df10.drop(df10.columns[0], axis=1, inplace=True)           #delete first column
f = np.array(df10).ravel().tolist()

df11 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\30ms.txt', header = None)
df11.drop(df11.columns[-1], axis=1, inplace=True)  #delete last column
df11.drop(df11.columns[0], axis=1, inplace=True)           #delete first column
f1 = np.array(df11).ravel().tolist()

#20 ms
df12 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\20ms.txt', header = None)
df12.drop(df12.columns[-1], axis=1, inplace=True)  #delete last column
df12.drop(df12.columns[0], axis=1, inplace=True)           #delete first column
g = np.array(df12).ravel().tolist()

df13 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\20ms.txt', header = None)
df13.drop(df13.columns[-1], axis=1, inplace=True)  #delete last column
df13.drop(df13.columns[0], axis=1, inplace=True)           #delete first column
g1 = np.array(df13).ravel().tolist()

#10 ms
df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\bright\10ms.txt', header = None)
df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column
h = np.array(df14).ravel().tolist()

df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_30_data\3x3\dark\10ms.txt', header = None)
df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column
h1 = np.array(df15).ravel().tolist()

    






#bright
a4 = np.mean(a)    #1 sec
b4 = np.mean(b)    #0.5 sec
c4 = np.mean(c)    #0.1 sec
d4 = np.mean(d)    #50 ms
e4 = np.mean(e)    #40 ms
f4 = np.mean(f)    #30 ms
g4 = np.mean(g)    #20 ms
h4 = np.mean(h)    #10 ms


#dark
a5 = np.mean(a1)   #1 sec
b5 = np.mean(b1)   #0.5 sec
c5 = np.mean(c1)   #0.1 sec
d5 = np.mean(d1)   #50 ms
e5 = np.mean(e1)   #40 ms
f5 = np.mean(f1)   #30 ms
g5 = np.mean(g1)   #20 ms
h5 = np.mean(h1)   #10 ms

diff = [a4-a5,b4-b5,c4-c5,d4-d5,e4-e5,f4-f5,g4-g5,h4-h5]
t = [1.0,0.5,0.1,0.05,0.04,0.03,0.02,0.01]
std = [np.std(a),np.std(b),np.std(c),np.std(d),np.std(e),np.std(f),np.std(g),np.std(h)]
std1 = [np.std(a1),np.std(b1),np.std(c1),np.std(d1),np.std(e1),np.std(f1),np.std(g1),np.std(h1)]
err = [((std[i]**2) + (std1[i]**2))**0.5 for i in range(0,8,1)]

def linearfit(time,m,c):
    return m*time + c
    
popt, pcov = curve_fit(linearfit, t, diff, sigma = err)

#slope, intercept, r_value, p_value, std_err = stats.linregress(t,diff)
line = [popt[0]*q + popt[1] for q in t]
intercept = str(popt[1]) + '+/-' + str(np.sqrt(pcov[1,1]))
slope = str(popt[0]) + ' +/- ' + str(np.sqrt(pcov[0,0]))



fig = plt.figure('Difference Between Mean Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 100 Exposures')
fig.suptitle('Difference Between Mean Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 100 Exposures', fontsize=20)
axes = fig.add_subplot(111)
#axes.plot(t,diff,'.')
axes.errorbar(t,diff,yerr=err, fmt = 'x')
t.insert(0,0)
line.insert(0,popt[1])
axes.plot(t,line)
axes.tick_params(axis = 'both', labelsize =16)
plt.grid()
plt.ylabel('Count reading', fontsize=18)
plt.xlabel('Exposure time/s', fontsize=18)






#find intercept of B and D distributions (FOR GAUSSIAN ONLY)
def solve(m1,m2,std1,std2):
  a = 1/(2*std1**2) - 1/(2*std2**2)
  b = m2/(std2**2) - m1/(std1**2)
  c = m1**2 /(2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
  return np.roots([a,b,c])


#Gaussian function for fitting
def fit_function(x, A, mu, sigma):
    return (A*np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))


#Histograms
fi = plt.figure('Histogram for 1 s Exposure for 3x3 ROI over 100 Exposures')
fi.suptitle('Bright and Dark Histogram overlap: 1 s Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe.hist(a1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0004, 24100, 2000])
print(popt) 
axe.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.003, 584, 250])
print(popt1)
axe.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 1 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 1 s exposure: ' + str(Pin1))


fi1 = plt.figure('Histogram for 0.5 s Exposure for 3x3 ROI over 100 Exposures')
fi1.suptitle('Bright and Dark Histogram overlap: 0.5 s Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe1 = fi1.add_subplot(111)
x, bins, p = axe1.hist(b, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe1.hist(b1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe1.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0004, 12700, 2000])
print(popt) 
axe1.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.0046, 305, 200])
print(popt1)
axe1.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe1.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 0.5 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 0.5 s exposure: ' + str(Pin1))



fi2 = plt.figure('Histogram for 0.1 s Exposure for 3x3 ROI over 100 Exposures')
fi2.suptitle('Bright and Dark Histogram overlap: 0.1 s Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe2 = fi2.add_subplot(111)
x, bins, p = axe2.hist(c, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe2.hist(c1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe2.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.001, 2700, 700])
print(popt) 
axe2.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.017, 184, 50])
print(popt1)
axe2.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe2.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 0.1 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 0.1 s exposure: ' + str(Pin1))


fi3 =plt.figure('Histogram for 50 ms Exposure for 3x3 ROI over 100 Exposures')
fi3.suptitle('Bright and Dark Histogram overlap: 50 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe3 = fi3.add_subplot(111)
x, bins, p = axe3.hist(d, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe3.hist(d1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe3.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0013, 1464, 400])
print(popt) 
axe3.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.03, 182, 32])
print(popt1)
axe3.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe3.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 50 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 50 ms exposure: ' + str(Pin1))


fi4 = plt.figure('Histogram for 40 ms Exposure for 3x3 ROI over 100 Exposures')
fi4.suptitle('Bright and Dark Histogram overlap: 40 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe4 = fi4.add_subplot(111)
x, bins, p = axe4.hist(e, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe4.hist(e1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe4.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0014, 1200, 500])
print(popt) 
axe4.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.02, 190, 40])
print(popt1)
axe4.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe4.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 40 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 40 ms exposure: ' + str(Pin1))


fi5 = plt.figure('Histogram for 30 ms Exposure for 3x3 ROI over 100 Exposures')
fi5.suptitle('Bright and Dark Histogram overlap: 30 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe5 = fi5.add_subplot(111)
x, bins, p = axe5.hist(f, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe5.hist(f1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe5.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0017, 970, 400])
print(popt) 
axe5.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.028, 180, 40])
print(popt1)
axe5.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe5.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 30 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 30 ms exposure: ' + str(Pin1))


fi6 = plt.figure('Histogram for 20 ms Exposure for 3x3 ROI over 100 Exposures')
fi6.suptitle('Bright and Dark Histogram overlap: 20 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe6 = fi6.add_subplot(111)
x, bins, p = axe6.hist(g, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe6.hist(g1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe6.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.0024, 620, 250])
print(popt) 
axe6.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.03, 176, 30])
print(popt1)
axe6.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe6.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 20 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 20 ms exposure: ' + str(Pin1))




fi7 =plt.figure('Histogram for 10 ms Exposure for 3x3 ROI over 100 Exposures')
fi7.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe7 = fi7.add_subplot(111)
x, bins, p = axe7.hist(h, density=True, bins = 20, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe7.hist(h1, density=True, bins = 20, label = 'Prereadout Super Pixel Dark Ion')
axe7.tick_params(axis='both', labelsize = 16)

xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(0, xmax, 10000)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.003, 380, 130])
print(popt) 
axe7.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it


xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.029, 178, 14])
print(popt1)
axe7.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe7.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(popt[1],popt1[1],popt[2],popt1[2])
print(result)
x1 = 0      
x2 = result[0]
#x3 = 9999999999

Pin = stats.norm.cdf(x2,popt[1],popt[2])
Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 10 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 10 ms exposure: ' + str(Pin1))


plt.show()