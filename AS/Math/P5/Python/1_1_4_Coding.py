from LxyStatis import *


print("Input data:")
data = list(map(float, input().split()))

print("------------------------------")
mean, variance,standard_deviation = CalcVarianceAndSD(data)
print("Mean = x̄ = ", mean , " Standard Deviation = ", standard_deviation)

print("\n------------After data + 3 ------------------")
data_add_3 = []
for v in data:
    data_add_3.append(v+3)
print(data_add_3)
mean, var1iance,standard_deviation = CalcVarianceAndSD(data_add_3)
print("Mean = x̄ = ", mean , " Standard Deviation = ", standard_deviation)

print("\n------------After data * 3 ------------------")
data_mul_3 = []
for v in data:
    data_mul_3.append(v*3)
print(data_mul_3)
mean, variance,standard_deviation = CalcVarianceAndSD(data_mul_3)
print("Mean = x̄ = ", mean , " Standard Deviation = ", standard_deviation)

print("\n------------After data * 10 +1 ------------------")
data_mul_10_add_1 = []
for v in data:
    data_mul_10_add_1.append(v*10+1)
print(data_mul_10_add_1)
mean, variance,standard_deviation = CalcVarianceAndSD(data_mul_10_add_1)
print("Mean = x̄ = ", mean , " Standard Deviation = ", standard_deviation)


str = input()
print(str)

str = input.nextLine() 
System.out.println(str)
