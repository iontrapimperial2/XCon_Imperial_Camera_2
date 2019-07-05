# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\5_sec_exposure\pic1.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\5_sec_exposure\pic1.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column


df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\2_sec_exposure\pic1.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\2_sec_exposure\pic4.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column


df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\1_sec_exposure\pic3.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\1_sec_exposure\pic2.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column


df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\900_ms_exposure\pic3.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column

df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\900_ms_exposure\pic1.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column


df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\800_ms_exposure\pic2.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column

df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\800_ms_exposure\pic1.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column


df10 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\700_ms_exposure\pic5.txt', header = None)
df10.drop(df10.columns[-1], axis=1, inplace=True)  #delete last column
df10.drop(df10.columns[0], axis=1, inplace=True)           #delete first column

df11 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\700_ms_exposure\pic2.txt', header = None)
df11.drop(df11.columns[-1], axis=1, inplace=True)  #delete last column
df11.drop(df11.columns[0], axis=1, inplace=True)           #delete first column


df12 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\600_ms_exposure\pic1.txt', header = None)
df12.drop(df12.columns[-1], axis=1, inplace=True)  #delete last column
df12.drop(df12.columns[0], axis=1, inplace=True)           #delete first column

df13 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\600_ms_exposure\pic5.txt', header = None)
df13.drop(df13.columns[-1], axis=1, inplace=True)  #delete last column
df13.drop(df13.columns[0], axis=1, inplace=True)           #delete first column


df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\500_ms_exposure\pic5.txt', header = None)
df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column

df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\500_ms_exposure\pic2.txt', header = None)
df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column


df16 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\400_ms_exposure\pic3.txt', header = None)
df16.drop(df16.columns[-1], axis=1, inplace=True)  #delete last column
df16.drop(df16.columns[0], axis=1, inplace=True)           #delete first column

df17 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\400_ms_exposure\pic3.txt', header = None)
df17.drop(df17.columns[-1], axis=1, inplace=True)  #delete last column
df17.drop(df17.columns[0], axis=1, inplace=True)           #delete first column


df18 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\300_ms_exposure\pic2.txt', header = None)
df18.drop(df18.columns[-1], axis=1, inplace=True)  #delete last column
df18.drop(df18.columns[0], axis=1, inplace=True)           #delete first column

df19 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\300_ms_exposure\pic2.txt', header = None)
df19.drop(df19.columns[-1], axis=1, inplace=True)  #delete last column
df19.drop(df19.columns[0], axis=1, inplace=True)           #delete first column


df20 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\200_ms_exposure\pic3.txt', header = None)
df20.drop(df20.columns[-1], axis=1, inplace=True)  #delete last column
df20.drop(df20.columns[0], axis=1, inplace=True)           #delete first column

df21 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\200_ms_exposure\pic3.txt', header = None)
df21.drop(df21.columns[-1], axis=1, inplace=True)  #delete last column
df21.drop(df21.columns[0], axis=1, inplace=True)           #delete first column


df22 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Bright\100_ms_exposure\pic5.txt', header = None)
df22.drop(df22.columns[-1], axis=1, inplace=True)  #delete last column
df22.drop(df22.columns[0], axis=1, inplace=True)           #delete first column

df23 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Full_image\Dark\100_ms_exposure\pic4.txt', header = None)
df23.drop(df23.columns[-1], axis=1, inplace=True)  #delete last column
df23.drop(df23.columns[0], axis=1, inplace=True)           #delete first column


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


list4 = np.array(df1).ravel().tolist()
list4.sort(reverse = True)
list5 = sorted(list4)
list6 = list(reversed(list5))


list7 = np.array(df2).ravel().tolist()
list7.sort(reverse = True)
list8 = sorted(list7)
list9 = list(reversed(list8))


list10 = np.array(df3).ravel().tolist()
list10.sort(reverse = True)
list11 = sorted(list10)
list12 = list(reversed(list11))


list13 = np.array(df4).ravel().tolist()
list13.sort(reverse = True)
list14 = sorted(list13)
list15 = list(reversed(list14))


list16 = np.array(df5).ravel().tolist()
list16.sort(reverse = True)
list17 = sorted(list16)
list18 = list(reversed(list17))


list19 = np.array(df6).ravel().tolist()
list19.sort(reverse = True)
list20 = sorted(list19)
list21 = list(reversed(list20))


list22 = np.array(df7).ravel().tolist()
list22.sort(reverse = True)
list23 = sorted(list22)
list24 = list(reversed(list23))


list25 = np.array(df8).ravel().tolist()
list25.sort(reverse = True)
list26 = sorted(list25)
list27 = list(reversed(list26))


list28 = np.array(df9).ravel().tolist()
list28.sort(reverse = True)
list29 = sorted(list28)
list30 = list(reversed(list29))


list31 = np.array(df10).ravel().tolist()
list31.sort(reverse = True)
list32 = sorted(list31)
list33 = list(reversed(list32))


list34 = np.array(df11).ravel().tolist()
list34.sort(reverse = True)
list35 = sorted(list34)
list36 = list(reversed(list35))


list37 = np.array(df12).ravel().tolist()
list37.sort(reverse = True)
list38 = sorted(list37)
list39 = list(reversed(list38))


