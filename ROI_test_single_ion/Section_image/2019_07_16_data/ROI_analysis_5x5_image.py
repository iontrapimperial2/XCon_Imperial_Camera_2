# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1 sec
df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\1s9.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column

df1 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\1t4.txt', header = None)
df1.drop(df1.columns[-1], axis=1, inplace=True)  #delete last column
df1.drop(df1.columns[0], axis=1, inplace=True)           #delete first column

#0.5 sec
df2 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\05s.txt', header = None)
df2.drop(df2.columns[-1], axis=1, inplace=True)  #delete last column
df2.drop(df2.columns[0], axis=1, inplace=True)           #delete first column

df3 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\05t.txt', header = None)
df3.drop(df3.columns[-1], axis=1, inplace=True)  #delete last column
df3.drop(df3.columns[0], axis=1, inplace=True)           #delete first column

#0.1 sec
df4 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\01s.txt', header = None)
df4.drop(df4.columns[-1], axis=1, inplace=True)  #delete last column
df4.drop(df4.columns[0], axis=1, inplace=True)           #delete first column

df5 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\01t.txt', header = None)
df5.drop(df5.columns[-1], axis=1, inplace=True)  #delete last column
df5.drop(df5.columns[0], axis=1, inplace=True)           #delete first column

#50 ms
df6 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\005s8.txt', header = None)
df6.drop(df6.columns[-1], axis=1, inplace=True)  #delete last column
df6.drop(df6.columns[0], axis=1, inplace=True)           #delete first column

df7 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\005t.txt', header = None)
df7.drop(df7.columns[-1], axis=1, inplace=True)  #delete last column
df7.drop(df7.columns[0], axis=1, inplace=True)           #delete first column

#40 ms
df8 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\004s6.txt', header = None)
df8.drop(df8.columns[-1], axis=1, inplace=True)  #delete last column
df8.drop(df8.columns[0], axis=1, inplace=True)           #delete first column

df9 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\004t.txt', header = None)
df9.drop(df9.columns[-1], axis=1, inplace=True)  #delete last column
df9.drop(df9.columns[0], axis=1, inplace=True)           #delete first column

#30 ms
df10 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\003s.txt', header = None)
df10.drop(df10.columns[-1], axis=1, inplace=True)  #delete last column
df10.drop(df10.columns[0], axis=1, inplace=True)           #delete first column

df11 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\002t.txt', header = None)
df11.drop(df11.columns[-1], axis=1, inplace=True)  #delete last column
df11.drop(df11.columns[0], axis=1, inplace=True)           #delete first column

#20 ms
df12 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\002s.txt', header = None)
df12.drop(df12.columns[-1], axis=1, inplace=True)  #delete last column
df12.drop(df12.columns[0], axis=1, inplace=True)           #delete first column

df13 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\002t.txt', header = None)
df13.drop(df13.columns[-1], axis=1, inplace=True)  #delete last column
df13.drop(df13.columns[0], axis=1, inplace=True)           #delete first column

#10 ms
df14 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\bright\001s5.txt', header = None)
df14.drop(df14.columns[-1], axis=1, inplace=True)  #delete last column
df14.drop(df14.columns[0], axis=1, inplace=True)           #delete first column

df15 = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\ROI_test_single_ion\Section_image\2019_07_16_data\dark\001t7.txt', header = None)
df15.drop(df15.columns[-1], axis=1, inplace=True)  #delete last column
df15.drop(df15.columns[0], axis=1, inplace=True)           #delete first column






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
#1 sec
list1 = np.array(df).ravel().tolist()
list1.sort(reverse = True)
list2 = sorted(list1)
list3 = list(reversed(list2))


list4 = np.array(df1).ravel().tolist()
list4.sort(reverse = True)
list5 = sorted(list4)
list6 = list(reversed(list5))

#0.5 sec
list7 = np.array(df2).ravel().tolist()
list7.sort(reverse = True)
list8 = sorted(list7)
list9 = list(reversed(list8))


list10 = np.array(df3).ravel().tolist()
list10.sort(reverse = True)
list11 = sorted(list10)
list12 = list(reversed(list11))

#0.1 sec
list13 = np.array(df4).ravel().tolist()
list13.sort(reverse = True)
list14 = sorted(list13)
list15 = list(reversed(list14))


list16 = np.array(df5).ravel().tolist()
list16.sort(reverse = True)
list17 = sorted(list16)
list18 = list(reversed(list17))

