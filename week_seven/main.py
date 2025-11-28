from fastapi import FastAPI, Path, Query, Form, Request, Body
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
import json
from pydantic import BaseModel

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

# 顯示table特定資料
def show_table_data(database_name, table_name, column, email):
    conn = get_db_connect()
    mycursor = conn.cursor()
    database_sql = f'use {database_name}'
    select_sql = f'select * from {table_name} where {column} = %s'
    mycursor.execute(database_sql)
    mycursor.execute(select_sql, (email,))
    result = [x for x in mycursor]
    conn.close()
    return result

# print(show_table_data('memberdatabase', 'memberinfo', 'name', 'aa'))

# 顯示會員資料
def show_member_data(database_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {database_name}')
    mycursor.execute('''select
        id,
        name,
        email
        from memberinfo
    ''')
    result = [x for x in mycursor]
    return result

# 顯示會員名字
def show_member_name(data_base_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {data_base_name}')
    mycursor.execute('select name from memberinfo')
    result = [x for x in mycursor]
    return result


# 顯示搜尋資料
def show_search_history(database_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute(f'use {database_name}')
    mycursor.execute(
        '''
        select
        search_history.id,
        memberinfo.name as search_person_name,
        target_user_id,
        search_time
        from search_history
        join memberinfo on search_history.search_person_id = memberinfo.id
        order by search_time desc'''
    )
    result = [x for x in mycursor]
    return result

# print(show_search_history('memberdatabase'))

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

# 修改資料庫的資料
def change_name(member_email, new_name):
    conn = get_db_connect()
    mycursor = conn.cursor()
    mycursor.execute('use memberdatabase')
    mysql_command = 'update memberinfo set name = %s where email = %s'
    mycursor.execute(mysql_command, (new_name, member_email))

    conn.commit()
    print('修改成功')
    result = show_table_data('memberdatabase', 'memberinfo', 'name', new_name)
    conn.close()
    return True

# print(change_name('aaa', 'aa'))

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
def regist_system(regist_user_name = Form(...), regist_email = Form(...), regist_password = Form(...)):
    check_email = show_table_data('memberdatabase', 'memberinfo', 'email', regist_email)
    stat_var = True
    if check_email:
        stat_var = False
    if stat_var:
        insert_info('memberinfo', ['name', 'email', 'password'], [regist_user_name, regist_email, regist_password])
        print('sign successfully')
        return RedirectResponse(url='/', status_code=303)
    else:
        return RedirectResponse(url='/ohoh?msg=重複的電子郵件', status_code=303)
        
@app.post('/login')
def login(request:Request, email = Form(...), password = Form(...)):
    check_data = show_table_data('memberdatabase', 'memberinfo', 'email', email)
    stat_var = False
    for i in check_data:
        if email == i[2] and password == i[3]:
            request.session['user'] = email
            request.session['username'] = i[1]
            request.session['user_id'] = i[0]
            stat_var = True
            break
    if stat_var:
        print(request.session)
        return RedirectResponse(url='/member', status_code=303)
    else:
        return RedirectResponse(url='/ohoh?msg=電子郵件或密碼錯誤', status_code=303)
    
@app.get('/member')
def member(request:Request):
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
        'nameContent' : '查詢會員姓名',
        'search' : '查詢',
        'new_name' : '更新我的名字',
        'update' : '更新',
        'who' : '誰查詢了我',
        'refresh' : '更新'
    })

@app.patch('/api/member')
def update_name(request:Request, body:dict=Body(...)):
    member_email = request.session.get('user')
    if member_email:
        new_name = body['name']
        print(member_email, new_name)
        answer = change_name(member_email, new_name)
        request.session['username'] = new_name
        return {'ok' : answer}
    else:
        return {'error':True}

@app.get('/api/member/{member_id}')
def search_member (request:Request, member_id:int):
    login_user_id = request.session.get('user_id')
    print(login_user_id)
    member_data = show_member_data('memberdatabase')
    data_lis = [i for i in member_data]
    data_id = [i[0] for i in data_lis]
    find_index = True
    if member_id in data_id:
        index = data_id.index(member_id)
    else:
        find_index = False
    if find_index:
        insert_info('search_history', ['search_person_id', 'target_user_id'], [login_user_id, data_lis[index][0]])
        return {'id' : data_lis[index][0], 'name' : data_lis[index][1], 'email' : data_lis[index][2]}
    else:
        return {'id' : None}

@app.get('/search')
def search_history(request:Request):
    user_id = request.session.get('user_id')
    search_data = show_search_history('memberdatabase')
    history_data = [i for i in search_data]
    result = []
    result_time = []
    
    for i in history_data:
        if user_id == i[2]:
            result.append(i[1])
            result_time.append(i[3])
      
    return {'name' : result, 'time' : result_time}
    

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