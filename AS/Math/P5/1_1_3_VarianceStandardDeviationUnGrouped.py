from LxyStatis import *


'''
data:  3 5 7 9 11 16
freq:  1 4 7 5 2  2
'''
print("Input frequency table data:")
data = list(map(float, input().split()))
print("Input frequency:")
freq = list(map(float, input().split()))

print("------------------------------")
mean, variance,standard_deviation = CalcUngroupedVarianceAndSD(data,freq)
print("Mean = x̄ = ", mean )
print("Variance =  Σx²f/Σf - x̄² = ", variance)
print("Standard Deviation = √Variance =  ", standard_deviation)