#50 ms
list19 = np.array(df6).ravel().tolist()
list19.sort(reverse = True)
list20 = sorted(list19)
list21 = list(reversed(list20))


list22 = np.array(df7).ravel().tolist()
list22.sort(reverse = True)
list23 = sorted(list22)
list24 = list(reversed(list23))

#40 ms
list25 = np.array(df8).ravel().tolist()
list25.sort(reverse = True)
list26 = sorted(list25)
list27 = list(reversed(list26))


list28 = np.array(df9).ravel().tolist()
list28.sort(reverse = True)
list29 = sorted(list28)
list30 = list(reversed(list29))

#30 ms
list31 = np.array(df10).ravel().tolist()
list31.sort(reverse = True)
list32 = sorted(list31)
list33 = list(reversed(list32))


list34 = np.array(df11).ravel().tolist()
list34.sort(reverse = True)
list35 = sorted(list34)
list36 = list(reversed(list35))

#20 ms
list37 = np.array(df12).ravel().tolist()
list37.sort(reverse = True)
list38 = sorted(list37)
list39 = list(reversed(list38))


list40 = np.array(df13).ravel().tolist()
list40.sort(reverse = True)
list41 = sorted(list40)
list42 = list(reversed(list41))

#10 ms
list43 = np.array(df14).ravel().tolist()
list43.sort(reverse = True)
list44 = sorted(list43)
list45 = list(reversed(list44))


list46 = np.array(df15).ravel().tolist()
list46.sort(reverse = True)
list47 = sorted(list46)
list48 = list(reversed(list47))



l1 = [0,1,2,3]
l2 = [1,2,3,4]
''''''
#bright
a = np.mean([df.iat[i,j] for i in l1 for j in l2])     #1 sec
b = np.mean([df2.iat[i,j] for i in l1 for j in l2])    #0.5 sec
c = np.mean([df4.iat[i,j] for i in l1 for j in l2])    #0.1 sec
d = np.mean([df6.iat[i,j] for i in l1 for j in l2])    #50 ms
e = np.mean([df8.iat[i,j] for i in l1 for j in l2])    #40 ms
f = np.mean([df10.iat[i,j] for i in l1 for j in l2])   #30 ms
g = np.mean([df12.iat[i,j] for i in l1 for j in l2])   #20 ms
h = np.mean([df14.iat[i,j] for i in l1 for j in l2])   #10 ms


#dark
a1 = np.mean([df1.iat[i,j] for i in l1 for j in l2])   #1 sec
b1 = np.mean([df3.iat[i,j] for i in l1 for j in l2])   #0.5 sec
c1 = np.mean([df5.iat[i,j] for i in l1 for j in l2])   #0.1 sec
d1 = np.mean([df7.iat[i,j] for i in l1 for j in l2])   #50 ms
e1 = np.mean([df9.iat[i,j] for i in l1 for j in l2])   #40 ms
f1 = np.mean([df11.iat[i,j] for i in l1 for j in l2])  #30 ms
g1 = np.mean([df13.iat[i,j] for i in l1 for j in l2])  #20 ms
h1 = np.mean([df15.iat[i,j] for i in l1 for j in l2])  #10 ms

diff = [a-a1,b-b1,c-c1,d-d1,e-e1,f-f1,g-g1,h-h1]
t = [1,0.5,0.1,0.05,0.04,0.03,0.02,0.01]


plt.figure('Difference between mean bright ion and dark ion reading vs Exposure time with 4x4 ROI')
plt.title('Difference between mean bright ion and dark ion reading vs Exposure time with 4x4 ROI', fontsize=20)
plt.plot(t,diff,'.')
plt.ylabel('Count reading')
plt.xlabel('Exposure time/s')

