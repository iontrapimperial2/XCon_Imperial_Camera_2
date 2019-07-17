# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\5_sec_exposure\pic2.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\5_sec_exposure\pic1.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column


df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\2_sec_exposure\pic5.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\2_sec_exposure\pic2.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column


df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\1_sec_exposure\pic5.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\1_sec_exposure\pic2.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column


df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\900_ms_exposure\pic3.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column

df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\900_ms_exposure\pic4.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column


df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\800_ms_exposure\pic3.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column

df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\800_ms_exposure\pic4.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column


df10 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\700_ms_exposure\pic3.txt', header = None)
df10.drop(df10.columns[-1], axis=1, inplace=True)  #delete last column
df10.drop(df10.columns[0], axis=1, inplace=True)           #delete first column

df11 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\700_ms_exposure\pic4.txt', header = None)
df11.drop(df11.columns[-1], axis=1, inplace=True)  #delete last column
df11.drop(df11.columns[0], axis=1, inplace=True)           #delete first column


df12 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\600_ms_exposure\pic3.txt', header = None)
df12.drop(df12.columns[-1], axis=1, inplace=True)  #delete last column
df12.drop(df12.columns[0], axis=1, inplace=True)           #delete first column

df13 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\600_ms_exposure\pic5.txt', header = None)
df13.drop(df13.columns[-1], axis=1, inplace=True)  #delete last column
df13.drop(df13.columns[0], axis=1, inplace=True)           #delete first column


df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\500_ms_exposure\pic4.txt', header = None)
df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column

df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\500_ms_exposure\pic2.txt', header = None)
df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column


df16 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\400_ms_exposure\pic2.txt', header = None)
df16.drop(df16.columns[-1], axis=1, inplace=True)  #delete last column
df16.drop(df16.columns[0], axis=1, inplace=True)           #delete first column

df17 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\400_ms_exposure\pic2.txt', header = None)
df17.drop(df17.columns[-1], axis=1, inplace=True)  #delete last column
df17.drop(df17.columns[0], axis=1, inplace=True)           #delete first column


df18 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\300_ms_exposure\pic2.txt', header = None)
df18.drop(df18.columns[-1], axis=1, inplace=True)  #delete last column
df18.drop(df18.columns[0], axis=1, inplace=True)           #delete first column

df19 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\300_ms_exposure\pic2.txt', header = None)
df19.drop(df19.columns[-1], axis=1, inplace=True)  #delete last column
df19.drop(df19.columns[0], axis=1, inplace=True)           #delete first column


df20 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\200_ms_exposure\pic4.txt', header = None)
df20.drop(df20.columns[-1], axis=1, inplace=True)  #delete last column
df20.drop(df20.columns[0], axis=1, inplace=True)           #delete first column

df21 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\200_ms_exposure\pic4.txt', header = None)
df21.drop(df21.columns[-1], axis=1, inplace=True)  #delete last column
df21.drop(df21.columns[0], axis=1, inplace=True)           #delete first column


df22 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\100_ms_exposure\pic3.txt', header = None)
df22.drop(df22.columns[-1], axis=1, inplace=True)  #delete last column
df22.drop(df22.columns[0], axis=1, inplace=True)           #delete first column

df23 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\100_ms_exposure\pic3.txt', header = None)
df23.drop(df23.columns[-1], axis=1, inplace=True)  #delete last column
df23.drop(df23.columns[0], axis=1, inplace=True)           #delete first column


df24 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\Higher_gain\50_ms_exposure\pic8.txt', header = None)
df24.drop(df24.columns[-1], axis=1, inplace=True)  #delete last column
df24.drop(df24.columns[0], axis=1, inplace=True)           #delete first column

df25 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\Higher_gain\50_ms_exposure\pic10.txt', header = None)
df25.drop(df25.columns[-1], axis=1, inplace=True)  #delete last column
df25.drop(df25.columns[0], axis=1, inplace=True)           #delete first column


df26 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\Higher_gain\40_ms_exposure\pic1.txt', header = None)
df26.drop(df26.columns[-1], axis=1, inplace=True)  #delete last column
df26.drop(df26.columns[0], axis=1, inplace=True)           #delete first column

