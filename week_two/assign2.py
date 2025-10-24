# Task 1

# (X, Y)
# 悟空(0, 0)
# 丁滿(-1, 4)
# 特南克斯(1, -2)
# 弗利沙(4, -1)
# 辛巴(-3, 3)
# 貝吉塔(-4, -1)

import math

def func1 (name):
    all_members = {"悟空": [0, 0], "丁滿": [-1, 4], "特南克斯": [1, -2], "弗利沙": [4, -1], "辛巴": [-3, 3], "貝吉塔": [-4, -1]}
    target = {}
    result = {}
    left = {"悟空": [0, 0], "特南克斯": [1, -2], "辛巴": [-3, 3], "貝吉塔": [-4, -1]}
    right = {"丁滿": [-1, 4], "弗利沙": [4, -1]}
    
    if name in all_members:
        target [name] = all_members.pop(name)
        target_position = target [name] # 表示key對應的值=[1, -2]

        for other_name, other_position in all_members.items():
            dx = abs(other_position[0] - target_position[0])
            dy = abs(other_position[1] - target_position[1])
            distance = dx + dy
            result [other_name] = distance
        # print (result) # 跑出所有對象所對應的距離

        if name not in right:
            result["丁滿"] = result["丁滿"] + 2
            result["弗利沙"] = result["弗利沙"] + 2
        if name not in left:
            result["辛巴"] = result["辛巴"] + 2
            result["悟空"] = result["悟空"] + 2
            result["貝吉塔"] = result["貝吉塔"] + 2
            result["特南克斯"] = result["特南克斯"] + 2
        # print(result) # 把過斜線距離+2的條件加進去
        
        # 找出最大值
        def get_all_max_key ():
            # max_key_value = max(result, key=result.get)
            max_key_value = max(result.values())
            max_keys = []
            # print(max_key_value)
            for key_max, value_max in result.items():
                if value_max == max_key_value:
                    max_keys.append(key_max)
            return "、".join(max_keys)
        
        # 找出最小值
        def get_all_min_key ():
            min_key_value = min(result.values())
            # print(min_key_value)
            min_keys = []
            for key_min, value_min in result.items():
                if value_min == min_key_value:
                    min_keys.append(key_min)
            return "、".join(min_keys)
    print(f"最遠{get_all_max_key()};最近{get_all_min_key()}")

# 範例         
func1("辛巴")
print("----------")
func1("悟空")
print("----------")
func1("弗利沙")
print("----------")
func1("特南克斯")
print("==========")



# Task 2

# step1:先去判斷criteria的分類，分成'r'跟'c'和名字的，並列出符合這些條件的服務，另外儲存至candidates串列

# step2:計算差值，找出最近的'r'跟'c'，把這些數字儲存在依照差值排序的串列裡面，這個串列叫做sorted_candidates

# step3:接下來是檢查是否有衝突，如果有衝突，就選擇第二好的，這也是為什麼需要做排序

# step4:如果candidates串列只有一個元素，也就是說只有一個服務符合條件，如果此服務衝突，就會回傳Sorry，這是針對那些指名服務的預約

# step5:最後要做紀錄

# criteria:"Field=Value", "Field>=Value", and "Field<=Value"

# 這一題讓我有機會使用大量for迴圈搭配if判斷式的用法，也有機會使用到之前碰到的list comprehension，現在熟悉很多了。另外也讓我學到，不要堅持自已所建立的邏輯，我就是一直堅持自己原本的想法才卡住的，如果有需要，還是要打掉重想
# 流程想了好幾的版本，總是會漏掉一些重要的判斷。這一版是在之前的基礎上，再去做修改的

services = [{"name":"S1", "r":4.5, "c":1000}, {"name":"S2", "r":3, "c":1200}, {"name":"S3", "r":3.8, "c":800}] 

reservation_time = {} # 預約紀錄
reservation_time_id = 1

def criteria_string(string): # 展開criteria
    strl = list(string)
    del strl[0:3]
    string1 = ''.join(strl)
    return float(string1)

def time_func(time1, time2): # 展開時間區間
        time = []
        time.append(time1)
        for i in range(time2 - time1):
            time.append(time[i] + 1)
        return time

def check_time_conflict(time, name=None): # 時間區間檢查
    time_set = set(time)
    for i in reservation_time.values():
        if set(i['time']) & time_set:
            if name is None or i['name'] == name:
                return i['name']
    return None



