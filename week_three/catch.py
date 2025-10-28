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


#　中文名字
hotel_CH_name_list = [] 
for i in hotel_CH:
    hotel_CH_name = i['旅宿名稱']
    hotel_CH_name_list.append(hotel_CH_name)

# print(hotel_CH_name_list)


# 英文名字
hotel_EN_name_list = [] 
for i in hotel_EN:
    hotel_EN_name = i['hotel name']
    hotel_EN_name_list.append(hotel_EN_name)

# print(hotel_EN_name_list)


# 中英名字混和
name_CH_EN_list = list(zip(hotel_CH_name_list, hotel_EN_name_list)) 


# 中文地址
hotel_address_CH_list = []
for i in hotel_CH:
    hotel_addrss_CH = i['地址']
    hotel_address_CH_list.append(hotel_addrss_CH)
# print(hotel_address_CH_list)


# 英文地址
hotel_address_EN_list = []
for i in hotel_EN:
    hotel_addrss_EN = i['address']
    hotel_address_EN_list.append(hotel_addrss_EN)
# print(hotel_address_EN_list)


# 中英混和地址
adress_CH_EN_list = list(zip(hotel_address_CH_list, hotel_address_EN_list))
# print(adress_CH_EN_list)


middle_result = list(zip(name_CH_EN_list, adress_CH_EN_list))
# print(middle_result)

# 手機
hotel_telephone = []
for i in hotel_CH:
    hotel_telephone_CH = i['電話或手機號碼']
    hotel_telephone.append(hotel_telephone_CH)
# print (hotel_telephone)


# 房間數
hotel_room = []
for i in hotel_CH:
    hotel_room_CH = i['房間數']
    hotel_room.append(hotel_room_CH)
# print(hotel_room)

# 手機+房間數
telephone_room = list(zip(hotel_telephone, hotel_room))
# print(telephone_room)


middle_result2 = list(zip(middle_result, telephone_room))
# print(middle_result2)


a = disconstructin(middle_result2)
b = disconstructin(a)
# print(b)


# 展開全部的元素
result = []
for i in b:
    if type(i) == tuple:
        for j in i:
            result.append(j)
    else:
        result.append(i)
# print(result)


# 讓每六個元素組成一個list
new_result = []
second_layer = []
for i in range(0, len(result), 6):
    new_result.append((result[i:i+6]))
# print(new_result)

# csv檔案寫入
file = open('hotel.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
for i in new_result:
    writer.writerow(i)
file.close()

# 行政區
district = []
for area in new_result:
    small_area = area[2][3:6]
    district.append(small_area)
    # print(district)


# 房間數
room_count = []
for room in new_result:
    room_count.append(room[5])
    # print(room_count)

district_room_count = list(zip(district, room_count))
# print(district_room_count)

taipei_district = ['北投區', '士林區', '內湖區', '南港區', '文山區', '大同區', '中山區', '松山區', '信義區', '大安區', '中正區', '萬華區']

# district_1 = []
# for i in district_room_count:
#     if i[0] == taipei_district[0]:
#         district_1.append(i)

# hotel_num = len(district_1)

# district_1_hotel_room = []
# for i in district_1:
#     district_1_hotel_room.append(i[1])

# sum_district_1_hotel_room = 0
# for i in district_1_hotel_room:
#     sum_district_1_hotel_room += int(i)

# D1 = [[taipei_district[0], hotel_num, sum_district_1_hotel_room]]
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


# print (district_result)


# csv檔案寫入
file = open('district.csv', mode='w', newline='', encoding='utf-8-sig')
writer = csv.writer(file)
for i in district_result:
    writer.writerow(i)
file.close()