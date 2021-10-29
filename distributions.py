# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
#import random
##################################################
numIter = 10
results = list(range(numIter))
for i in results: #range(10) :
    results[i] = np.random.randint(10)



numBins = round((len(results))**(1/2))
bins = np.linspace(round(min(results)), round(max(results)), numBins)
digitized = (np.digitize(results, bins))-1
countsPerBin = np.zeros(len(bins))
print(range(len(digitized)))
for j in range(len(digitized)):
    countsPerBin[digitized[j]] += 1#countsPerBin[digitized[j]] + 1
    #print(j)
   # print(digitized[j])
  #  print(countsPerBin[digitized[j]])
#fig2 = plt.figure()
#ax2 = plt.axes()    
#ax2.plot(bins, countsPerBin);

plt.ylabel('Probability')
plt.xlabel('Data');
plt.hist(results, density=True, bins=10)