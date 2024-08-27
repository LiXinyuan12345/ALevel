from LxyStatis import *


print("Input statistical data:")
data = list(map(int, input().split()))

#print("Data:", data)
print("------------------------------")
print("Mean  : ", CalcMean(data))
mode,frequncy =  CalcMode(data)
print("Mode  :  {}({})".format(mode,frequncy))
print("Median: ", CalcMedian(data))