df27 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\Higher_gain\40_ms_exposure\pic7.txt', header = None)
df27.drop(df27.columns[-1], axis=1, inplace=True)  #delete last column
df27.drop(df27.columns[0], axis=1, inplace=True)           #delete first column


df28 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\Higher_gain\30_ms_exposure\pic1.txt', header = None)
df28.drop(df28.columns[-1], axis=1, inplace=True)  #delete last column
df28.drop(df28.columns[0], axis=1, inplace=True)           #delete first column

df29 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\Higher_gain\30_ms_exposure\pic1.txt', header = None)
df29.drop(df29.columns[-1], axis=1, inplace=True)  #delete last column
df29.drop(df29.columns[0], axis=1, inplace=True)           #delete first column


df30 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\Higher_gain\20_ms_exposure\pic1.txt', header = None)
df30.drop(df30.columns[-1], axis=1, inplace=True)  #delete last column
df30.drop(df30.columns[0], axis=1, inplace=True)           #delete first column

df31 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\Higher_gain\20_ms_exposure\pic1.txt', header = None)
df31.drop(df31.columns[-1], axis=1, inplace=True)  #delete last column
df31.drop(df31.columns[0], axis=1, inplace=True)           #delete first column


df32 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Bright_section\Higher_gain\10_ms_exposure\pic1.txt', header = None)
df32.drop(df32.columns[-1], axis=1, inplace=True)  #delete last column
df32.drop(df32.columns[0], axis=1, inplace=True)           #delete first column

df33 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\Dark_section\Higher_gain\10_ms_exposure\pic1.txt', header = None)
df33.drop(df33.columns[-1], axis=1, inplace=True)  #delete last column
df33.drop(df33.columns[0], axis=1, inplace=True)           #delete first column



