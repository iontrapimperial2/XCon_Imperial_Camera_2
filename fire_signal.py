# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:44:12 2019

@author: iontrap
"""
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,7.2, 0.2)
V = [0, 0.001, 0, 0, 0,
     0, 0.316, 0.348, 0.358, 0.354,
     0.357, 0.355, 0.356, 0.358, 0.357,
     0.354, 0.357, 0.359, 0.355, 0.355,
     0.356, 0.356, 0.355, 0.351, 0.350,
     0.358, 0.351, 0.351, 0.351, 0.352,
     0.358, 0.356, 0.002, 0, 0,  0]

plt.plot(t,V,)
plt.xlabel('Time')
plt.ylabel('Fire Signal Voltage')
plt.show()