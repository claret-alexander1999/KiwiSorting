from enum import auto
from operator import itemgetter

from numpy import sort

import matplotlib.pyplot as plt


kiwisorting=[]

with open ("kiwidata.txt") as textFile:
    for line in textFile:
        kiwisortingArray=[item.strip() for item in line.split(',')]
        kiwisorting.append(kiwisortingArray)

def bubblesort(kiwisortingArray):
    for i in range(len(kiwisortingArray)-1,0,-1):
        for j in range(i):
            if kiwisortingArray[j]>kiwisortingArray[j+1]:
                temp=kiwisortingArray[j]
                kiwisortingArray[j]=kiwisortingArray[j+1]
                kiwisortingArray[j+1]=temp



def selectionsort(kiwisortingArray):
    for i in range(0,len(kiwisortingArray)-1):
        minimumposition=i
        for j in range(i,len(kiwisortingArray)):
            if kiwisortingArray[j]<kiwisortingArray[minimumposition]:
                minimumposition=j

        temp=kiwisortingArray[i]
        kiwisortingArray[i]=kiwisortingArray[minimumposition]
        kiwisortingArray[minimumposition]=temp


selectionsort(kiwisortingArray)
#bubblesort(kiwisortingArray)
print(kiwisortingArray)
#plt.plot(kiwisortingArray)
#plt.ylabel('Kiwi Weight')
#plt.xlabel('Number of Kiwis')
#plt.show()
