# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

path = r"C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Exposure_test_with_noise\Experiment_1"
path1 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Exposure_test_with_noise\Experiment_2'
path2 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\Exposure_test_with_noise\Com'


t = np.arange(0.1,2.1,0.1)
counts = []
counts1 = []
counts2 = []

for i in range(1,21,1):
    df = pd.read_csv(path + "\exposure_test_n_" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts.append(a.tolist())
    
for i in range(1,21,1):
    df = pd.read_csv(path1 + "\exposure_test_n_" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts1.append(a.tolist())

for i in range(1,21,1):
    df = pd.read_csv(path2 + "\\exposure_test_n_com_" + str(i) + ".asc", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts2.append(a.tolist())
    

slope, intercept, r_value, p_value, std_err = stats.linregress(t,counts)
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(t,counts1)
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(t,counts2)

line = slope*t+intercept
line1 = slope1*t+intercept1
line2 = slope2*t+intercept2






plt.figure('Experiment 1')

plt.plot(t,counts, '.')
plt.plot (t, line)
plt.xlabel('Exposure Time')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 2')
plt.plot(t,counts1, '.')
plt.plot (t, line1)
plt.xlabel('Exposure Time')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Commercial')
plt.plot(t,counts2, '.')
plt.plot (t, line2)
plt.xlabel('Exposure Time')
plt.ylabel('Mean Signal Count per Pixel')


#plt.plot(t, np.array(counts) - np.array(counts1), '.')

plt.show()