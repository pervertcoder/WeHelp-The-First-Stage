from typing import Annotated
from fastapi import FastAPI, Path, Query, Form
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import re

app = FastAPI() # FastAPI物件

# 非靜態檔案處理路由，擺在上方

@app.get('/member')
def member():
    return FileResponse('memberpage/memberpageindex.html')

@app.post('/login')
def login(email:str=Form(...), password:str=Form(...)):
    if not email or not password:
        return RedirectResponse(url='ohoh?msg=請填寫帳號或密碼', status_code=303)
    elif email != 'abc@abc.com':
        return RedirectResponse(url='ohoh?msg=帳號不存在', status_code=303)
    elif password != 'abc':
        return RedirectResponse(url='ohoh?msg=密碼不存在', status_code=303)
    else:
        return RedirectResponse(url='/member', status_code=303)

@app.get('/ohoh')
def fail(msg: str = Query()):
    return FileResponse('failpage/failpageindex.html')

# 統一處理靜態檔案，擺在下方，才不會影響其他路由

app.mount('/failpage', StaticFiles(directory='failpage'))
app.mount('/', StaticFiles(directory='homepage', html=True))