
import urllib.request as request
import json
import csv
url_CH = 'https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch'
with request.urlopen(url_CH) as response_CH:
    data_CH = json.load(response_CH)
hotel_CH = data_CH['list']

url_EN = 'https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en'
with request.urlopen(url_EN)as response_EN:
    data_EN = json.load(response_EN)
hotel_EN = data_EN['list']

# 解構元組
def disconstructin (lis):
    empty_list = []
    for i in lis:
     for j in i:
         empty_list.append(j)
    return empty_list

# 分隔元素
def divide_element(lis, num):
    new_result = []
    for i in range(0, len(lis), num):
        new_result.append(lis[i:i + num])
    return new_result

# 找英文名字
def find_index_id (lis, n):
    for i in hotel_EN:
        if i['_id'] == lis[n][0]:
            index = hotel_EN.index(i)
    return hotel_EN[index]['hotel name']

# 找英文地址
def find_index_id_adress (lis, n):
    for i in hotel_EN:
        if i['_id'] == lis[n][0]:
            index = hotel_EN.index(i)
    return hotel_EN[index]['address']

# ID編碼
id_list = []
for i in hotel_CH:
    hotel_id = i['_id']
    id_list.append(hotel_id)
# print(id_list)

#　中文名字
hotel_CH_name_list = [] 
for i in hotel_CH:
    hotel_CH_name = i['旅宿名稱']
    hotel_CH_name_list.append(hotel_CH_name)
# print(hotel_CH_name_list)

hotel_id_name = list(zip(id_list, hotel_CH_name_list))
# print(hotel_id_name)
hotel_id_name_list = disconstructin(hotel_id_name)
hotel_id_name1 = divide_element(hotel_id_name_list, 2)
print(hotel_id_name1)

# 加入英文名字
for i in hotel_id_name1:
    order = hotel_id_name1.index(i)
    engname_order = find_index_id(hotel_id_name1, order)
    i.append(engname_order)
# print (hotel_id_name1)

# 加入中文地址
for h in range(len(hotel_id_name1)):
    hotel_CH_address = hotel_CH[h]['地址']
    hotel_id_name1[h].append(hotel_CH_address)

# 加入英文地址
for j in hotel_id_name1:
    order = hotel_id_name1.index(j)
    engaddress = find_index_id_adress(hotel_id_name1, order)
    j.append(engaddress)

# 加入電話
for k in range(len(hotel_id_name1)):
    hotel_phone = hotel_CH[k]['電話或手機號碼']
    hotel_id_name1[k].append(hotel_phone)

# 加入房間數
for l in range(len(hotel_id_name1)):
    hotel_room = hotel_CH[l]['房間數']
    hotel_id_name1[l].append(hotel_room)
# print(hotel_id_name1)

for w in hotel_id_name1:
    del w[0]
print(hotel_id_name1)

# 行政區
district = []
for area in hotel_id_name1:
    small_area = area[2][3:6]
    district.append(small_area)
    # print(district)


# # 房間數
room_count = []
for room in hotel_id_name1:
    room_count.append(room[5])
    # print(room_count)

district_room_count = list(zip(district, room_count))
# print(district_room_count)

taipei_district = ['北投區', '士林區', '內湖區', '南港區', '文山區', '大同區', '中山區', '松山區', '信義區', '大安區', '中正區', '萬華區']

district_1 = []
for i in district_room_count:
    if i[0] == taipei_district[0]:
        district_1.append(i)

hotel_num = len(district_1)

district_1_hotel_room = []
for i in district_1:
    district_1_hotel_room.append(i[1])

sum_district_1_hotel_room = 0
for i in district_1_hotel_room:
    sum_district_1_hotel_room += int(i)

D1 = [[taipei_district[0], hotel_num, sum_district_1_hotel_room]]
# print(D1)

def district_maker(lis, dis):
    district_num = []
    for i in lis:
        if i[0] == dis:
            district_num.append(i)
    
    hotel_n = len(district_num)

    district_hotel_rom = []
    for j in district_num:
        district_hotel_rom.append(j[1])
    
    sum_district_num_hotel_room = 0
    for h in district_hotel_rom:
        sum_district_num_hotel_room +=  int(h)
    
    D = [dis, hotel_n, sum_district_num_hotel_room]
    return D


district_result = []
for i in taipei_district:
    district_result.append(district_maker(district_room_count, i))


print (district_result)


# # csv檔案寫入
# file = open('hotel.csv', mode='w', newline='', encoding='utf-8-sig')
# writer = csv.writer(file)
# for i in hotel_id_name1:
#     writer.writerow(i)
# file.close()


# # csv檔案寫入
# file = open('district.csv', mode='w', newline='', encoding='utf-8-sig')
# writer = csv.writer(file)
# for i in district_result:
#     writer.writerow(i)
# file.close()