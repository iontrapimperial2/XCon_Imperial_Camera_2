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


b1= []
b2= []
b3= []
b4= []
b5= []
b6= []
b7= []
b8= []
b9= []
b10= []
b11= []
b12= []
b13= []
b14= []
b15= []
b16= []
b17= []
b18= []
b19= []
b20= []
b21= []
b22= []
b23= []
b24= []
b25= []


d1= []
d2= []
d3= []
d4= []
d5= []
d6= []
d7= []
d8= []
d9= []
d10= []
d11= []
d12= []
d13= []
d14= []
d15= []
d16= []
d17= []
d18= []
d19= []
d20= []
d21= []
d22= []
d23= []
d24= []
d25= []




for num in range(1,101,1):
    x = list(range(num*5, (100*5), 1))
    y = x +list(range(0, (num-1)*5,1))
    #10 ms
    df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_23_data\Bright\10ms.txt', header = None)
    df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
    df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column
    h2 = df14.drop(y)
    #h2 = [h2.iat[i,j] for i in l1 for j in l2]
    b1.append(h2.iat[0,0])
    #b2.append(h2.iat[0,1])
    #b3.append(h2.iat[0,2])
    #b4.append(h2.iat[0,3])
    #b5.append(h2.iat[0,4])
    #b6.append(h2.iat[1,0])
    b7.append(h2.iat[1,1])
    b8.append(h2.iat[1,2])
    b9.append(h2.iat[1,3])
    #b10.append(h2.iat[1,4])
    #b11.append(h2.iat[2,0])
    b12.append(h2.iat[2,1])
    b13.append(h2.iat[2,2])
    b14.append(h2.iat[2,3])
    #b15.append(h2.iat[2,4])
    #b16.append(h2.iat[3,0])
    b17.append(h2.iat[3,1])
    b18.append(h2.iat[3,2])
    b19.append(h2.iat[3,3])
    #b20.append(h2.iat[3,4])
    #b21.append(h2.iat[4,0])
    #b22.append(h2.iat[4,1])
    #b23.append(h2.iat[4,2])
    #b24.append(h2.iat[4,3])
    #b25.append(h2.iat[4,4])
    
    df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_23_data\Dark\10ms.txt', header = None)
    df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
    df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column
    h3 = df15.drop(y)
    #h3 = [h3.iat[i,j] for i in l1 for j in l2]
    #d1.append(h3.iat[0,0])
    #d2.append(h3.iat[0,1])
    #d3.append(h3.iat[0,2])
    #d4.append(h3.iat[0,3])
    #d5.append(h3.iat[0,4])
    #d6.append(h3.iat[1,0])
    d7.append(h3.iat[1,1])
    d8.append(h3.iat[1,2])
    d9.append(h3.iat[1,3])
    #d10.append(h3.iat[1,4])
    #d11.append(h3.iat[2,0])
    d12.append(h3.iat[2,1])
    d13.append(h3.iat[2,2])
    d14.append(h3.iat[2,3])
    #d15.append(h3.iat[2,4])
    #d16.append(h3.iat[3,0])
    d17.append(h3.iat[3,1])
    d18.append(h3.iat[3,2])
    d19.append(h3.iat[3,3])
    #d20.append(h3.iat[3,4])
    #d21.append(h3.iat[4,0])
    #d22.append(h3.iat[4,1])
    #d23.append(h3.iat[4,2])
    #d24.append(h3.iat[4,3])
    #d25.append(h3.iat[4,4])


    

    












#find intercept of B and D distributions
def solve(m1,m2,std1,std2):
  a = 1/(2*std1**2) - 1/(2*std2**2)
  b = m2/(std2**2) - m1/(std1**2)
  c = m1**2 /(2*std1**2) - m2**2 / (2*std2**2) - np.log(std2/std1)
  return np.roots([a,b,c])

