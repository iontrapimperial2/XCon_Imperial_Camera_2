# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich, YWu
"""
   
import pandas as pd
import numpy as np
from math import factorial
#from scipy.special import factorial
import matplotlib.pyplot as plt
from scipy import signal
from scipy import stats
from scipy.optimize import curve_fit



# =============================================================================
# a = []
# a1 = []
# b = []
# b1 = []
# c = []
# c1 = []
# d = []
# d1 = []
# e = []
# e1 = []
# =============================================================================
'''
f = []
f1 = []
g = []
g1 = []
h = []
h1 = []
'''

###Bright###

#for num in range(1,1001,1):

#7x7
df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_16_data\7x7\binned\bright\10ms.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
a = np.array(df).ravel().tolist()
        

#6x6
df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_16_data\6x6\binned\bright\10ms.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
b = np.array(df2).ravel().tolist()
        

#5x5
df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_16_data\5x5\binned\bright\10ms.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column
c = np.array(df4).ravel().tolist()
        
#4x4
df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_16_data\4x4\binned\bright\10ms.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column
d = np.array(df6).ravel().tolist()
        
#3x3
df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_16_data\3x3\binned\bright\10ms.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column
e = np.array(df8).ravel().tolist()


###Dark###

#7x7
df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_02_data\7x7\dark\10ms.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
a1 = np.array(df1).ravel().tolist()
    
#6x6    
df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_02_data\6x6\dark\10ms.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column
b1 = np.array(df3).ravel().tolist()
    
#5x5
df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_02_data\5x5\dark\10ms.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column
c1 = np.array(df5).ravel().tolist()
    
#4x4
df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_02_data\4x4\dark\10ms.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column
d1 = np.array(df7).ravel().tolist()
    
#3x3
df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_08_02_data\3x3\dark\10ms.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column
e1 = np.array(df9).ravel().tolist()



#find intercept of B and D distributions (FOR GAUSSIAN ONLY)
def solve(m1,m2,std1,std2):
  a = 1/(2*std1**2) - 1/(2*std2**2)
  b = m2/(std2**2) - m1/(std1**2)
  c = m1**2 /(2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
  return np.roots([a,b,c])


#Gaussian function for fitting
def fit_function(x, mu, sigma):
    return ((1/(sigma*np.sqrt(2*np.pi)))*np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))

def MB_fit(x,a, A, mu, sigma):
    return (np.sqrt(2/np.pi)*(((x**2)*np.exp(-(x**2)/(2*(a**2))))/(a**3)))*(A*np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2)))

def P(x,s,G):
    return (((x/G)**(s-1))/(G*factorial(int(s-1)))) * np.exp(-x/G)

def q(s,l):
    return ((l**(s))/(factorial(int(s)))) * np.exp(l)

def q1(x,l):
    return ((l**(x))/(factorial(int(x)))) * np.exp(l)

def function_fit(x,s):
        return (((x/300)**(s-1))/(300*factorial(int(s-1)))) * np.exp(-x/300)
  
def h(x,l,G):
    h= [] 
    for i in range(1,170,1):
        a = P(x,i,G)*q(i,l)
        #print(a)
        h.append(a)
    return sum(h)
    
def convolve(x,l,G,mu,sigma):
    return signal.fftconvolve(h(x,l,G),fit_function(x,mu,sigma),mode = 'same')    


#Histograms
'''
fi = plt.figure('Histogram for 10 ms Exposure for 7x7 ROI over 2000 Exposures')
fi.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 7x7 ROI over 2000 Exposures', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 150, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe.hist(a1, density=True, bins = 150, label = 'Prereadout Super Pixel Dark Ion')
axe.tick_params(axis='both', labelsize = 16)

# =============================================================================
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, 10000)
# #lnspc = np.linspace(0, xmax, 10000)
# #lnspc2 = np.linspace(100, xmax+100, 10000)
# 
# 
# binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
# popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [10500, 500])
# #popt, pcov = curve_fit(MB_fit, xdata=binscenters, ydata=x, p0 = [100,0.003, 410, 250])
# #popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [2,2, 5])#
# #popt, pcov = curve_fit(convolve, xdata=binscenters, ydata=x, p0 = [5,90,1000, 200])#
# #popt, pcov = curve_fit(q1, xdata=binscenters, ydata=x)#, p0 = [100]
# #print(popt) 
# #fit = [convolve(i,*popt) for i in lnspc]
# axe.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Post-readout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe.plot(lnspc, MB_fit(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe.plot(lnspc2, convolve(lnspc,*popt)/120, 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe.plot(lnspc, q1(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# =============================================================================

a2 = []
for i in bins:
    if i < 264.416:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x[:len(binscenters2)]
for i in a3:
    if i < 0.0014:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error = sum(a3*binwidth)  
print('bright ion discrimination error from histogram overlap for 7x7 ROI: ' + str(error))   
        
a2 = []
for i in bins1:
    if i > 264.416:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x1[-len(binscenters2):]
for i in a3:
    if i < 0.0016:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error1 = sum(a3*binwidth)  
print('dark ion discrimination error from histogram overlap for 7x7 ROI: ' + str(error1))
print(error + error1)

# =============================================================================
# xt1 = plt.xticks()[0]  
# xmin1, xmax1 = min(xt1), max(xt1)  
# lnspc1 = np.linspace(xmin1, xmax1, 10000)
# #lnspc1 = np.linspace(0, xmax1, 10000)
# #lnspc3 = np.linspace(100, xmax1+100, 10000)
# 
# binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
# popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [10200, 400])
# #popt1, pcov1 = curve_fit(MB_fit, xdata=binscenters1, ydata=x1, p0 = [30,0.02, 150, 60])
# #popt1, pcov1 = curve_fit(function_fit, xdata=binscenters1, ydata=x1,p0 = [3,1000])
# #popt1, pcov1 = curve_fit(convolve, xdata=binscenters1, ydata=x1, p0 = [1,10,150, 12])#
# #print(popt1)
# axe.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Post-readout Super Pixel Dark Ion Gaussian fit") 
# #axe.plot(lnspc1, MB_fit(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# #axe.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# #axe.plot(lnspc3, convolve(lnspc1,*popt1)/2, 'r', label="Prereadout Super Pixel Dark Ion Gaussian fit") # plot it
# axe.legend(fontsize = 16)
# 
# plt.xlabel('Count reading', fontsize=18)
# plt.ylabel('Probability Density', fontsize=18)
# 
# 
# result = solve(popt[0],popt1[0],popt[1],popt1[1])
# result = solve(popt,popt1)
# print(result)
# x1 = 0      
# x2 = result[0]
# #x3 = 9999999999
# 
# Pin = stats.norm.cdf(x2,popt[0],popt[1])
# Pin1 = 1- stats.norm.cdf(x2, popt1[0], popt1[1])#(p_upper1) - (p_lower1)
# print('probability of misinterpreting bright ion as dark ion at 10 ms exposure for 7x7 ROI: ' + str(Pin))
# print('probability of misinterpreting dark ion as bright ion at 10 ms exposure for 7x7 ROI: ' + str(Pin1))
# =============================================================================
axe.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi1 = plt.figure('Histogram for 10 ms Exposure for 6x6 ROI over 2000 Exposures')
fi1.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 6x6 ROI over 2000 Exposures', fontsize=20)
axe1 = fi1.add_subplot(111)
x, bins, p = axe1.hist(b, density=True, bins = 150, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe1.hist(b1, density=True, bins = 150, label = 'Prereadout Super Pixel Dark Ion')
axe1.tick_params(axis='both', labelsize = 16)

#xt = plt.xticks()[0]  
#xmin, xmax = min(xt), max(xt)  
#lnspc = np.linspace(xmin, xmax, 10000)


#binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
#popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [0.003, 350, 200])
#popt, pcov = curve_fit(MB_fit, xdata=binscenters, ydata=x, p0 = [100,0.003, 350, 200])
#print(popt) 
#axe1.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
#axe1.plot(lnspc, MB_fit(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
a2 = []
for i in bins:
    if i < 240.48:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x[:len(binscenters2)]
for i in a3:
    if i < 0.0015:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error = sum(a3*binwidth)  
print('bright ion discrimination error from histogram overlap for 6x6 ROI: ' + str(error))   
        
a2 = []
for i in bins1:
    if i > 240.48:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x1[-len(binscenters2):]
for i in a3:
    if i < 0.0021:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error1 = sum(a3*binwidth)  
print('dark ion discrimination error from histogram overlap for 6x6 ROI: ' + str(error1))
print(error + error1)

#xt1 = plt.xticks()[0]  
#xmin1, xmax1 = min(xt1), max(xt1)  
#lnspc1 = np.linspace(xmin1, xmax1, 10000)


#binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
#popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [0.023, 157, 30])
#popt1, pcov1 = curve_fit(MB_fit, xdata=binscenters1, ydata=x1, p0 = [30,0.023, 157, 30])
#print(popt1)
#axe1.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
#axe1.plot(lnspc1, MB_fit(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
axe1.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

#result = solve(popt[1],popt1[1],popt[2],popt1[2])
#print(result)
#x1 = 0      
#x2 = result[0]
#x3 = 9999999999

#Pin = stats.norm.cdf(x2,popt[1],popt[2])
#Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
#print('probability of misinterpreting bright ion as dark ion at 10 ms exposure for 6x6 ROI: ' + str(Pin))
#print('probability of misinterpreting dark ion as bright ion at 10 ms exposure for 6x6 ROI: ' + str(Pin1))
'''

'''
fi2 = plt.figure('Histogram for 10 ms Exposure for 5x5 ROI over 2000 Exposures')
fi2.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 5x5 ROI over 2000 Exposures', fontsize=20)
axe2 = fi2.add_subplot(111)
x, bins, p = axe2.hist(c, density=True, bins = 100, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe2.hist(c1, density=True, bins = 100, label = 'Prereadout Super Pixel Dark Ion')
axe2.tick_params(axis='both', labelsize = 16)

# =============================================================================
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, 10000)
# 
# 
# binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
# popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [5500, 200])
# #popt, pcov = curve_fit(MB_fit, xdata=binscenters, ydata=x, p0 = [100,0.003, 350, 200])
# #print(popt) 
# axe2.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe2.plot(lnspc, MB_fit(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# =============================================================================
a2 = []
for i in bins:
    if i < 228.6:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x[:len(binscenters2)]
for i in a3:
    if i < 0.00144291:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error = sum(a3*binwidth)  
print('bright ion discrimination error from histogram overlap for 5x5 ROI: ' + str(error))   
        
a2 = []
for i in bins1:
    if i > 228.6:
        
        a2.append(i)
binscenters2 = np.array([(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x1[-len(binscenters2):]
for i in a3:
    if i < 0.00251:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error1 = sum(a3*binwidth)  
print('dark ion discrimination error from histogram overlap for 5x5 ROI: ' + str(error1))
print(error + error1)

# =============================================================================
# xt1 = plt.xticks()[0]  
# xmin1, xmax1 = min(xt1), max(xt1)  
# lnspc1 = np.linspace(xmin1, xmax1, 10000)
# 
# 
# binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
# popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [5200, 300])
# #popt1, pcov1 = curve_fit(MB_fit, xdata=binscenters1, ydata=x1, p0 = [30,0.023, 157, 30])
# print(popt1)
# axe2.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Post-readout Super Pixel Dark Ion Gaussian fit") 
# #axe2.plot(lnspc1, MB_fit(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# axe2.legend(fontsize = 16)
# 
# plt.xlabel('Count reading', fontsize=18)
# plt.ylabel('Probability Density', fontsize=18)
# 
# result = solve(popt[0],popt1[0],popt[1],popt1[1])
# print(result)
# x1 = 0      
# x2 = result[0]
# #x3 = 9999999999
# 
# Pin = stats.norm.cdf(x2,popt[0],popt[1])
# Pin1 = 1- stats.norm.cdf(x2, popt1[0], popt1[1])#(p_upper1) - (p_lower1)
# print('probability of misinterpreting bright ion as dark ion at 10 ms exposure for 5x5 ROI: ' + str(Pin))
# print('probability of misinterpreting dark ion as bright ion at 10 ms exposure for 5x5 ROI: ' + str(Pin1))
# =============================================================================
axe2.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)



fi3 =plt.figure('Histogram for 10 ms Exposure for 4x4 ROI over 2000 Exposures')
fi3.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 4x4 ROI over 2000 Exposures', fontsize=20)
axe3 = fi3.add_subplot(111)
x, bins, p = axe3.hist(d, density=True, bins = 100, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe3.hist(d1, density=True, bins = 100, label = 'Prereadout Super Pixel Dark Ion')
axe3.tick_params(axis='both', labelsize = 16)

# =============================================================================
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, 10000)
# 
# 
# binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
# popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [3500, 200])
# #popt, pcov = curve_fit(MB_fit, xdata=binscenters, ydata=x, p0 = [100,0.003, 350, 200])
# #print(popt) 
# axe3.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe3.plot(lnspc, MB_fit(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# =============================================================================
a2 = []
for i in bins:
    if i < 217.6:
        
        a2.append(i)
binscenters2 = np.array([0.5*(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x[:len(binscenters2)]
for i in a3:
    if i < 0.002063:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error = sum(a3*binwidth)  
print('bright ion discrimination error from histogram overlap for 4x4 ROI: ' + str(error))   
        
a2 = []
for i in bins1:
    if i > 217.6:
        
        a2.append(i)
binscenters2 = np.array([0.5*(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x1[-len(binscenters2):]
for i in a3:
    if i < 0.00201:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error1 = sum(a3*binwidth)  
print('dark ion discrimination error from histogram overlap for 4x4 ROI: ' + str(error1))
print(error + error1)

# =============================================================================
# xt1 = plt.xticks()[0]  
# xmin1, xmax1 = min(xt1), max(xt1)  
# lnspc1 = np.linspace(xmin1, xmax1, 10000)
# 
# 
# binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
# popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [3340, 200])
# #popt1, pcov1 = curve_fit(MB_fit, xdata=binscenters1, ydata=x1, p0 = [30,0.023, 157, 30])
# #print(popt1)
# axe3.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# #axe3.plot(lnspc1, MB_fit(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# =============================================================================
axe3.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

# =============================================================================
# result = solve(popt[1],popt1[1],popt[2],popt1[2])
# print(result)
# x1 = 0      
# x2 = result[0]
# #x3 = 9999999999
# 
# Pin = stats.norm.cdf(x2,popt[1],popt[2])
# Pin1 = 1- stats.norm.cdf(x2, popt1[1], popt1[2])#(p_upper1) - (p_lower1)
# print('probability of misinterpreting bright ion as dark ion at 10 ms exposure for 4x4 ROI: ' + str(Pin))
# print('probability of misinterpreting dark ion as bright ion at 10 ms exposure for 4x4 ROI: ' + str(Pin1))
# =============================================================================
'''

fi4 = plt.figure('Histogram for 10 ms Exposure for 3x3 ROI over 2000 Exposures')
fi4.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 3x3 ROI over 2000 Exposures', fontsize=20)
axe4 = fi4.add_subplot(111)
x, bins, p = axe4.hist(e, density=True, bins = 100, label = 'Prereadout Super Pixel Bright Ion')
x1, bins1, p1 = axe4.hist(e1, density=True, bins = 100, label = 'Prereadout Super Pixel Dark Ion')
axe4.tick_params(axis='both', labelsize = 16)

# =============================================================================
# xt = plt.xticks()[0]  
# xmin, xmax = min(xt), max(xt)  
# lnspc = np.linspace(xmin, xmax, 10000)
# 
# 
# binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
# popt, pcov = curve_fit(fit_function, xdata=binscenters, ydata=x, p0 = [3000, 200])
# #popt, pcov = curve_fit(MB_fit, xdata=binscenters, ydata=x, p0 = [100,0.003, 350, 200])
# #print(popt) 
# axe4.plot(lnspc, fit_function(lnspc,*popt), 'r', label="Post-readout Super Pixel Bright Ion Gaussian fit") # plot it
# #axe4.plot(lnspc, MB_fit(lnspc,*popt), 'r', label="Prereadout Super Pixel Bright Ion Gaussian fit") # plot it
# =============================================================================
a2 = []
for i in bins:
    if i < 211.6:
        
        a2.append(i)
binscenters2 = np.array([0.5*(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x[:len(binscenters2)]
for i in a3:
    if i < 0.00344:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error = sum(a3*binwidth)  
print('bright ion discrimination error from histogram overlap for 3x3 ROI: ' + str(error))   
        
a2 = []
for i in bins1:
    if i > 211.6:
        
        a2.append(i)
binscenters2 = np.array([0.5*(a2[1+i] - a2[i]) for i in range(len(a2)-1)])
binwidth = (a2[2] - a2[1])
a3 = x1[-len(binscenters2):]
for i in a3:
    if i < 0.00336:
        None
    else:
        print(':O')
        print(i)
#print(a3)
#print(binscenters2)
#print(binwidth)
#print(len(binscenters2))   
error1 = sum(a3*binwidth)  
print('dark ion discrimination error from histogram overlap for 3x3 ROI: ' + str(error1))
print(error + error1)

# =============================================================================
# xt1 = plt.xticks()[0]  
# xmin1, xmax1 = min(xt1), max(xt1)  
# lnspc1 = np.linspace(xmin1, xmax1, 10000)
# 
# 
# binscenters1 = np.array([0.5 * (bins1[i] + bins1[i+1]) for i in range(len(bins1)-1)])
# popt1, pcov1 = curve_fit(fit_function, xdata=binscenters1, ydata=x1, p0 = [2000, 200])
# #popt1, pcov1 = curve_fit(MB_fit, xdata=binscenters1, ydata=x1, p0 = [30,0.023, 157, 30])
# #print(popt1)
# axe4.plot(lnspc1, fit_function(lnspc1,*popt1), 'g', label="Post-readout Super Pixel Dark Ion Gaussian fit") 
# #axe4.plot(lnspc1, MB_fit(lnspc1,*popt1), 'g', label="Prereadout Super Pixel Dark Ion Gaussian fit") 
# =============================================================================
axe4.legend(fontsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

# =============================================================================
# result = solve(popt[0],popt1[0],popt[1],popt1[1])
# print(result)
# x1 = 0      
# x2 = result[0]
# #x3 = 9999999999
# 
# Pin = stats.norm.cdf(x2,popt[0],popt[1])
# Pin1 = 1- stats.norm.cdf(x2, popt1[0], popt1[1])#(p_upper1) - (p_lower1)
# print('probability of misinterpreting bright ion as dark ion at 10 ms exposure for 3x3 ROI: ' + str(Pin))
# print('probability of misinterpreting dark ion as bright ion at 10 ms exposure for 3x3 ROI: ' + str(Pin1))
# =============================================================================


plt.show()