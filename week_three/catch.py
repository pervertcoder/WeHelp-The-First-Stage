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


file = open('hotel.csv', mode='w', newline='', encoding='utf-8')
writer = csv.writer(file)
for i in new_result:
    writer.writerow(i)
file.close()