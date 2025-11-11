from fastapi import FastAPI, Path, Query, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
import requests
data_ch = requests.get('https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch')
data_en = requests.get('https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en')
data_ch.encoding = 'utf-8'
content_ch = data_ch.json()
content_en = data_en.json()
hotel_ch = content_ch['list']
hotel_en = content_en['list']
# print(hotel_ch)
# print(hotel_en)

hotel_ch_list = []
for hotels in hotel_ch:
    hotel_ch_list.append(hotels['_id'])
    hotel_ch_list.append(hotels['旅宿名稱'])
# print(hotel_ch_list)

hotel_list = []
for h in range(0, len(hotel_ch_list), 2):
    hotel_list.append(hotel_ch_list[0+h:h+2])
# print(hotel_list)

for i in hotel_en:
    for h in hotel_list:
        if i['_id'] == h[0]:
            h.append(i['hotel name'])

for m in hotel_ch:
    for l in hotel_list:
        if m['_id'] == l[0]:
            l.append(m['電話或手機號碼'])
# print (hotel_list)







app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key = 'mysecretkey123')
template = Jinja2Templates(directory='templates')

@app.get ('/')
def root(request:Request):
    return template.TemplateResponse('index.html', {
        'request' : request,
        'title' : '會員登入系統',
        'welcome' : '歡迎光臨，請輸入信箱密碼',
        'login_system' : '登入系統',
        'mail_html' : '信箱',
        'password_html' : '密碼',
        'agreement' : '同意條款',
        'login_btn' : '登入',
        'get_hotel_information' : '取得旅館資訊',
        'order' : '編號',
        'get_information' : '取得',
    })

@app.post('/login')
def login(request:Request, email = Form(...), password = Form(...)):
    if email == 'abc@abc.com' and password == 'abc':
        request.session['user'] = email
        print(request.session['user'])
        return RedirectResponse(url='/member', status_code=303)
    if email == '' or password == '':
        return RedirectResponse(url='/ohoh?msg=請輸入帳號或密碼', status_code=303)
    if email != 'abc@abc.com' or password != 'abc':
        return RedirectResponse(url='/ohoh?msg=帳號或密碼不存在', status_code=303)
    
    # return RedirectResponse(url='/ohoh', status_code=303)
@app.get('/member')
def member(request:Request):
    user_state = request.session.get('user')
    if not user_state:
        return RedirectResponse(url='/')
    return template.TemplateResponse('memberpageindex.html', {
        'request' : request,
        'member_title' : 'memberpage',
        'member_h1' : '歡迎光臨，這是會員頁',
        'successful_message' : '恭喜您，成功登入系統',
        'logout_a' : '登出系統',
    })
@app.get('/logout')
def logout (request:Request):
    request.session.clear()
    return RedirectResponse(url='/')

@app.get('/ohoh')
def failpage(request:Request, msg):
    if msg == '帳號或密碼不存在':
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '帳號或密碼不存在',
        'fail_title' : 'failpage',
    })
    else:
        msg = '請輸入帳號和密碼'
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '請輸入帳號和密碼',
        'fail_title' : 'failpage',
    })

@app.get('/hotel/{hotelnum}')
def hotel_infor(request:Request, hotelnum:int):
    tem_list = []
    answer = ''
    if hotelnum > 0 and hotelnum < 621:
        for i in hotel_list:
            if int(hotelnum) == int(i[0]):
                tem_list.extend(i[1:4])
                print(tem_list)
        answer = '、'.join(tem_list)
        return template.TemplateResponse('hotelpageindex.html', {
            'request' : request,
            'hotel_title' : 'hotelpage',
            'hotel_h1' : '旅館資訊',
            'back_home' : '返回首頁',
            'hotelinfor' : answer,
    })
    else:
        return template.TemplateResponse('hotelpageindex.html', {
            'request' : request,
            'hotel_title' : 'hotelpage',
            'hotel_h1' : '旅館資訊',
            'back_home' : '返回首頁',
            'hotelinfor' : '查詢不到相關資料',
    })

# @app.post('/hotel_order')
# def hotelinformation():


# 統一處理靜態檔案
app.mount('/StaticFiles', StaticFiles(directory='StaticFiles'))