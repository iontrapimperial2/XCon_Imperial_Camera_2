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

df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Bright\2_sec_exposure\pic1.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Dark\2_sec_exposure\pic4.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column

'''
plt.figure('5 s Exposure Bright Ion')
plt.title('5 s Exposure Bright Ion', fontsize=16)
plt.imshow(df)

plt.figure('5 s Exposure Dark Ion')
plt.title('5 s Exposure Dark Ion', fontsize=16)
plt.imshow(df1)

plt.figure('2 s Exposure Bright Ion')
plt.title('2 s Exposure Bright Ion', fontsize=16)
plt.imshow(df2)

plt.figure('2 s Exposure Dark Ion')
plt.title('2 s Exposure Dark Ion', fontsize=16)
plt.imshow(df3)
'''
list1 = np.array(df).ravel().tolist()
list1.sort(reverse = True)
list2 = sorted(list1)
list3 = list(reversed(list2))
print(list3[:50])

list4 = np.array(df1).ravel().tolist()
list4.sort(reverse = True)
list5 = sorted(list4)
list6 = list(reversed(list5))
#print(list6[:50])

list7 = np.array(df2).ravel().tolist()
list7.sort(reverse = True)
list8 = sorted(list7)
list9 = list(reversed(list8))
#print(list9[:50])

list10 = np.array(df3).ravel().tolist()
list10.sort(reverse = True)
list11 = sorted(list10)
list12 = list(reversed(list11))
#print(list12[:50])

r = []
c = []
a = list3[:210]

    
for i in a:
    for row in range(df.shape[0]): 
        for col in range(df.shape[1]):
            
            if df.iat[row,col] == i:
                print(row, col)
                r.append(row)
                c.append(col)
#data = c, r
plt.figure()
plt.plot(c,r, '.')
plt.xlim((0,512))
plt.ylim((0,512))
#print(data)



r1 = []
c1 = []
a1 = list9[:145]

    
for j in a1:
    for row in range(df2.shape[0]): 
        for col in range(df2.shape[1]):
            
            if df2.iat[row,col] == j:
                print(row, col)
                r1.append(row)
                c1.append(col)

#data1 = c1, r1
plt.figure()
plt.plot(c1,r1, '.')
plt.xlim((0,512))
plt.ylim((0,512))
#print(data)
    



                    


'''
plt.figure('Histogram for 5 s Exposure')
plt.title('Bright and Dark Histogram overlap: 5 s Exposure', fontsize=16)
plt.hist(list3[:210], bins = 200)
plt.hist(list6[:210], bins = 200)

plt.figure('Histogram for 2 s Exposure')
plt.title('Bright and Dark Histogram overlap: 2 s Exposure', fontsize=16)
plt.hist(list9[:145], bins = 200)
plt.hist(list12[:145], bins = 200)
'''

plt.show()