'''
#1 sec
r = []
c = []
a = list3[:9]

    
for i in a:
    for row in range(df.shape[0]): 
        for col in range(df.shape[1]):
            
            if df.iat[row,col] == i:
                print(row, col)
                r.append(row)
                c.append(col)
#data = c, r
fig = plt.figure('Brightest pixels for 5x5 image at 1 s Exposure at 1800 gain')
fig.suptitle('Brightest pixels for 5x5 image at 1 s Exposure', fontsize=20)
ax = fig.add_subplot(111)
ax.plot(c,r, '.')
ax.set_xlim((0,5))
ax.set_ylim((0,5))
ax.set_aspect('equal')


#0.5 sec
r1 = []
c1 = []
a1 = list9[:9]

    
for j in a1:
    for row in range(df2.shape[0]): 
        for col in range(df2.shape[1]):
            
            if df2.iat[row,col] == j:
                print(row, col)
                r1.append(row)
                c1.append(col)

#data1 = c1, r1
fig1 = plt.figure('Brightest pixels for 5x5 image at 0.5 s Exposure at 1800 gain')
fig1.suptitle('Brightest pixels for 5x5 image at 0.5 s Exposure', fontsize=20)
ax1 = fig1.add_subplot(111)
ax1.plot(c1,r1, '.')
ax1.set_xlim((0,5))
ax1.set_ylim((0,5))
ax1.set_aspect('equal')

  
#0.1 sec
r2 = []
c2 = []
a2 = list15[:9]

    
for j in a2:
    for row in range(df4.shape[0]): 
        for col in range(df4.shape[1]):
            
            if df4.iat[row,col] == j:
                print(row, col)
                r2.append(row)
                c2.append(col)

#data1 = c1, r1
fig2 = plt.figure('Brightest pixels for 5x5 image at 0.1 s Exposure at 1800 gain')
fig2.suptitle('Brightest pixels for 5x5 image at 0.1 s Exposure', fontsize=20)
ax2 = fig2.add_subplot(111)
ax2.plot(c2,r2, '.')
ax2.set_xlim((0,5))
ax2.set_ylim((0,5))
ax2.set_aspect('equal')


#50 ms
r3 = []
c3 = []
a3 = list21[:9]

    
for j in a3:
    for row in range(df6.shape[0]): 
        for col in range(df6.shape[1]):
            
            if df6.iat[row,col] == j:
                print(row, col)
                r3.append(row)
                c3.append(col)

#data1 = c1, r1
fig3 = plt.figure('Brightest pixels for 5x5 image at 50 ms Exposure at 1800 gain')
fig3.suptitle('Brightest pixels for 5x5 image at 50 ms Exposure', fontsize=20)
ax3 = fig3.add_subplot(111)
ax3.plot(c3,r3, '.')
ax3.set_xlim((0,5))
ax3.set_ylim((0,5))
ax3.set_aspect('equal')   


#40 ms
r4 = []
c4 = []
a4 = list27[:9]

    
for j in a4:
    for row in range(df8.shape[0]): 
        for col in range(df8.shape[1]):
            
            if df8.iat[row,col] == j:
                print(row, col)
                r4.append(row)
                c4.append(col)

#data1 = c1, r1
fig4 = plt.figure('Brightest pixels for 5x5 image at 40 ms Exposure at 1800 gain')
fig4.suptitle('Brightest pixels for 5x5 image at 40 ms Exposure', fontsize=20)
ax4 = fig4.add_subplot(111)
ax4.plot(c4,r4, '.')
ax4.set_xlim((0,5))
ax4.set_ylim((0,5))
ax4.set_aspect('equal')          


#30 ms
r5 = []
c5 = []
a5 = list33[:9]

    
for j in a5:
    for row in range(df10.shape[0]): 
        for col in range(df10.shape[1]):
            
            if df10.iat[row,col] == j:
                print(row, col)
                r5.append(row)
                c5.append(col)

#data1 = c1, r1
fig5 = plt.figure('Brightest pixels for 5x5 image at 30 ms Exposure at 1800 gain')
fig5.suptitle('Brightest pixels for 5x5 image at 30 ms Exposure', fontsize=20)
ax5 = fig5.add_subplot(111)
ax5.plot(c5,r5, '.')
ax5.set_xlim((0,5))
ax5.set_ylim((0,5))
ax5.set_aspect('equal')      


#20 ms
r6 = []
c6 = []
a6 = list39[:9]

    
for j in a6:
    for row in range(df12.shape[0]): 
        for col in range(df12.shape[1]):
            
            if df12.iat[row,col] == j:
                print(row, col)
                r6.append(row)
                c6.append(col)

#data1 = c1, r1
fig6 = plt.figure('Brightest pixels for 5x5 image at 20 ms Exposure at 1800 gain')
fig6.suptitle('Brightest pixels for 5x5 image at 20 ms Exposure', fontsize=20)
ax6 = fig6.add_subplot(111)
ax6.plot(c6,r6, '.')
ax6.set_xlim((0,5))
ax6.set_ylim((0,5))
ax6.set_aspect('equal') 


#10 ms
r7 = []
c7 = []
a7 = list45[:9]

    
for j in a7:
    for row in range(df14.shape[0]): 
        for col in range(df14.shape[1]):
            
            if df14.iat[row,col] == j:
                print(row, col)
                r7.append(row)
                c7.append(col)

#data1 = c1, r1
fig7 = plt.figure('Brightest pixels for 5x5 image at 10 ms Exposure at 1800 gain')
fig7.suptitle('Brightest pixels for 5x5 image at 10 ms Exposure', fontsize=20)
ax7 = fig7.add_subplot(111)
ax7.plot(c7,r7, '.')
ax7.set_xlim((0,5))
ax7.set_ylim((0,5))
ax7.set_aspect('equal')       
'''


