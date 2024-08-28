from LxyStatis import *

#------------------------------------------------------
#  Groupd Data FreqTable
#
#       data                freq
#  150 <= x < 155            3
#  155 <= x < 160            5
#  160 <= x < 165            9
#  165 <= x < 170            7
#  170 <= x < 175            1 
#
#------------------------------------------------------

'''
data:  150 155 160 165 170 175 
freq:       3   5   9   7   1
'''

print("Input frequency table data:")
data = list(map(float, input().split()))
print("Input frequency:")
freq = list(map(float, input().split()))

print("------------------------------")
grouped_data=[]
for i in range(1,len(data)):
    grouped_data.append( (data[i-1], data[i]) )
    
mode,mean,median = CalcgroupedFreqTable(grouped_data,freq)
print("Mean  : ", mean)
print("Mode  : ", mode)
print("Median: ", median)

