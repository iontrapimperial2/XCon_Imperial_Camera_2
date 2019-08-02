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

l1 = [1,2,3]
l2 = [1,2,3]

#bright
a = []     #1 sec
b = []    #0.5 sec
c = []    #0.1 sec
d = []    #50 ms
e = []    #40 ms
f = []   #30 ms
g = []   #20 ms
h = []   #10 ms


#dark
a1 = []   #1 sec
b1 = []   #0.5 sec
c1 = []   #0.1 sec
d1 = []   #50 ms
e1 = []   #40 ms
f1 = []  #30 ms
g1 = []  #20 ms
h1 = []  #10 ms

for i in range(1,10,1):

    #1 sec
    df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\1s' + str(i) + '.txt', header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
    
    df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\1t' + str(i) + '.txt', header = None)
    df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
    df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
    
    #0.5 sec
    df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\05s' + str(i) + '.txt', header = None)
    df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
    df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
    
    df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\05t' + str(i) + '.txt', header = None)
    df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
    df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column
    
    #0.1 sec
    df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\01s' + str(i) + '.txt', header = None)
    df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
    df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column
    
    df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\01t' + str(i) + '.txt', header = None)
    df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
    df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column
    
    #50 ms
    df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\005s' + str(i) + '.txt', header = None)
    df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
    df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column
    
    df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\005t' + str(i) + '.txt', header = None)
    df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
    df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column
    
    #40 ms
    df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\004s' + str(i) + '.txt', header = None)
    df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
    df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column
    
    df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\004t' + str(i) + '.txt', header = None)
    df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
    df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column
    
    #30 ms
    df10 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\003s' + str(i) + '.txt', header = None)
    df10.drop(df10.columns[-1], axis=1, inplace=True)  #delete last column
    df10.drop(df10.columns[0], axis=1, inplace=True)           #delete first column
    
    df11 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\003t' + str(i) + '.txt', header = None)
    df11.drop(df11.columns[-1], axis=1, inplace=True)  #delete last column
    df11.drop(df11.columns[0], axis=1, inplace=True)           #delete first column
    
    #20 ms
    df12 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\002s' + str(i) + '.txt', header = None)
    df12.drop(df12.columns[-1], axis=1, inplace=True)  #delete last column
    df12.drop(df12.columns[0], axis=1, inplace=True)           #delete first column
    
    df13 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\002t' + str(i) + '.txt', header = None)
    df13.drop(df13.columns[-1], axis=1, inplace=True)  #delete last column
    df13.drop(df13.columns[0], axis=1, inplace=True)           #delete first column
    
    #10 ms
    df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\001s' + str(i) + '.txt', header = None)
    df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
    df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column
    
    df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\001t' + str(i) + '.txt', header = None)
    df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
    df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column

    
    #bright
    a2 = [sum([df.iat[1,2],df.iat[2,1],df.iat[2,2],df.iat[2,3],df.iat[3,2]])]     #1 sec
    a = a + a2
    
    b2 = [sum([df2.iat[1,2],df2.iat[2,1],df2.iat[2,2],df2.iat[2,3],df2.iat[3,2]])]    #0.5 sec
    b = b + b2
    
    c2 = [sum([df4.iat[1,2],df4.iat[2,1],df4.iat[2,2],df4.iat[2,3],df4.iat[3,2]])]     #0.1 sec
    c = c + c2
    
    d2 = [sum([df6.iat[1,2],df6.iat[2,1],df6.iat[2,2],df6.iat[2,3],df6.iat[3,2]])]     #50 ms
    d = d + d2
    
    e2 = [sum([df8.iat[1,2],df8.iat[2,1],df8.iat[2,2],df8.iat[2,3],df8.iat[3,2]])]     #40 ms
    e = e + e2
    
    f2 = [sum([df10.iat[1,2],df10.iat[2,1],df10.iat[2,2],df10.iat[2,3],df10.iat[3,2]])]    #30 ms
    f = f + f2
    
    g2 = [sum([df12.iat[1,2],df12.iat[2,1],df12.iat[2,2],df12.iat[2,3],df12.iat[3,2]])]    #20 ms
    g = g + g2
    
    h2 = [sum([df14.iat[1,2],df14.iat[2,1],df14.iat[2,2],df14.iat[2,3],df14.iat[3,2]])]    #10 ms
    h = h + h2


    #dark
    a3 = [sum([df1.iat[1,2],df1.iat[2,1],df1.iat[2,2],df1.iat[2,3],df1.iat[3,2]])]    #1 sec
    a1 = a1 + a3
    
    b3 = [sum([df3.iat[1,2],df3.iat[2,1],df3.iat[2,2],df3.iat[2,3],df3.iat[3,2]])]    #0.5 sec
    b1 = b1 + b3
    
    c3 = [sum([df5.iat[1,2],df5.iat[2,1],df5.iat[2,2],df5.iat[2,3],df5.iat[3,2]])]    #0.1 sec
    c1 = c1 + c3
    
    d3 = [sum([df7.iat[1,2],df7.iat[2,1],df7.iat[2,2],df7.iat[2,3],df7.iat[3,2]])]    #50 ms
    d1 = d1 + d3
    
    e3 = [sum([df9.iat[1,2],df9.iat[2,1],df9.iat[2,2],df9.iat[2,3],df9.iat[3,2]])]    #40 ms
    e1 = e1 + e3
    
    f3 = [sum([df11.iat[1,2],df11.iat[2,1],df11.iat[2,2],df11.iat[2,3],df11.iat[3,2]])]   #30 ms
    f1 = f1 + f3
    
    g3 = [sum([df13.iat[1,2],df13.iat[2,1],df13.iat[2,2],df13.iat[2,3],df13.iat[3,2]])]   #20 ms
    g1 = g1 + g3
    
    h3 = [sum([df15.iat[1,2],df15.iat[2,1],df15.iat[2,2],df15.iat[2,3],df15.iat[3,2]])]   #10 ms
    h1 = h1 + h3





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