'''
#Histograms
fi = plt.figure('Histogram 10 ms Exposure for 5x5 ROI over 100 Exposures')
fi.suptitle('Histogram of pixel 1 for 10 ms Exposure for 5x5 ROI over 100 Exposures', fontsize=20)
axe = fi.add_subplot(111)
x1, bins1, p1 = axe.hist(b1, density=True, bins = 50)
x2, bins2, p2 = axe.hist(b2, density=True, bins = 50)
x3, bins3, p3 = axe.hist(b3, density=True, bins = 50)
x4, bins4, p4 = axe.hist(b4, density=True, bins = 50)
x5, bins5, p5 = axe.hist(b5, density=True, bins = 50)
x6, bins6, p6 = axe.hist(b6, density=True, bins = 50)
x7, bins7, p7 = axe.hist(b7, density=True, bins = 50)
x8, bins8, p8 = axe.hist(b8, density=True, bins = 50)
x9, bins9, p9 = axe.hist(b9, density=True, bins = 50)
x10, bins10, p10 = axe.hist(b10, density=True, bins = 50)
x11, bins11, p11 = axe.hist(b11, density=True, bins = 50)
x12, bins12, p12 = axe.hist(b12, density=True, bins = 50)
x13, bins13, p13 = axe.hist(b13, density=True, bins = 50)
x14, bins14, p14 = axe.hist(b14, density=True, bins = 50)
x15, bins15, p15 = axe.hist(b15, density=True, bins = 50)
x16, bins16, p16 = axe.hist(b16, density=True, bins = 50)
x17, bins17, p17 = axe.hist(b17, density=True, bins = 50)
x18, bins18, p18 = axe.hist(b18, density=True, bins = 50)
x19, bins19, p19 = axe.hist(b19, density=True, bins = 50)
x20, bins20, p20 = axe.hist(b20, density=True, bins = 50)
x21, bins21, p21 = axe.hist(b21, density=True, bins = 50)
x22, bins22, p22 = axe.hist(b22, density=True, bins = 50)
x23, bins23, p23 = axe.hist(b23, density=True, bins = 50)
x24, bins24, p24 = axe.hist(b24, density=True, bins = 50)
x25, bins25, p25 = axe.hist(b25, density=True, bins = 50)
axe.tick_params(axis='both', labelsize = 16)
'''

xt1 = b1  
xmin1, xmax1 = min(xt1), max(xt1)
lnspc1 = np.linspace(xmin1, xmax1, 10000)
'''
m1, s1 = stats.norm.fit(b1) # get mean and standard deviation  

xt2 = b2  
xmin2, xmax2 = min(xt2), max(xt2)
lnspc2 = np.linspace(xmin2, xmax2, 10000)
m2, s2 = stats.norm.fit(b2) # get mean and standard deviation  

xt3 = b3  
xmin3, xmax3 = min(xt3), max(xt3)
lnspc3 = np.linspace(xmin3, xmax3, 10000)
m3, s3 = stats.norm.fit(b3) # get mean and standard deviation  

xt4 = b4  
xmin4, xmax4 = min(xt4), max(xt4)  
lnspc4 = np.linspace(xmin4, xmax4, 10000)
m4, s4 = stats.norm.fit(b4) # get mean and standard deviation  

xt5 = b5  
xmin5, xmax5 = min(xt5), max(xt5)  
lnspc5 = np.linspace(xmin5, xmax5, 10000)
m5, s5 = stats.norm.fit(b5) # get mean and standard deviation  

xt6 = b6  
xmin6, xmax6 = min(xt6), max(xt6)  
lnspc6 = np.linspace(xmin6, xmax6, 10000)
m6, s6 = stats.norm.fit(b6) # get mean and standard deviation  
'''
xt7 = b7  
xmin7, xmax7 = min(xt7), max(xt7)  
lnspc7 = np.linspace(xmin7, xmax7, 10000)
m7, s7 = stats.norm.fit(b7) # get mean and standard deviation  

xt8 = b8  
xmin8, xmax8 = min(xt8), max(xt8)  
lnspc8 = np.linspace(xmin8, xmax8, 10000)
m8, s8 = stats.norm.fit(b8) # get mean and standard deviation  

xt9 = b9  
xmin9, xmax9 = min(xt9), max(xt9)  
lnspc9 = np.linspace(xmin9, xmax9, 10000)
m9, s9 = stats.norm.fit(b9) # get mean and standard deviation  
'''
xt10 = b10  
xmin10, xmax10 = min(xt10), max(xt10)  
lnspc10 = np.linspace(xmin10, xmax10, 10000)
m10, s10 = stats.norm.fit(b10) # get mean and standard deviation  

xt11 = b11  
xmin11, xmax11 = min(xt11), max(xt11)  
lnspc11 = np.linspace(xmin11, xmax11, 10000)
m11, s11 = stats.norm.fit(b11) # get mean and standard deviation  
'''
xt12 = b12  
xmin12, xmax12 = min(xt12), max(xt12)  
lnspc12 = np.linspace(xmin12, xmax12, 10000)
m12, s12 = stats.norm.fit(b12) # get mean and standard deviation  

