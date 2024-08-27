from LxyStatis import *


'''
data:  37 37.5 38 38.5 39 39.5 40 40.5 41
freq:  3   3   12  5   16  9    7  4    1  
'''
print("Input frequency table data:")
data = list(map(float, input().split()))
print("Input frequency:")
freq = list(map(float, input().split()))

print("------------------------------")
mode,mean,median = CalcUngroupedFreqTable(data,freq)
print("Mean  : ", mean)
print("Mode  : ", mode)
print("Median: ", median)