fig = plt.figure('Difference Between Mean Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 9 Exposures')
fig.suptitle('Difference Between Mean Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 9 Exposures', fontsize=20)
axes = fig.add_subplot(111)
#axes.plot(t,diff,'.')
axes.errorbar(t,diff,yerr=err, fmt = 'x')
axes.plot(t,line)
axes.tick_params(axis = 'both', labelsize =16)
plt.ylabel('Count reading', fontsize=18)
plt.xlabel('Exposure time/s', fontsize=18)


#bright
a6 = sum(a)    #1 sec
b6 = sum(b)    #0.5 sec
c6 = sum(c)    #0.1 sec
d6 = sum(d)    #50 ms
e6 = sum(e)    #40 ms
f6 = sum(f)    #30 ms
g6 = sum(g)    #20 ms
h6 = sum(h)    #10 ms


#dark
a7 = sum(a1)   #1 sec
b7 = sum(b1)   #0.5 sec
c7 = sum(c1)   #0.1 sec
d7 = sum(d1)   #50 ms
e7 = sum(e1)   #40 ms
f7 = sum(f1)   #30 ms
g7 = sum(g1)   #20 ms
h7 = sum(h1)   #10 ms

diff1 = [a6-a7,b6-b7,c6-c7,d6-d7,e6-e7,f6-f7,g6-g7,h6-h7]


slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(t,diff1)
line1 = [slope1*i+intercept1 for i in t]


fig1 = plt.figure('Difference Between Total Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 9 Exposures')
fig1.suptitle('Difference Between Total Bright and Dark Ion Reading vs Exposure Time with 3x3 ROI over 9 Exposures', fontsize=20)
axes1 = fig1.add_subplot(111)
axes1.plot(t,diff1,'.')
axes1.plot(t,line1)
axes1.tick_params(axis = 'both', labelsize =16)
plt.ylabel('Count reading', fontsize=18)
plt.xlabel('Exposure time/s', fontsize=18)