xt13 = b13  
xmin13, xmax13 = min(xt13), max(xt13)  
lnspc13 = np.linspace(xmin13, xmax13, 10000)
m13, s13 = stats.norm.fit(b13) # get mean and standard deviation  

xt14 = b14  
xmin14, xmax14 = min(xt14), max(xt14)  
lnspc14 = np.linspace(xmin14, xmax14, 10000)
m14, s14 = stats.norm.fit(b14) # get mean and standard deviation  
'''
xt15 = b15  
xmin15, xmax15 = min(xt15), max(xt15)  
lnspc15 = np.linspace(xmin15, xmax15, 10000)
m15, s15 = stats.norm.fit(b15) # get mean and standard deviation  

xt16 = b16  
xmin16, xmax16 = min(xt16), max(xt16)  
lnspc16 = np.linspace(xmin16, xmax16, 10000)
m16, s16 = stats.norm.fit(b16) # get mean and standard deviation  
'''
xt17 = b17  
xmin17, xmax17 = min(xt17), max(xt17)  
lnspc17 = np.linspace(xmin17, xmax17, 10000)
m17, s17 = stats.norm.fit(b17) # get mean and standard deviation  

xt18 = b18  
xmin18, xmax18 = min(xt18), max(xt18)  
lnspc18 = np.linspace(xmin18, xmax18, 10000)
m18, s18 = stats.norm.fit(b18) # get mean and standard deviation  

xt19 = b19  
xmin19, xmax19 = min(xt19), max(xt19)  
lnspc19 = np.linspace(xmin19, xmax19, 10000)
m19, s19 = stats.norm.fit(b19) # get mean and standard deviation  
'''
xt20 = b20  
xmin20, xmax20 = min(xt20), max(xt20)  
lnspc20 = np.linspace(xmin20, xmax20, 10000)
m20, s20 = stats.norm.fit(b20) # get mean and standard deviation  

xt21 = b21  
xmin21, xmax21 = min(xt21), max(xt21)  
lnspc21 = np.linspace(xmin21, xmax21, 10000)
m21, s21 = stats.norm.fit(b21) # get mean and standard deviation  

xt22 = b22  
xmin22, xmax22 = min(xt22), max(xt22)  
lnspc22 = np.linspace(xmin22, xmax22, 10000)
m22, s22 = stats.norm.fit(b22) # get mean and standard deviation  

xt23 = b23  
xmin23, xmax23 = min(xt23), max(xt23)  
lnspc23 = np.linspace(xmin23, xmax23, 10000)
m23, s23 = stats.norm.fit(b23) # get mean and standard deviation  

xt24 = b24  
xmin24, xmax24 = min(xt24), max(xt24)  
lnspc24 = np.linspace(xmin24, xmax24, 10000)
m24, s24 = stats.norm.fit(b24) # get mean and standard deviation  

xt25 = b25  
xmin25, xmax25 = min(xt25), max(xt25)  
lnspc25 = np.linspace(xmin25, xmax25, 10000)
m25, s25 = stats.norm.fit(b25) # get mean and standard deviation  
'''
'''
xt26 = d1  
xmin26, xmax26 = min(xt26), max(xt26)
lnspc26 = np.linspace(xmin26, xmax26, 10000)
m26, s26 = stats.norm.fit(d1) # get mean and standard deviation  

xt27 = d2  
xmin27, xmax27 = min(xt27), max(xt27)
lnspc27 = np.linspace(xmin27, xmax27, 10000)
m27, s27 = stats.norm.fit(d2) # get mean and standard deviation  

xt28 = d3  
xmin28, xmax28 = min(xt28), max(xt28)
lnspc28 = np.linspace(xmin28, xmax28, 10000)
m28, s28 = stats.norm.fit(d3) # get mean and standard deviation  

xt29 = d4  
xmin29, xmax29 = min(xt29), max(xt29)  
lnspc29 = np.linspace(xmin29, xmax29, 10000)
m29, s29 = stats.norm.fit(d4) # get mean and standard deviation  

xt30 = d5  
xmin30, xmax30 = min(xt30), max(xt30)  
lnspc30 = np.linspace(xmin30, xmax30, 10000)
m30, s30 = stats.norm.fit(d5) # get mean and standard deviation  

xt31 = d6  
xmin31, xmax31 = min(xt31), max(xt31)  
lnspc31 = np.linspace(xmin31, xmax31, 10000)
m31, s31 = stats.norm.fit(d6) # get mean and standard deviation  
'''
xt32 = d7  
xmin32, xmax32 = min(xt32), max(xt32)  
lnspc32 = np.linspace(xmin32, xmax32, 10000)
m32, s32 = stats.norm.fit(d7) # get mean and standard deviation  

