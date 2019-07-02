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
path8 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_8'
path9 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_9'
path10 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_10'
path11 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_11'
path12 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Com_1'
path13 =r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\Experiment_12'

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
counts8 = []
counts9 = []
counts10 = []
counts11 = []
counts12 = []
counts13 = []

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
    df = pd.read_csv(path8 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts8.append(a.tolist())
    
for i in range(1,6,1):
    df = pd.read_csv(path9 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts9.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path10 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts10.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path11 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts11.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path13 + "\\test" + str(i) + ".txt", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts13.append(a.tolist())

for i in range(1,6,1):
    df = pd.read_csv(path2 + "\\test" + str(i) + ".asc", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts2.append(a.tolist())
 
for i in range(1,6,1):
    df = pd.read_csv(path12 + "\\test" + str(i) + ".asc", header = None)
    df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
    df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

    a = sum(np.array(df).ravel())/(512**2)
    counts12.append(a.tolist())

"""
plt.figure('Experiment 1')

plt.plot(VSSpeeds,counts, '.')
plt.title('Vertical Clock Voltage Amplitude +2V')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 2')
plt.title('Vertical Clock Voltage Amplitude +2V')
plt.plot(VSSpeeds,counts1, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Commercial 1')
plt.title('Vertical Clock Voltage Amplitude +2V')
plt.plot(VSSpeeds,counts2, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 3')
plt.title('Vertical Clock Voltage Amplitude +3V')
plt.plot(VSSpeeds,counts3, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 4')
plt.title('Vertical Clock Voltage Amplitude +3V')
plt.plot(VSSpeeds,counts4, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 5')
plt.title('Vertical Clock Voltage Amplitude +4V')
plt.plot(VSSpeeds,counts5, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 6')
plt.title('Vertical Clock Voltage Amplitude 0V')
plt.plot(VSSpeeds,counts6, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 7')
plt.title('Vertical Clock Voltage Amplitude 0V')
plt.plot(VSSpeeds,counts7, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 8')
plt.title('Vertical Clock Voltage Amplitude +1V')
plt.plot(VSSpeeds,counts8, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 9')
plt.title('Vertical Clock Voltage Amplitude +2V')
plt.plot(VSSpeeds,counts9, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 10')
plt.title('Vertical Clock Voltage Amplitude 0V')
plt.plot(VSSpeeds,counts10, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Experiment 11')
plt.title('Vertical Clock Voltage Amplitude +1V')
plt.plot(VSSpeeds,counts11, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')

plt.figure('Commercial 2')
plt.title('Vertical Clock Voltage Amplitude 0V')
plt.plot(VSSpeeds,counts12, '.')
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')
"""

plt.figure('Comparison')
plt.title('Noise vs. Vertical Shift Speed for' + '\n ' + 'Vertical Clock Voltage Amplitudes 0 V to +4 V')
line1, = plt.plot(VSSpeeds,counts7)
line2, = plt.plot(VSSpeeds,counts11)
line3, = plt.plot(VSSpeeds,counts9)
line4, = plt.plot(VSSpeeds,counts4)
line5, = plt.plot(VSSpeeds,counts5)
plt.legend((line1, line2, line3, line4, line5), ('0 V', '+1 V', '+2 V', '+3 V', '+4 V'))
plt.xlabel('Vertical Shift speed/ \u03BCs')
plt.ylabel('Mean Signal Count per Pixel')
#plt.plot(t, np.array(counts) - np.array(counts1), '.')

plt.show()