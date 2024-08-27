from LxyStatis import *


print("Input statistical data:")
data = list(map(int, input().split()))

print("------------------------------")
lower_quatile,upper_quatile,interquartile_range = CalcQuartilesAndRange(data)
print("Lower Quatile  : ", lower_quatile, " Upper Quatile  : ",upper_quatile,"  Interquartile Range  :", interquartile_range)


