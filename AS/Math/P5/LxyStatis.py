import copy

#------------------------------
# 计算平均数
#------------------------------
def CalcMean(data):
    if len(data) == 0:
        return 0
    
    total = 0
    for v in data:
        total += v
    return total/len(data)

#------------------------------
#计算众数
#------------------------------
def CalcMode(data):
    frequencies = {}
    for v in data:
        cnt = frequencies.get(v,0)
        frequencies[v]= cnt+1

    v   = 0
    cnt = 0
    for k in frequencies.keys():
        if frequencies[k] > cnt:
            v = k
            cnt = frequencies[k]
    return v,cnt

        
#------------------------------
# 计算中位数
#------------------------------
def CalcMedian(data):

    data = copy.deepcopy(data)
    data.sort()
    n    = len(data)

    # odd
    if n % 2 == 1:
        return data[(n+1)//2-1]

    # even
    second =(n+1)//2
    first  =second-1
    return ( data[second] + data[first])/2


#------------------------------
# 计算上下四分距和范围
#------------------------------
def  CalcQuartilesAndRange(data):

    data = copy.deepcopy(data)
    data.sort()
    n    = len(data)    

    lower_quatile_pos = (n+1)//4
    upper_quatile_pos = (n+1)*3//4

    lower_quatile = upper_quatile = 0
    if  (n+1)/4 == lower_quatile_pos:
        lower_quatile = data[lower_quatile_pos-1]
    else:
        lower_quatile = (data[lower_quatile_pos-1] + data[lower_quatile_pos])/2

    if  (n+1)*3/4 == upper_quatile_pos:
        upper_quatile = data[upper_quatile_pos-1]
    else:
        upper_quatile = (data[upper_quatile_pos-1] + data[upper_quatile_pos])/2

    interquartile_range = upper_quatile - lower_quatile
    return lower_quatile,upper_quatile,interquartile_range
    
#------------------------------------------------------
#  Ungroupd Data FreqTable
#
#   data:  37 37.5 38 38.5 39 39.5 40 40.5 41
#   freq:  3   3   12  5   16  9    7  4    1  
#
#------------------------------------------------------
def CalcUngroupedFreqTable(data,frequncy):
    
    # find mode
    max_freq = frequncy[0]
    mode     = data[0]
    for i in range(1,len(data)):
        if max_freq < frequncy[i]:
            max_freq = frequncy[i]
            mode     = data[i]

    # find mean
    sum = 0
    cnt = 0 
    for i in range(len(data)):
        sum += data[i] * frequncy[i]
        cnt += frequncy[i]
    mean = sum/cnt

    # find median
    median = 0
    median_pos = (cnt+1)/2
    freq_sum   = 0
    for i in range(len(frequncy)):  
        freq_sum += frequncy[i]  
        if median_pos <= freq_sum:
            median = data[i] 
            break

    return mode,mean,median


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
def CalcgroupedFreqTable(data,frequncy):

    # find mode
    max_freq = frequncy[0]
    mode     = data[0]
    for i in range(1,len(data)):
        if max_freq < frequncy[i]:
            max_freq = frequncy[i]
            mode     = data[i]

    # find mean
    sum = 0
    cnt = 0 
    for i in range(len(data)):
        mean_v_i = (data[i][0] + data[i][1])/2
        sum += mean_v_i * frequncy[i]
        cnt += frequncy[i]
    mean = sum/cnt

    # find median
    median = 0
    median_pos = (cnt+1)/2
    freq_sum   = 0
    for i in range(len(frequncy)):  
        freq_sum += frequncy[i]  
        if median_pos <= freq_sum:
            median = data[i] 
            break

    return mode,mean,median