'''
plt.figure('5 s Exposure Bright Ion')
plt.title('5 s Exposure Bright Ion', fontsize=16)
plt.imshow(df, origin='lower')

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
#5 sec
list1 = np.array(df).ravel().tolist()
list1.sort(reverse = True)
list2 = sorted(list1)
list3 = list(reversed(list2))


list4 = np.array(df1).ravel().tolist()
list4.sort(reverse = True)
list5 = sorted(list4)
list6 = list(reversed(list5))

#2 sec
list7 = np.array(df2).ravel().tolist()
list7.sort(reverse = True)
list8 = sorted(list7)
list9 = list(reversed(list8))


list10 = np.array(df3).ravel().tolist()
list10.sort(reverse = True)
list11 = sorted(list10)
list12 = list(reversed(list11))

#1 sec
list13 = np.array(df4).ravel().tolist()
list13.sort(reverse = True)
list14 = sorted(list13)
list15 = list(reversed(list14))


list16 = np.array(df5).ravel().tolist()
list16.sort(reverse = True)
list17 = sorted(list16)
list18 = list(reversed(list17))

#0.9 sec
list19 = np.array(df6).ravel().tolist()
list19.sort(reverse = True)
list20 = sorted(list19)
list21 = list(reversed(list20))


list22 = np.array(df7).ravel().tolist()
list22.sort(reverse = True)
list23 = sorted(list22)
list24 = list(reversed(list23))

#0.8 sec
list25 = np.array(df8).ravel().tolist()
list25.sort(reverse = True)
list26 = sorted(list25)
list27 = list(reversed(list26))


list28 = np.array(df9).ravel().tolist()
list28.sort(reverse = True)
list29 = sorted(list28)
list30 = list(reversed(list29))

#0.7 sec
list31 = np.array(df10).ravel().tolist()
list31.sort(reverse = True)
list32 = sorted(list31)
list33 = list(reversed(list32))


list34 = np.array(df11).ravel().tolist()
list34.sort(reverse = True)
list35 = sorted(list34)
list36 = list(reversed(list35))

#0.6 sec
list37 = np.array(df12).ravel().tolist()
list37.sort(reverse = True)
list38 = sorted(list37)
list39 = list(reversed(list38))


list40 = np.array(df13).ravel().tolist()
list40.sort(reverse = True)
list41 = sorted(list40)
list42 = list(reversed(list41))

#0.5 sec
list43 = np.array(df14).ravel().tolist()
list43.sort(reverse = True)
list44 = sorted(list43)
list45 = list(reversed(list44))


list46 = np.array(df15).ravel().tolist()
list46.sort(reverse = True)
list47 = sorted(list46)
list48 = list(reversed(list47))

#0.4 sec
list49 = np.array(df16).ravel().tolist()
list49.sort(reverse = True)
list50 = sorted(list49)
list51 = list(reversed(list50))


list52 = np.array(df17).ravel().tolist()
list52.sort(reverse = True)
list53 = sorted(list52)
list54 = list(reversed(list53))

#0.3 sec
list55 = np.array(df18).ravel().tolist()
list55.sort(reverse = True)
list56 = sorted(list55)
list57 = list(reversed(list56))


list58 = np.array(df19).ravel().tolist()
list58.sort(reverse = True)
list59 = sorted(list58)
list60 = list(reversed(list59))

#0.2 sec
list61 = np.array(df20).ravel().tolist()
list61.sort(reverse = True)
list62 = sorted(list61)
list63 = list(reversed(list62))


list64 = np.array(df21).ravel().tolist()
list64.sort(reverse = True)
list65 = sorted(list64)
list66 = list(reversed(list65))

#0.1 sec
list67 = np.array(df22).ravel().tolist()
list67.sort(reverse = True)
list68 = sorted(list67)
list69 = list(reversed(list68))


list70 = np.array(df23).ravel().tolist()
list70.sort(reverse = True)
list71 = sorted(list70)
list72 = list(reversed(list71))

#50 ms
list73 = np.array(df24).ravel().tolist()
list73.sort(reverse = True)
list74 = sorted(list73)
list75 = list(reversed(list74))


list76 = np.array(df25).ravel().tolist()
list76.sort(reverse = True)
list77 = sorted(list76)
list78 = list(reversed(list77))

#40 ms
list79 = np.array(df26).ravel().tolist()
list79.sort(reverse = True)
list80 = sorted(list79)
list81 = list(reversed(list80))


list82 = np.array(df27).ravel().tolist()
list82.sort(reverse = True)
list83 = sorted(list82)
list84 = list(reversed(list83))


list85 = np.array(df28).ravel().tolist()
list85.sort(reverse = True)
list86 = sorted(list85)
list87 = list(reversed(list86))


list88 = np.array(df29).ravel().tolist()
list88.sort(reverse = True)
list89 = sorted(list88)
list90 = list(reversed(list89))


list91 = np.array(df30).ravel().tolist()
list91.sort(reverse = True)
list92 = sorted(list91)
list93 = list(reversed(list92))


list94 = np.array(df31).ravel().tolist()
list94.sort(reverse = True)
list95 = sorted(list94)
list96 = list(reversed(list95))


list97 = np.array(df32).ravel().tolist()
list97.sort(reverse = True)
list98 = sorted(list97)
list99 = list(reversed(list98))


list100 = np.array(df33).ravel().tolist()
list100.sort(reverse = True)
list101 = sorted(list100)
list102 = list(reversed(list101))

five_sec_b_mean = np.mean(list3[:9])
five_sec_d_mean = np.mean(list4)
five_sec_dif = five_sec_b_mean - five_sec_d_mean

two_sec_b_mean = np.mean(list9[:9])
two_sec_d_mean = np.mean(list10)
two_sec_dif = two_sec_b_mean - two_sec_d_mean

one_sec_b_mean = np.mean(list15[:9])
one_sec_d_mean = np.mean(list16)
one_sec_dif = one_sec_b_mean - one_sec_d_mean

ninehundred_ms_b_mean = np.mean(list21[:9])
ninehundred_ms_d_mean = np.mean(list22)
ninehundred_ms_dif = ninehundred_ms_b_mean - ninehundred_ms_d_mean

eighthundred_ms_b_mean = np.mean(list27[:9])
eighthundred_ms_d_mean = np.mean(list28)
eighthundred_ms_dif = eighthundred_ms_b_mean - eighthundred_ms_d_mean

sevenhundred_ms_b_mean = np.mean(list33[:9])
sevenhundred_ms_d_mean = np.mean(list34)
sevenhundred_ms_dif = sevenhundred_ms_b_mean - sevenhundred_ms_d_mean

sixhundred_ms_b_mean = np.mean(list39[:9])
sixhundred_ms_d_mean = np.mean(list40)
sixhundred_ms_dif = sixhundred_ms_b_mean - sixhundred_ms_d_mean

fivehundred_ms_b_mean = np.mean(list45[:9])
fivehundred_ms_d_mean = np.mean(list46)
fivehundred_ms_dif = fivehundred_ms_b_mean - fivehundred_ms_d_mean

fourhundred_ms_b_mean = np.mean(list51[:9])
fourhundred_ms_d_mean = np.mean(list52)
fourhundred_ms_dif = fourhundred_ms_b_mean - fourhundred_ms_d_mean

threehundred_ms_b_mean = np.mean(list57[:9])
threehundred_ms_d_mean = np.mean(list58)
threehundred_ms_dif = threehundred_ms_b_mean - threehundred_ms_d_mean

twohundred_ms_b_mean = np.mean(list63[:9])
twohundred_ms_d_mean = np.mean(list64)
twohundred_ms_dif = twohundred_ms_b_mean - twohundred_ms_d_mean

onehundred_ms_b_mean = np.mean(list69[:9])
onehundred_ms_d_mean = np.mean(list70)
onehundred_ms_dif = onehundred_ms_b_mean - onehundred_ms_d_mean

fifty_ms_b_mean = np.mean(list75[:9])
fifty_ms_d_mean = np.mean(list76)
fifty_ms_dif = fifty_ms_b_mean - fifty_ms_d_mean

fourty_ms_b_mean = np.mean(list81[:9])
fourty_ms_d_mean = np.mean(list82)
fourty_ms_dif = fourty_ms_b_mean - fourty_ms_d_mean

mean = [five_sec_dif, two_sec_dif, one_sec_dif, ninehundred_ms_dif, eighthundred_ms_dif, sevenhundred_ms_dif,
        sixhundred_ms_dif,fivehundred_ms_dif, fourhundred_ms_dif, threehundred_ms_dif, twohundred_ms_dif,
        onehundred_ms_dif, fifty_ms_dif, fourty_ms_dif]

t = [5,2,1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.05,0.04]
'''
plt.figure('Difference between mean bright ion and dark ion reading vs Exposure time')
plt.title('Difference between mean bright ion and dark ion reading vs Exposure time', fontsize=16)
plt.plot(t,mean,'.')
plt.ylabel('Count reading')
plt.xlabel('Exposure time/s')



