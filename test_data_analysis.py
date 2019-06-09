# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:45:08 2019

@author: IonTrap/JMHeinrich
"""
   
import pandas as pd
import numpy as np

results2 = pd.read_csv('test3.txt', header = None, usecols = np.arange(1,513))

import matplotlib.pyplot as plt

plt.imshow(results2)
plt.show()