list40 = np.array(df13).ravel().tolist()
list40.sort(reverse = True)
list41 = sorted(list40)
list42 = list(reversed(list41))


list43 = np.array(df14).ravel().tolist()
list43.sort(reverse = True)
list44 = sorted(list43)
list45 = list(reversed(list44))


list46 = np.array(df15).ravel().tolist()
list46.sort(reverse = True)
list47 = sorted(list46)
list48 = list(reversed(list47))


list49 = np.array(df16).ravel().tolist()
list49.sort(reverse = True)
list50 = sorted(list49)
list51 = list(reversed(list50))


list52 = np.array(df17).ravel().tolist()
list52.sort(reverse = True)
list53 = sorted(list52)
list54 = list(reversed(list53))


list55 = np.array(df18).ravel().tolist()
list55.sort(reverse = True)
list56 = sorted(list55)
list57 = list(reversed(list56))


list58 = np.array(df19).ravel().tolist()
list58.sort(reverse = True)
list59 = sorted(list58)
list60 = list(reversed(list59))


list61 = np.array(df20).ravel().tolist()
list61.sort(reverse = True)
list62 = sorted(list61)
list63 = list(reversed(list62))


list64 = np.array(df21).ravel().tolist()
list64.sort(reverse = True)
list65 = sorted(list64)
list66 = list(reversed(list65))


list67 = np.array(df22).ravel().tolist()
list67.sort(reverse = True)
list68 = sorted(list67)
list69 = list(reversed(list68))


list70 = np.array(df23).ravel().tolist()
list70.sort(reverse = True)
list71 = sorted(list70)
list72 = list(reversed(list71))


'''
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
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(c,r, '.')
ax.set_xlim((0,512))
ax.set_ylim((0,512))
ax.set_aspect('equal')
#fig.show()
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
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.plot(c1,r1, '.')
ax1.set_xlim((0,512))
ax1.set_ylim((0,512))
ax1.set_aspect('equal')
#fig1.show()
#print(data)
'''    
r2 = []
c2 = []
a2 = list69[:7]

    
for j in a2:
    for row in range(df22.shape[0]): 
        for col in range(df22.shape[1]):
            
            if df22.iat[row,col] == j:
                print(row, col)
                r2.append(row)
                c2.append(col)

#data1 = c1, r1
fig2 = plt.figure('brightest_pixels_plot_100_ms')
ax2 = fig2.add_subplot(111)
ax2.plot(c2,r2, '.')
ax2.set_xlim((0,512))
ax2.set_ylim((0,512))
ax2.set_aspect('equal')



                    


'''
plt.figure('Histogram for 5 s Exposure')
plt.title('Bright and Dark Histogram overlap: 5 s Exposure', fontsize=16)
plt.hist(list3[:210], bins = 200)
plt.hist(list6[:210], bins = 200)

plt.figure('Histogram for 2 s Exposure')
plt.title('Bright and Dark Histogram overlap: 2 s Exposure', fontsize=16)
plt.hist(list9[:145], bins = 200)
plt.hist(list12[:145], bins = 200)

plt.figure('Histogram for 1 s Exposure')
plt.title('Bright and Dark Histogram overlap: 1 s Exposure', fontsize=16)
plt.hist(list15[:45], bins = 200)
plt.hist(list18[:150], bins = 200)

plt.figure('Histogram for 0.9 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.9 s Exposure', fontsize=16)
plt.hist(list21[:70], bins = 200)
plt.hist(list24[:180], bins = 200)

plt.figure('Histogram for 0.8 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.8 s Exposure', fontsize=16)
plt.hist(list27[:35], bins = 200)
plt.hist(list30[:180], bins = 200)

plt.figure('Histogram for 0.7 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.7 s Exposure', fontsize=16)
plt.hist(list33[:35], bins = 200)
plt.hist(list36[:180], bins = 200)

plt.figure('Histogram for 0.6 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.6 s Exposure', fontsize=16)
plt.hist(list39[:28], bins = 200)
plt.hist(list42[:180], bins = 200)

plt.figure('Histogram for 0.5 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.5 s Exposure', fontsize=16)
plt.hist(list45[:29], bins = 200)
plt.hist(list48[:180], bins = 200)

plt.figure('Histogram for 0.4 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.4 s Exposure', fontsize=16)
plt.hist(list51[:21], bins = 200)
plt.hist(list54[:180], bins = 200)

plt.figure('Histogram for 0.3 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.3 s Exposure', fontsize=16)
plt.hist(list57[:4], bins = 200)
plt.hist(list60[:100], bins = 200)

plt.figure('Histogram for 0.2 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.2 s Exposure', fontsize=16)
plt.hist(list63[:5], bins = 200)
plt.hist(list66[:100], bins = 200)

plt.figure('Histogram for 0.1 s Exposure')
plt.title('Bright and Dark Histogram overlap: 0.1 s Exposure', fontsize=16)
plt.hist(list69[:7], bins = 200)
plt.hist(list72[:100], bins = 200)


t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0, 2.0, 5.0]
n = [7,5,4,21,29,28,35,35,70,45,145,210]

plt.figure('no. of pixels vs Exposure time')
plt.title('no. of pixels in ROI vs Exposure time')
plt.ylabel('no. of pixels in ROI')
plt.xlabel('Exposure time/s')
plt.plot(t,n, '.')
'''
plt.show()