#bright
a2 = [df.iat[i,j] for i in l1 for j in l2]     #1 sec
b2 = [df2.iat[i,j] for i in l1 for j in l2]    #0.5 sec
c2 = [df4.iat[i,j] for i in l1 for j in l2]    #0.1 sec
d2 = [df6.iat[i,j] for i in l1 for j in l2]    #50 ms
e2 = [df8.iat[i,j] for i in l1 for j in l2]    #40 ms
f2 = [df10.iat[i,j] for i in l1 for j in l2]   #30 ms
g2 = [df12.iat[i,j] for i in l1 for j in l2]   #20 ms
h2 = [df14.iat[i,j] for i in l1 for j in l2]   #10 ms


#dark
a3 = [df1.iat[i,j] for i in l1 for j in l2]   #1 sec
b3 = [df3.iat[i,j] for i in l1 for j in l2]   #0.5 sec
c3 = [df5.iat[i,j] for i in l1 for j in l2]   #0.1 sec
d3 = [df7.iat[i,j] for i in l1 for j in l2]   #50 ms
e3 = [df9.iat[i,j] for i in l1 for j in l2]   #40 ms
f3 = [df11.iat[i,j] for i in l1 for j in l2]  #30 ms
g3 = [df13.iat[i,j] for i in l1 for j in l2]  #20 ms
h3 = [df15.iat[i,j] for i in l1 for j in l2]  #10 ms


plt.figure('Histogram for 1 s Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 1 s Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(a2, bins = 9)
plt.hist(a3, bins = 9)

plt.figure('Histogram for 0.5 s Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 0.5 s Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(b2, bins = 9)
plt.hist(b3, bins = 9)

plt.figure('Histogram for 0.1 s Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 0.1 s Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(c2, bins = 9)
plt.hist(c3, bins = 9)

plt.figure('Histogram for 50 ms Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 50 ms Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(d2, bins = 9)
plt.hist(d3, bins = 9)

plt.figure('Histogram for 40 ms Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 40 ms Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(e2, bins = 9)
plt.hist(e3, bins = 9)

plt.figure('Histogram for 30 ms Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 30 ms Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(f2, bins = 9)
plt.hist(f3, bins = 9)

plt.figure('Histogram for 20 ms Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 20 ms Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(g2, bins = 9)
plt.hist(g3, bins = 9)

plt.figure('Histogram for 10 ms Exposure for 4x4 ROI at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 10 ms Exposure for 4x4 ROI at 1800 gain', fontsize=16)
plt.hist(h2, bins = 9)
plt.hist(h3, bins = 9)



'''
plt.figure('Histogram for 1 s Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 1 s Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list3[:9], bins = 25)
plt.hist(list6, bins = 25)

plt.figure('Histogram for 0.5 s Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 0.5 s Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list9[:9], bins = 25)
plt.hist(list12, bins = 25)

plt.figure('Histogram for 0.1 s Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 0.1 s Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list15[:9], bins = 25)
plt.hist(list18, bins = 25)

plt.figure('Histogram for 50 ms Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 50 ms Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list21[:9], bins = 25)
plt.hist(list24, bins = 25)

plt.figure('Histogram for 40 ms Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 40 ms Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list27[:9], bins = 25)
plt.hist(list30, bins = 25)

plt.figure('Histogram for 30 ms Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 30 ms Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list33[:9], bins = 25)
plt.hist(list36, bins = 25)

plt.figure('Histogram for 20 ms Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 20 ms Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list39[:9], bins = 25)
plt.hist(list42, bins = 25)

plt.figure('Histogram for 10 ms Exposure for 5x5 section at 1800 gain')
plt.title('Bright and Dark Histogram overlap: 10 ms Exposure for 5x5 section at 1800 gain', fontsize=16)
plt.hist(list45[:9], bins = 25)
plt.hist(list48, bins = 25)

'''
plt.show()