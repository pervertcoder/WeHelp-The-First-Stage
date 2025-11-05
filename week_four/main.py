from fastapi import FastAPI, Path, Query, Form, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

import urllib.request as request
import json
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

# ID編碼
id_list = []
for i in hotel_CH:
    hotel_id = i['_id']
    id_list.append(hotel_id)

#　中文名字
hotel_CH_name_list = [] 
for i in hotel_CH:
    hotel_CH_name = i['旅宿名稱']
    hotel_CH_name_list.append(hotel_CH_name)

hotel_id_name = list(zip(id_list, hotel_CH_name_list))
# print(hotel_id_name)
hotel_id_name_list = disconstructin(hotel_id_name)
hotel_id_name1 = divide_element(hotel_id_name_list, 2)

# 加入英文名字
for i in hotel_id_name1:
    order = hotel_id_name1.index(i)
    engname_order = find_index_id(hotel_id_name1, order)
    i.append(engname_order)

# 加入電話號碼
for k in range(len(hotel_id_name1)):
    hotel_phone = hotel_CH[k]['電話或手機號碼']
    hotel_id_name1[k].append(hotel_phone)

# print(hotel_id_name1)

app = FastAPI() # FastAPI物件
app.add_middleware(SessionMiddleware, secret_key='mysecret')

# 非靜態檔案處理路由，擺在上方

@app.get('/member')
def member(request:Request):
    if not request.session.get('login'):
        return RedirectResponse(url='/')
    return FileResponse('memberpage/memberpageindex.html')

# @app.post('/hotel/{id}')
# def hotel(id, hotelnum):
#     return RedirectResponse(url='/hotel/{id}')

@app.post('/login')
def login(request:Request, email:str=Form(...), password:str=Form(...)):
    if not email or not password:
        return RedirectResponse(url='ohoh?msg=請填寫帳號或密碼', status_code=303)
    elif email != 'abc@abc.com' or password != 'abc':
        return RedirectResponse(url='ohoh?msg=帳號或密碼不存在', status_code=303)
    else:
        request.session['login'] = True
        return RedirectResponse(url='/member', status_code=303)

@app.get('/ohoh')
def fail(msg: str = Query()):
    return FileResponse('failpage/failpageindex.html')

@app.get('/logout')
def logout(request:Request):
    request.session.pop('login', None)
    return RedirectResponse(url='/')

# 統一處理靜態檔案，擺在下方，才不會影響其他路由
app.mount('/memberpage', StaticFiles(directory='memberpage'))
app.mount('/failpage', StaticFiles(directory='failpage'))
app.mount('/', StaticFiles(directory='homepage', html=True))