#Histograms
fi = plt.figure('Histogram for 1 s Exposure for 3x3 ROI at 1000 gain over 9 Exposures')
fi.suptitle('Bright and Dark Histogram overlap: 1 s Exposure for 3x3 ROI at 1000 gain over 9 Exposures', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe.hist(a1, density=True, bins = 81, label = 'Dark Ion')
axe.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(a))
m, s = stats.norm.fit(a) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(a1))
m1, s1 = stats.norm.fit(a1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe.legend(fontsize = 16)
#axe.set_xlim((0,5000))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi1 = plt.figure('Histogram for 0.5 s Exposure for 3x3 ROI at 1000 gain over 9 Exposures')
fi1.suptitle('Bright and Dark Histogram overlap: 0.5 s Exposure for 3x3 ROI over 9 Exposures', fontsize=20)
axe1 = fi1.add_subplot(111)
x, bins, p = axe1.hist(b, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe1.hist(b1, density=True, bins = 81, label = 'Dark Ion')
axe1.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(b))
m, s = stats.norm.fit(b) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe1.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(b1))
m1, s1 = stats.norm.fit(b1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe1.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe1.legend(fontsize = 16)
#axe1.set_xlim((0,2500))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)



fi2 = plt.figure('Histogram for 0.1 s Exposure for 3x3 ROI over 9 Exposures')
fi2.suptitle('Bright and Dark Histogram overlap: 0.1 s Exposure for 3x3 ROI over 9 Exposures', fontsize=20)
axe2 = fi2.add_subplot(111)
x, bins, p = axe2.hist(c, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe2.hist(c1, density=True, bins = 81, label = 'Dark Ion')
axe2.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(c))
m, s = stats.norm.fit(c) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe2.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(c1))
m1, s1 = stats.norm.fit(c1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe2.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe2.legend(fontsize = 16)
#axe2.set_xlim((0,1000))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi3 =plt.figure('Histogram for 50 ms Exposure for 3x3 ROI over 9 Exposures')
fi3.suptitle('Bright and Dark Histogram overlap: 50 ms Exposure for 3x3 ROI gain over 9 Exposures', fontsize=20)
axe3 = fi3.add_subplot(111)
x, bins, p = axe3.hist(d, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe3.hist(d1, density=True, bins = 81, label = 'Dark Ion')
axe3.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(d))
m, s = stats.norm.fit(d) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe3.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(d1))
m1, s1 = stats.norm.fit(d1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe3.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe3.legend(fontsize = 16)
#axe3.set_xlim((0,800))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi4 = plt.figure('Histogram for 40 ms Exposure for 3x3 ROI over 9 Exposures')
fi4.suptitle('Bright and Dark Histogram overlap: 40 ms Exposure for 3x3 ROI over 9 Exposures', fontsize=20)
axe4 = fi4.add_subplot(111)
x, bins, p = axe4.hist(e, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe4.hist(e1, density=True, bins = 81, label = 'Dark Ion')
axe4.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(e))
m, s = stats.norm.fit(e) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe4.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(e1))
m1, s1 = stats.norm.fit(e1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe4.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe4.legend(fontsize = 16)
#axe4.set_xlim((0,800))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi5 = plt.figure('Histogram for 30 ms Exposure for 3x3 ROI over 9 Exposures')
fi5.suptitle('Bright and Dark Histogram overlap: 30 ms Exposure for 3x3 ROI over 9 Exposures', fontsize=20)
axe5 = fi5.add_subplot(111)
x, bins, p = axe5.hist(f, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe5.hist(f1, density=True, bins = 81, label = 'Dark Ion')
axe5.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(f))
m, s = stats.norm.fit(f) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe5.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(f1))
m1, s1 = stats.norm.fit(f1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe5.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe5.legend(fontsize = 16)
#axe5.set_xlim((100,700))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi6 = plt.figure('Histogram for 20 ms Exposure for 3x3 ROI over 9 Exposures')
fi6.suptitle('Bright and Dark Histogram overlap: 20 ms Exposure for 3x3 ROI gain over 9 Exposures', fontsize=20)
axe6 = fi6.add_subplot(111)
x, bins, p = axe6.hist(g, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe6.hist(g1, density=True, bins = 81, label = 'Dark Ion')
axe6.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(g))
m, s = stats.norm.fit(g) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe6.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(g1))
m1, s1 = stats.norm.fit(g1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe6.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe6.legend(fontsize = 16)
#axe6.set_xlim((100,600))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)


fi7 =plt.figure('Histogram for 10 ms Exposure for 3x3 ROI over 9 Exposures')
fi7.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 3x3 ROI over 9 Exposures', fontsize=20)
axe7 = fi7.add_subplot(111)
x, bins, p = axe7.hist(h, density=True, bins = 81, label = 'Bright Ion')
x1, bins1, p1 = axe7.hist(h1, density=True, bins = 81, label = 'Dark Ion')
axe7.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(h))
m, s = stats.norm.fit(h) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe7.plot(lnspc, pdf_g, 'r', label="Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, len(h1))
m1, s1 = stats.norm.fit(h1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe7.plot(lnspc1, pdf_g1, 'g', label="Dark Ion Gaussian fit") 
axe7.legend(fontsize = 16)
#axe7.set_xlim((100,700))
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
plt.show()