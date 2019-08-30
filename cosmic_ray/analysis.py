# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:18:50 2019

@author: iontrap
"""

import pandas as pd
import numpy as np

cos = []

df = pd.read_csv(r'C:\Users\iontrap\Documents\iontrap\code\python\XCon_Imperial_Camera_2\cosmic_ray\pic5.txt', header = None)
df.drop(df.columns[-1], axis=1, inplace=True)  #delete last column
df.drop(df.columns[0], axis=1, inplace=True)           #delete first column
a = np.array(df).ravel().tolist()
for i in a:
    if i>5000:
        cos.append(i)