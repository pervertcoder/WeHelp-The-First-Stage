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
def show_table(data_base_name, table_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {data_base_name}')
    mycursor.execute(f'''create table {table_name}(
        id int auto_increment primary key,
        name varchar(254) not null,
        email varchar(254) not null,
        password varchar(254) not null)'''
    )
    conn.commit()
    conn.close()
    print(f'table {table_name} created successfully')

# 顯示table
def show_table_data(database_name, table_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {database_name}')
    mycursor.execute(f'select * from {table_name}')
    result = [x for x in mycursor]
    conn.close()
    return result
check_data = show_table_data('memberdatabase', 'memberinfo')
check_name = [x[1] for x in check_data]
print(check_name)

# 資料寫進資料庫
def insert_info(table_name, columns, values):
    conn = get_db_connect()
    mycursor = conn.cursor()

    col_str = ','.join(columns)
    placeholder = ','.join(['%s'] * len(values))
    sql_command = f'insert into {table_name} ({col_str})values({placeholder})'
    mycursor.execute('use memberdatabase')
    mycursor.execute(sql_command, values)

    conn.commit()
    conn.close()
    print('data inserted successfully')



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
def regist_system(request:Request, regist_user_name = Form(...), regist_email = Form(...), regist_password = Form(...)):
    check = show_table_data('memberdatabase', 'memberinfo')
    stat_var = True
    if regist_user_name == '' or regist_email == '' or regist_password == '':
        stat_var = False
        return RedirectResponse(url='/ohoh?msg=請輸入姓名、電子郵件和密碼', status_code=303)
    for i in check:
        if regist_email == i[2]:
            stat_var = False
            break
    if stat_var:
        insert_info('memberinfo', ['name', 'email', 'password'], [regist_user_name, regist_email, regist_password])
        print('sign successfully')
        return RedirectResponse(url='/', status_code=303)
    else:
        return RedirectResponse(url='/ohoh?msg=重複的電子郵件', status_code=303)
        


@app.post('/login')
def login(request:Request, email = Form(...), password = Form(...)):
    check_data = show_table_data('memberdatabase', 'memberinfo')
    stat_var = False
    if  email.strip() == '' or password.strip() == '':
        return RedirectResponse(url='/ohoh?msg=請輸入電子郵件和密碼', status_code=303)
    for i in check_data:
        if email == i[2] and password == i[3]:
            request.session['user'] = email
            request.session['username'] = i[1]
            stat_var = True
            break
    if stat_var:
        return RedirectResponse(url='/member', status_code=303)
    else:
        return RedirectResponse(url='/ohoh?msg=電子郵件或密碼錯誤', status_code=303)
    
@app.get('/member')
def member(request:Request):
    # check_data = show_table_data('memberdatabase', 'memberinfo')
    # check_name = [x[1] for x in check_data]
    user_state = request.session.get('user')
    user_name = request.session.get('username')
    if not user_state:
        return RedirectResponse(url='/')
    return template.TemplateResponse('memberpageindex.html', {
        'request' : request,
        'member_title' : 'memberpage',
        'member_h1' : '歡迎光臨，這是會員頁',
        'successful_message' : f'{user_name}，歡迎登入系統',
        'logout_a' : '登出系統',
    })
@app.get('/logout')
def logout (request:Request):
    request.session.clear()
    return RedirectResponse(url='/')

@app.get('/ohoh')
def failpage(request:Request, msg:str):
    if msg == '請輸入姓名、電子郵件和密碼': # 註冊
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '請輸入姓名、電子郵件和密碼',
        'fail_title' : 'failpage',
    })
    if msg == '重複的電子郵件': # 註冊
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '重複的電子郵件',
        'fail_title' : 'failpage',
    })
    if msg == '電子郵件或密碼錯誤':  # 登入
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '電子郵件或密碼錯誤',
        'fail_title' : 'failpage',
    })
    if msg == '請輸入電子郵件和密碼': # 登入
        return template.TemplateResponse('failpageindex.html', {
        'request' : request,
        'fail' : '失敗頁面',
        'error_message' : '請輸入電子郵件和密碼',
        'fail_title' : 'failpage',
    })


# 統一處理靜態檔案
app.mount('/StaticFiles', StaticFiles(directory='StaticFiles'))