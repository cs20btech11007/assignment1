# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X7unxib3Cdji9SNljD6eqe7D2DD90eP_
"""

from scipy.stats import binom 
import matplotlib.pyplot as plt 
# setting the values 
# of n and p 
n = 2
p = 0.25
# defining list of r values 
i_values = list(range(n + 1)) 
# list of pmf values 
dist = [binom.pmf(i, n, p) for i in i_values ] 
# plotting the graph  
plt.bar(i_values, dist) 
plt.show()