r = []
c = []
a = list3[:194]

    
for i in a:
    for row in range(df.shape[0]): 
        for col in range(df.shape[1]):
            
            if df.iat[row,col] == i:
                print(row, col)
                r.append(row)
                c.append(col)
#data = c, r
fig = plt.figure('Brightest pixels for 16x16 image at 5 s Exposure')
ax = fig.add_subplot(111)
ax.plot(c,r, '.')
ax.set_xlim((0,16))
ax.set_ylim((0,16))
ax.set_aspect('equal')
#fig.show()
#print(data)



r1 = []
c1 = []
a1 = list9[:152]

    
for j in a1:
    for row in range(df2.shape[0]): 
        for col in range(df2.shape[1]):
            
            if df2.iat[row,col] == j:
                print(row, col)
                r1.append(row)
                c1.append(col)

#data1 = c1, r1
fig1 = plt.figure('Brightest pixels for 16x16 image at 2 s Exposure')
ax1 = fig1.add_subplot(111)
ax1.plot(c1,r1, '.')
ax1.set_xlim((0,16))
ax1.set_ylim((0,16))
ax1.set_aspect('equal')
#fig1.show()
#print(data)
'''  

r2 = []
c2 = []
a2 = list75[:19]

    
for j in a2:
    for row in range(df24.shape[0]): 
        for col in range(df24.shape[1]):
            
            if df24.iat[row,col] == j:
                print(row, col)
                r2.append(row)
                c2.append(col)

#data1 = c1, r1
fig2 = plt.figure('Brightest pixels for 12x12 image at 40 ms Exposure at 1800 gain')
ax2 = fig2.add_subplot(111)
ax2.plot(c2,r2, '.')
ax2.set_xlim((0,12))
ax2.set_ylim((0,12))
ax2.set_aspect('equal')


                    


'''
plt.figure('Histogram for 5 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 5 s Exposure for 16x16 section', fontsize=16)
plt.hist(list3, bins = 200)#[:194]
plt.hist(list6, bins = 200)

