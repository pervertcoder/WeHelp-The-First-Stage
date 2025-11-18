from fastapi import FastAPI, Path, Query, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
import requests

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
# 連線MySQL
def get_db_connect():
    mydb = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
    )
    return mydb

# 創造database
def create_database(database_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'create database {database_name}')
    conn.commit()
    conn.close()
    print(f'Database {database_name} created successfully')

# 顯示databases
def show_databases ():
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute('show databases')
    db_list = [x[0] for x in mycursor]
    conn.close()
    return db_list

# 創造table
def show_table(data_base_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {data_base_name}')
    mycursor.execute('show tables')
    table_list = [table[0] for table in mycursor]
    conn.close()
    return table_list

# print(show_databases())
# 11/18進度：寫入資料進入資料庫
# 註冊、登入、登出
app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key = 'mysecretkey123')
template = Jinja2Templates(directory='templates')

@app.get ('/')
def root(request:Request):
    return template.TemplateResponse('index.html', {
        'request' : request,
        'regist_system' : '註冊帳號',
        'user_name' : '姓名',
        'regist_btn' : '註冊',
        'title' : '會員登入系統',
        'welcome' : '歡迎光臨，請註冊登入系統',
        'login_system' : '登入系統',
        'mail_html' : '信箱',
        'password_html' : '密碼',
        'agreement' : '同意條款',
        'login_btn' : '登入',
        'get_hotel_information' : '取得旅館資訊',
        'order' : '編號',
        'get_information' : '取得',
    })

@app.post('/signup')
def regist_system(user_name = Form(...), email = Form(...), password = Form(...)):
    pass
@app.post('/login')
def login(request:Request, email = Form(...), password = Form(...)):
    pass
    
    return RedirectResponse(url='/ohoh', status_code=303)
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
# @app.get('/logout')
# def logout (request:Request):
#     request.session.clear()
#     return RedirectResponse(url='/')

# @app.get('/ohoh')
# def failpage(request:Request, msg):
#     if msg == '帳號或密碼不存在':
#         return template.TemplateResponse('failpageindex.html', {
#         'request' : request,
#         'fail' : '失敗頁面',
#         'error_message' : '帳號或密碼不存在',
#         'fail_title' : 'failpage',
#     })
#     else:
#         msg = '請輸入帳號和密碼'
#         return template.TemplateResponse('failpageindex.html', {
#         'request' : request,
#         'fail' : '失敗頁面',
#         'error_message' : '請輸入帳號和密碼',
#         'fail_title' : 'failpage',
#     })

# @app.get('/hotel/{hotelnum}')
# def hotel_infor(request:Request, hotelnum:int):
#     tem_list = []
#     answer = ''
#     if hotelnum > 0 and hotelnum < 621:
#         for i in hotel_list:
#             if int(hotelnum) == int(i[0]):
#                 tem_list.extend(i[1:4])
#                 print(tem_list)
#         answer = '、'.join(tem_list)
#         return template.TemplateResponse('hotelpageindex.html', {
#             'request' : request,
#             'hotel_title' : 'hotelpage',
#             'hotel_h1' : '旅館資訊',
#             'back_home' : '返回首頁',
#             'hotelinfor' : answer,
#     })
#     else:
#         return template.TemplateResponse('hotelpageindex.html', {
#             'request' : request,
#             'hotel_title' : 'hotelpage',
#             'hotel_h1' : '旅館資訊',
#             'back_home' : '返回首頁',
#             'hotelinfor' : '查詢不到相關資料',
#     })


# 統一處理靜態檔案
app.mount('/StaticFiles', StaticFiles(directory='StaticFiles'))