xt33 = d8  
xmin33, xmax33 = min(xt33), max(xt33)  
lnspc33 = np.linspace(xmin33, xmax33, 10000)
m33, s33 = stats.norm.fit(d8) # get mean and standard deviation  

xt34 = d9  
xmin34, xmax34 = min(xt34), max(xt34)  
lnspc34 = np.linspace(xmin34, xmax34, 10000)
m34, s34 = stats.norm.fit(d9) # get mean and standard deviation  
'''
xt35 = d10  
xmin35, xmax35 = min(xt35), max(xt35)  
lnspc35 = np.linspace(xmin35, xmax35, 10000)
m35, s35 = stats.norm.fit(d10) # get mean and standard deviation  

xt36 = d11  
xmin36, xmax36 = min(xt36), max(xt36)  
lnspc36 = np.linspace(xmin36, xmax36, 10000)
m36, s36 = stats.norm.fit(d11) # get mean and standard deviation  
'''
xt37 = d12  
xmin37, xmax37 = min(xt37), max(xt37)  
lnspc37 = np.linspace(xmin37, xmax37, 10000)
m37, s37 = stats.norm.fit(d12) # get mean and standard deviation  

xt38 = d13  
xmin38, xmax38 = min(xt38), max(xt38)  
lnspc38 = np.linspace(xmin38, xmax38, 10000)
m38, s38 = stats.norm.fit(d13) # get mean and standard deviation  

xt39 = d14  
xmin39, xmax39 = min(xt39), max(xt39)  
lnspc39 = np.linspace(xmin39, xmax39, 10000)
m39, s39 = stats.norm.fit(d14) # get mean and standard deviation  
'''
xt40 = d15  
xmin40, xmax40 = min(xt40), max(xt40)  
lnspc40 = np.linspace(xmin40, xmax40, 10000)
m40, s40 = stats.norm.fit(d15) # get mean and standard deviation  

xt41 = d16  
xmin41, xmax41 = min(xt41), max(xt41)  
lnspc41 = np.linspace(xmin41, xmax41, 10000)
m41, s41 = stats.norm.fit(d16) # get mean and standard deviation  
'''
xt42 = d17  
xmin42, xmax42 = min(xt42), max(xt42)  
lnspc42 = np.linspace(xmin42, xmax42, 10000)
m42, s42 = stats.norm.fit(d17) # get mean and standard deviation  

xt43 = d18  
xmin43, xmax43 = min(xt43), max(xt43)  
lnspc43 = np.linspace(xmin43, xmax43, 10000)
m43, s43 = stats.norm.fit(d18) # get mean and standard deviation  

xt44 = d19  
xmin44, xmax44 = min(xt44), max(xt44)  
lnspc44 = np.linspace(xmin44, xmax44, 10000)
m44, s44 = stats.norm.fit(d19) # get mean and standard deviation  
'''
xt45 = d20  
xmin45, xmax45 = min(xt45), max(xt45)  
lnspc45 = np.linspace(xmin45, xmax45, 10000)
m45, s45 = stats.norm.fit(d20) # get mean and standard deviation  

xt46 = d21  
xmin46, xmax46 = min(xt46), max(xt46)  
lnspc46 = np.linspace(xmin46, xmax46, 10000)
m46, s46 = stats.norm.fit(d21) # get mean and standard deviation  

xt47 = d22  
xmin47, xmax47 = min(xt47), max(xt47)  
lnspc47 = np.linspace(xmin47, xmax47, 10000)
m47, s47 = stats.norm.fit(d22) # get mean and standard deviation  

xt48 = d23  
xmin48, xmax48 = min(xt48), max(xt48)  
lnspc48 = np.linspace(xmin48, xmax48, 10000)
m48, s48 = stats.norm.fit(d23) # get mean and standard deviation  

xt49 = d24  
xmin49, xmax49 = min(xt49), max(xt49)  
lnspc49 = np.linspace(xmin49, xmax49, 10000)
m49, s49 = stats.norm.fit(d24) # get mean and standard deviation  

xt50 = d25  
xmin50, xmax50 = min(xt50), max(xt50)  
lnspc50 = np.linspace(xmin50, xmax50, 10000)
m50, s50 = stats.norm.fit(d25) # get mean and standard deviation 
'''

