from LxyStatis import *


'''
data:  37 37.5 38 38.5 39 39.5 40 40.5 41
'''
print("Input data:")
data = list(map(float, input().split()))

print("------------------------------")
mean, variance,standard_deviation = CalcVarianceAndSD(data)
print("Mean = x̄ = ", mean )
print("Variance = Σx²/n - x̄² = ", variance)
print("Standard Deviation = √Variance =  ", standard_deviation)

