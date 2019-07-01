# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

path = r"C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_1"
path1 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_2'
path2 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Com'
path3 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_3'
path4 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_4'
path5 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_5'
path6 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_6'
path7 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_7'

#path = r"C:\Users\yudiw\OneDrive\Documents\Imperial\MSc Optics and Photonics\Summer Project\code\python\XCon_Imperial_Camera_2\CIC_test"
#path1 =r'C:\Users\yudiw\OneDrive\Documents\Imperial\MSc Optics and Photonics\Summer Project\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_2'
#path2 =r'C:\Users\yudiw\OneDrive\Documents\Imperial\MSc Optics and Photonics\Summer Project\code\python\XCon_Imperial_Camera_2\CIC_test\Com'


VSSpeeds = np.array([0.3, 0.5, 0.9, 1.7, 3.3])
counts = []
counts1 = []
counts2 = []
counts3 = []
counts4 = []
counts5 = []
counts6 = []
counts7 = []

for i in range(1,6,1):
    df = pd.read_csv(path + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts.append(a.tolist())

  
for i in range(1,6,1):
    df = pd.read_csv(path1 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts1.append(a.tolist())
    
for i in range(1,6,1):
    df = pd.read_csv(path3 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts3.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path4 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts4.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path5 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts5.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path6 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts6.append(a.tolist())
    
for i in range(1,6,1):
    df = pd.read_csv(path7 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts7.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path2 + "\\test" + str(i) + ".asc", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts2.append(a.tolist())
 
'''
slope, intercept, r_value, p_value, std_err = stats.linregress(VSSpeeds,counts)
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(VSSpeeds,counts1)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(VSSpeeds,counts2)

line = slope*VSSpeeds+intercept
line1 = slope1*VSSpeeds+intercept1
line2 = slope2*VSSpeeds+intercept2
'''





plt.figure('Experiment 1')

plt.plot(VSSpeeds,counts, '.')
#plt.plot (VSSpeeds, line)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 2')
plt.plot(VSSpeeds,counts1, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Commercial')
plt.plot(VSSpeeds,counts2, '.')
#plt.plot (VSSpeeds, line2)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 3')
plt.plot(VSSpeeds,counts3, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 4')
plt.plot(VSSpeeds,counts4, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 5')
plt.plot(VSSpeeds,counts5, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 6')
plt.plot(VSSpeeds,counts6, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 7')
plt.plot(VSSpeeds,counts7, '.')
#plt.plot (VSSpeeds, line1)
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

#plt.plot(t, np.array(counts) - np.array(counts1), '.')

plt.show()