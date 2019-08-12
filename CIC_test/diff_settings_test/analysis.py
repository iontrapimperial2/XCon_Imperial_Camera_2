# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 10:58:02 2019

@author: iontrap
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#7x7
df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\0V_05microsec.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
a = np.array(df).ravel().tolist()

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\1V_05microsec.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column
a1 = np.array(df1).ravel().tolist()

#6x6
df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\2V_05microsec.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column
b = np.array(df2).ravel().tolist()

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\3V_05microsec.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column
b1 = np.array(df3).ravel().tolist()

#5x5
df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\4V_05microsec.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column
c = np.array(df4).ravel().tolist()

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\CIC_test\diff_settings_test\2V_03microsec.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column
c1 = np.array(df5).ravel().tolist()

print(np.mean(a), np.std(a))
print(np.mean(a1), np.std(a1))
print(np.mean(b), np.std(b))
print(np.mean(b1), np.std(b1))
print(np.mean(c), np.std(c))
print(np.mean(c1), np.std(c1))


fi = plt.figure('Histogram for Background 1 sec exposure with 0V and 0.5 microsec vertical shift')
fi.suptitle('Histogram for Background 1 sec exposure with 0V and 0.5 microsec vertical shift', fontsize=20)
axe = fi.add_subplot(111)
x, bins, p = axe.hist(a, density=True, bins = 150, label = '0V and 0.5 microsec vertical shift')
axe.tick_params(axis='both', labelsize = 16)
#axe.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

fi1 = plt.figure('Histogram for Background 1 sec exposure with 1V and 0.5 microsec vertical shift')
fi1.suptitle('Histogram for Background 1 sec exposure with 1V and 0.5 microsec vertical shift', fontsize=20)
axe1 = fi1.add_subplot(111)
x1, bins1, p1 = axe.hist(a1, density=True, bins = 150, label = '1V and 0.5 microsec vertical shift')
axe1.tick_params(axis='both', labelsize = 16)
axe1.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

fi2 = plt.figure('Histogram for Background 1 sec exposure with 2V and 0.5 microsec vertical shift')
fi2.suptitle('Histogram for Background 1 sec exposure with 2V and 0.5 microsec vertical shift', fontsize=20)
axe2 = fi2.add_subplot(111)
x2, bins2, p2 = axe.hist(b, density=True, bins = 150, label = '2V and 0.5 microsec vertical shift')
axe2.tick_params(axis='both', labelsize = 16)
axe2.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

fi3 = plt.figure('Histogram for Background 1 sec exposure with 3V and 0.5 microsec vertical shift')
fi3.suptitle('Histogram for Background 1 sec exposure with 3V and 0.5 microsec vertical shift', fontsize=20)
axe3 = fi3.add_subplot(111)
x3, bins3, p3 = axe.hist(b1, density=True, bins = 150, label = '3V and 0.5 microsec vertical shift')
axe3.tick_params(axis='both', labelsize = 16)
axe3.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)

fi4 = plt.figure('Histogram for Background 1 sec exposure with 4V and 0.5 microsec vertical shift')
fi4.suptitle('Histogram for Background 1 sec exposure with 4V and 0.5 microsec vertical shift', fontsize=20)
axe4 = fi4.add_subplot(111)
x4, bins4, p4 = axe.hist(c, density=True, bins = 150, label = '4V and 0.5 microsec vertical shift')
axe4.tick_params(axis='both', labelsize = 16)
axe4.legend(fontsize = 16)
plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
axe.legend(fontsize = 16)

fi5 = plt.figure('Histogram for Background 1 sec exposure with 2V and 0.3 microsec vertical shift')
fi5.suptitle('Histogram for Background 1 sec exposure with 2V and 0.3 microsec vertical shift', fontsize=20)
axe5 = fi5.add_subplot(111)
x5, bins5, p5 = axe.hist(c1, density=True, bins = 150, label = '2V and 0.3 microsec vertical shift')
axe5.tick_params(axis='both', labelsize = 16)

plt.xlabel('Count reading', fontsize=18)
plt.ylabel('Probability Density', fontsize=18)
''''''
plt.show()










