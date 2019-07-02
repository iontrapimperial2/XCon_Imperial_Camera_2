# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Bright\5_sec_exposure\pic1.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column


df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Dark\5_sec_exposure\pic1.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column

#df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ions_tobeanalysed\python\Single_section_3.txt', header = None)
#df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
#df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column


plt.figure('Bright Ion')
plt.title('5 s Exposure Bright Ion', fontsize=16)
plt.imshow(df)

plt.figure('Dark Ion')
plt.title('5 s Exposure Dark Ion', fontsize=16)
plt.imshow(df1)

list1 = np.array(df).ravel().tolist()
list1.sort(reverse = True)
list2 = sorted(list1)
list3 = list(reversed(list2))
print(list3[:50])

list4 = np.array(df1).ravel().tolist()
list4.sort(reverse = True)
list5 = sorted(list4)
list6 = list(reversed(list5))
print(list6[:50])

plt.figure('Histogram')
plt.title('Bright and Dark Histogram overlap', fontsize=16)
plt.hist(list3[:500], bins = 200)#.tolist().sort(reverse = True )[:50]
plt.hist(list6[:500], bins = 200)

'''
fig, axs = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle('5 s Exposure Bright Ion', fontsize=16)
axs[0].imshow(df)
axs[0].invert_yaxis()

axs[1].hist(np.array(df).ravel(), bins = 200)


fig, axs = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle('5 s Exposure Dark Ion', fontsize=16)
axs[0].imshow(df1)
axs[0].invert_yaxis()

axs[1].hist(np.array(df1).ravel(), bins = 200)


fig, axs = plt.subplots(2, 1, constrained_layout=True)
fig.suptitle('1.0 s Exposure', fontsize=16)
axs[0].imshow(df2)
axs[0].invert_yaxis()

axs[1].hist(np.array(df2).ravel(), bins = 200)

a = sum(np.array(df).ravel())
b = sum(np.array(df1).ravel())
c = sum(np.array(df2).ravel())
counts = [a,b,c]
t = [0.1, 0.5, 1.0]

plt.figure()
plt.plot(t,counts)
plt.xlabel('Exposure Time')
'''
plt.show()