fi1 = plt.figure('Maximum Likelihood for 10 ms Exposure for 5x5 ROI over 100 Exposures')
fi1.suptitle('Maximum Likelihood for 10 ms Exposure for 5x5 ROI over 100 Exposures', fontsize=20)
ax = fi1.add_subplot(111)
pdf_g = stats.norm.pdf(lnspc7, m7, s7)*stats.norm.pdf(lnspc7, m8, s8)*stats.norm.pdf(lnspc7, m9, s9)*stats.norm.pdf(lnspc7, m12, s12)*stats.norm.pdf(lnspc7, m13, s13)*stats.norm.pdf(lnspc7, m14, s14)*stats.norm.pdf(lnspc7, m17, s17)*stats.norm.pdf(lnspc7, m18, s18)*stats.norm.pdf(lnspc7, m19, s19) # now get theoretical values in our interval  
ax.plot(lnspc7, 3000*pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") 
pdf_g1 = stats.norm.pdf(lnspc7, m32, s32)*stats.norm.pdf(lnspc7, m33, s33)*stats.norm.pdf(lnspc7, m34, s34)*stats.norm.pdf(lnspc7, m37, s37)*stats.norm.pdf(lnspc7, m38, s38)*stats.norm.pdf(lnspc7, m39, s39)*stats.norm.pdf(lnspc7, m42, s42)*stats.norm.pdf(lnspc7, m43, s43)*stats.norm.pdf(lnspc7, m44, s44) # now get theoretical values in our interval  
ax.plot(lnspc7, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
ax.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

'''
xmin51, xmax51 = -max(pdf_g), max(pdf_g)  
lnspc51 = np.linspace(xmin51, xmax51, 10000)
m51, s51 = stats.norm.fit(pdf_g) # get mean and standard deviation 
pdf_g2 = stats.norm.pdf(lnspc51, m51, s51)

xmin52, xmax52 = -max(pdf_g1), max(pdf_g1)  
lnspc52 = np.linspace(xmin52, xmax52, 10000)
m52, s52 = stats.norm.fit(pdf_g1) # get mean and standard deviation 
pdf_g3= stats.norm.pdf(lnspc52, m52, s52)

fig = plt.figure('Maximum Likelihood for 10 ms Exposure for 5x5 ROI over 100 Exposures')
fig.suptitle('Maximum Likelihood for 10 ms Exposure for 5x5 ROI over 100 Exposures', fontsize=20)
ax1 = fig.add_subplot(111)
ax1.plot(lnspc51, pdf_g2, 'r', label="Super Pixel Bright Ion Gaussian fit") 
ax1.plot(lnspc52, 100000*pdf_g3, 'g', label="Super Pixel Dark Ion Gaussian fit") 
ax1.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
'''
'''
result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 1 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 1 s exposure: ' + str(Pin1))


fi1 = plt.figure('Histogram for 0.5 s Exposure for 3x3 ROI over 100 Exposures')
fi1.suptitle('Bright and Dark Histogram overlap: 0.5 s Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe1 = fi1.add_subplot(111)
x, bins, p = axe1.hist(b, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe1.hist(b1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe1.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(b))
m, s = stats.norm.fit(b) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe1.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(b1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe1.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe1.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 0.5 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 0.5 s exposure: ' + str(Pin1))



fi2 = plt.figure('Histogram for 0.1 s Exposure for 3x3 ROI over 100 Exposures')
fi2.suptitle('Bright and Dark Histogram overlap: 0.1 s Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe2 = fi2.add_subplot(111)
x, bins, p = axe2.hist(c, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe2.hist(c1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe2.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(c))
m, s = stats.norm.fit(c) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe2.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(c1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe2.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe2.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 0.1 s exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 0.1 s exposure: ' + str(Pin1))


fi3 =plt.figure('Histogram for 50 ms Exposure for 3x3 ROI over 100 Exposures')
fi3.suptitle('Bright and Dark Histogram overlap: 50 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe3 = fi3.add_subplot(111)
x, bins, p = axe3.hist(d, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe3.hist(d1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe3.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(d))
m, s = stats.norm.fit(d) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe3.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(d1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe3.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe3.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 50 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 50 ms exposure: ' + str(Pin1))


fi4 = plt.figure('Histogram for 40 ms Exposure for 3x3 ROI over 100 Exposures')
fi4.suptitle('Bright and Dark Histogram overlap: 40 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe4 = fi4.add_subplot(111)
x, bins, p = axe4.hist(e, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe4.hist(e1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe4.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(e))
m, s = stats.norm.fit(e) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe4.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(e1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe4.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe4.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 40 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 40 ms exposure: ' + str(Pin1))


fi5 = plt.figure('Histogram for 30 ms Exposure for 3x3 ROI over 100 Exposures')
fi5.suptitle('Bright and Dark Histogram overlap: 30 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe5 = fi5.add_subplot(111)
x, bins, p = axe5.hist(f, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe5.hist(f1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe5.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(f))
m, s = stats.norm.fit(f) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe5.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(f1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe5.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe5.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 30 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 30 ms exposure: ' + str(Pin1))


fi6 = plt.figure('Histogram for 20 ms Exposure for 3x3 ROI over 100 Exposures')
fi6.suptitle('Bright and Dark Histogram overlap: 20 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe6 = fi6.add_subplot(111)
x, bins, p = axe6.hist(g, density=True, bins = 50, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe6.hist(g1, density=True, bins = 50, label = 'Super Pixel Dark Ion')
axe6.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, len(g))
m, s = stats.norm.fit(g) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe6.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(g1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe6.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe6.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 20 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 20 ms exposure: ' + str(Pin1))


fi7 =plt.figure('Histogram for 10 ms Exposure for 3x3 ROI over 100 Exposures')
fi7.suptitle('Bright and Dark Histogram overlap: 10 ms Exposure for 3x3 ROI over 100 Exposures', fontsize=20)
axe7 = fi7.add_subplot(111)
x, bins, p = axe7.hist(h, density=True, bins = 30, label = 'Super Pixel Bright Ion')
x1, bins1, p1 = axe7.hist(h1, density=True, bins = 30, label = 'Super Pixel Dark Ion')
axe7.tick_params(axis='both', labelsize = 16)
xt = plt.xticks()[0]  
xmin, xmax = min(xt), max(xt)  
lnspc = np.linspace(xmin, xmax, 10000)
m, s = stats.norm.fit(h) # get mean and standard deviation  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
axe7.plot(lnspc, pdf_g, 'r', label="Super Pixel Bright Ion Gaussian fit") # plot it

xt1 = plt.xticks()[0]  
xmin1, xmax1 = min(xt1), max(xt1)  
lnspc1 = np.linspace(xmin1, xmax1, 10000)
m1, s1 = stats.norm.fit(h1) # get mean and standard deviation  
pdf_g1 = stats.norm.pdf(lnspc1, m1, s1) # now get theoretical values in our interval  
axe7.plot(lnspc1, pdf_g1, 'g', label="Super Pixel Dark Ion Gaussian fit") 
axe7.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

result = solve(m,m1,s,s1)
print(result)
x1 = 0      
x2 = result[0]
x3 = 9999999999
double_prob = erf( (x1-m) / (s*sqrt(2)) )
p_lower = double_prob/2
double_prob1 = erf( (x2-m) / (s*sqrt(2)) )
p_upper = double_prob1/2
double_prob2 = erf( (x2-m1) / (s1*sqrt(2)) )
p_lower1 = double_prob2/2
double_prob3 = erf( (x3-m1) / (s1*sqrt(2)) )
p_upper1 = double_prob3/2
Pin = (p_upper) - (p_lower)
Pin1 = (p_upper1) - (p_lower1)
print('probability of misinterpreting bright ion as dark ion at 10 ms exposure: ' + str(Pin))
print('probability of misinterpreting dark ion as bright ion at 10 ms exposure: ' + str(Pin1))
'''


plt.show()