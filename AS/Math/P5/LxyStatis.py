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
    