plt.figure('Histogram for 2 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 2 s Exposure for 16x16 section', fontsize=16)
plt.hist(list9[:152], bins = 200)
plt.hist(list12, bins = 200)

plt.figure('Histogram for 1 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 1 s Exposure for 16x16 section', fontsize=16)
plt.hist(list15[:137], bins = 200)
plt.hist(list18, bins = 200)

plt.figure('Histogram for 0.9 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.9 s Exposure for 16x16 section', fontsize=16)
plt.hist(list21[:111], bins = 200)
plt.hist(list24, bins = 200)

plt.figure('Histogram for 0.8 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.8 s Exposure for 16x16 section', fontsize=16)
plt.hist(list27[:122], bins = 200)
plt.hist(list30, bins = 200)

plt.figure('Histogram for 0.7 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.7 s Exposure for 16x16 section', fontsize=16)
plt.hist(list33[:118], bins = 200)
plt.hist(list36, bins = 200)

plt.figure('Histogram for 0.6 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.6 s Exposure for 16x16 section', fontsize=16)
plt.hist(list39[:118], bins = 200)
plt.hist(list42, bins = 200)

plt.figure('Histogram for 0.5 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.5 s Exposure for 16x16 section', fontsize=16)
plt.hist(list45[:133], bins = 200)
plt.hist(list48, bins = 200)

plt.figure('Histogram for 0.4 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.4 s Exposure for 16x16 section', fontsize=16)
plt.hist(list51[:108], bins = 200)
plt.hist(list54, bins = 200)

plt.figure('Histogram for 0.3 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.3 s Exposure for 16x16 section', fontsize=16)
plt.hist(list57[:103], bins = 200)
plt.hist(list60, bins = 200)

plt.figure('Histogram for 0.2 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.2 s Exposure for 16x16 section', fontsize=16)
plt.hist(list63[:57], bins = 200)
plt.hist(list66[:100], bins = 200)

plt.figure('Histogram for 0.1 s Exposure for 16x16 section')
plt.title('Bright and Dark Histogram overlap: 0.1 s Exposure for 16x16 section', fontsize=16)
plt.hist(list69[:45], bins = 200)
plt.hist(list72[:100], bins = 200)

plt.figure('Histogram for 50 ms Exposure for 12x12 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 50 ms Exposure for 12x12 section at 1800 gain', fontsize=16)
plt.hist(list75[:19], bins = 150)#
plt.hist(list78, bins = 150)

plt.figure('Histogram for 40 ms Exposure for 12x12 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 40 ms Exposure for 12x12 section at 1800 gain', fontsize=16)
plt.hist(list81[:10], bins = 150)
plt.hist(list84, bins = 150)

plt.figure('Histogram for 30 ms Exposure for 12x12 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 30 ms Exposure for 12x12 section at 1800 gain', fontsize=16)
plt.hist(list87, bins = 150)
plt.hist(list90, bins = 150)

plt.figure('Histogram for 20 ms Exposure for 12x12 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 20 ms Exposure for 12x12 section at 1800 gain', fontsize=16)
plt.hist(list93, bins = 150)
plt.hist(list96, bins = 150)

plt.figure('Histogram for 10 ms Exposure for 12x12 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 10 ms Exposure for 12x12 section at 1800 gain', fontsize=16)
plt.hist(list99, bins = 150)
plt.hist(list102, bins = 150)


t = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0, 2.0, 5.0]
n = [45,57,103,108,133,118,118,122,111,137,152,194]

plt.figure('no. of pixels vs Exposure time for 16x16 section')
plt.title('no. of pixels in ROI vs Exposure time for 16x16 section', fontsize=16)
plt.ylabel('no. of pixels in ROI')
plt.xlabel('Exposure time/s')
plt.plot(t,n, '.')
'''
plt.show()