def func2(ss, start, end, criteria):
    time_spread = time_func(start, end)
    global reservation_time_id
    candidates = []
    if 'r<=' in criteria:
        criteria_check = criteria_string(criteria)
        for s in ss:
            if s['r'] <= criteria_check:
                candidates.append(s)
        

    if 'r>=' in criteria:
        criteria_check = criteria_string(criteria)
        for s in ss:
            if s['r'] >= criteria_check:
                candidates.append(s)
        
    
    if 'c<=' in criteria:
        criteria_check = criteria_string(criteria)
        for s in ss:
            if s['c'] <= criteria_check:
                candidates.append(s)
        

    if 'c>=' in criteria:
        criteria_check = criteria_string(criteria)
        for s in ss:
            if s['c'] >= criteria_check:
                candidates.append(s)
        
        
    if 'name=' in criteria:
        ser_name = criteria.split('=')[1]
        for s in ss:
            if s['name'] == ser_name:
                candidates.append(s)

    # 計算差值，找到最接近的服務（r 或 c)
    flag = False
    for k in ['r<=','r>=','c<=','c>=']:
        if k in criteria:
            flag = True
            break
    
    if flag:
        if 'r' in criteria:
            key = 'r'
        else:
            key = 'c'
        
        criteria_check = criteria_string(criteria)

        diffs = []
        for s in candidates:
            diffs.append((abs(s[key] - criteria_check), s))
    
        diffs.sort(key=lambda x:x[0]) # 待釐清
        
        sorted_candidates = []
        for item in diffs:
            s = item[1]
            sorted_candidates.append(s)
    else:
        sorted_candidates = candidates
    
    # 找第一個沒衝突的
    for s in sorted_candidates:
        if not check_time_conflict(time_spread, s['name']):
            reservation_time[reservation_time_id] = {'name': s['name'], 'time': time_spread}
            reservation_time_id += 1
            return s['name']
        
    
    # 如果只有一個候選服務，且衝突 → sorry
    if len(sorted_candidates) == 1:
        return 'sorry'
    return 'sorry'

    


        

print(func2(services, 15, 17, "c>=800"))  # S3 
print(func2(services, 11, 13, "r<=4"))  # S3
print(func2(services, 10, 12, "name=S3"))  # Sorry
print(func2(services, 15, 18, "r>=4.5") ) # S1 
print(func2(services, 16, 18, "r>=4"))  # Sorry
print(func2(services, 13, 17, "name=S1"))  # Sorry
print(func2(services, 8, 9, "c<=1500"))# S2 
print(func2(services, 8, 9, "c<=1500")) # S1
print("==========")

# Task 3
# 25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17, …
# Find out the nth term in this sequence.


def function_a (data):
    list_a = []
    num = 25
    while num >= data:
        list_a.append(num)
        list_a_copy = list_a.copy()
        list_combined_a = list_a + list_a_copy
        num -= 2
    list_combined_a_v1 = sorted(list_combined_a) # 排序
    list_combined_a_v2 = list(reversed(list_combined_a_v1)) # 轉成降冪排列
    list_combined_a_v2.remove(list_combined_a_v2[0]) # 移除第一項
    list_combined_a_v2.append('_')
    list_combined_a_v3 = [list_combined_a_v2[n:n+2] for n in range(0, len(list_combined_a_v2), 2)]
    return list_combined_a_v3 # 利用list comprehension讓每兩項組合在一起


def function_b (data):
    data_b = data - 3
    list_b = []
    num_b = 21
    while num_b >= data_b:
        list_b.append(num_b)
        num_b -= 1
    list_b.append("_")
    list_b_sublist = [list(reversed(list_b[n:n+2])) for n in range(0, len(list_b), 2)]
    return list_b_sublist

def sequence(data_a):
    data_b = data_a - 3
    result_list_a = function_a(data_a)
    result_list_b = function_b(data_b)

    newlist = []
    for i in zip(result_list_a, result_list_b):
        newlist.append(i[0])
        newlist.append(i[1])
    
    newlist2 = []
    for i in newlist:
        for j in i:
            newlist2.append(j)
    return newlist2

ans = sequence(-1000)

def func3(index):
    return ans[index]
#資料量一大就跑超級慢><
# 範例
print(func3(1))
print(func3(5))
print(func3(10))
print(func3(30))
print("==========")

# Task 4

# - Available Spaces: list/array containing number of available seats for each car.
# - Status Bitmap: string containing only 0 or 1. 0 means the corresponding car can
# serve passengers for now.
# - Passenger Number: number of incoming passengers

def func4 (sp, stat, n):
    stat_list = list(stat)
    check = []
    for i in range(len(sp)):
        if int(stat_list[i]) == 1:
            sp[i] = '_'
        else:
            sp[i] = abs(sp[i] - n)
            check.append(sp[i])
    vacancy = min(check)
    vacancy_check = sp.index(vacancy)
    return vacancy_check

# 範例
print(func4([3, 1, 5, 4, 3, 2], "101000", 2)) # print 5
print(func4([1, 0, 5, 1, 3], "10100", 4)) # print 4
print(func4([4, 6, 5, 8], "1000", 4)) # print 2

# Task 4是最有成就感的一題，行數少、花最少時間寫完、只有反找index的語法有跟AI做確認，可以說幾乎是我自己自行完成的！！棒棒