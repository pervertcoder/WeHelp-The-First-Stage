from typing import Annotated
from fastapi import FastAPI, Path, Query
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI() # FastAPI物件

# 非靜態檔案處理路由，擺在上方
@app.get('/square/{num}')
def square(num:Annotated[int, Path(ge = 1)]):
    num = int(num)
    return {'result': num*num}

@app.get('/multiply')
def multiply(
    n1:Annotated[int, Query(ge = 0, le = 10)],
    n2:Annotated[int, Query(ge = 0, le = 10)]
):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 * n2
    return {'result': result}

@app.get('/echo/{name}')
def echo(name:Annotated[str, Path(min_length=2, max_length=30)]):
    return {'message':'hello ' + name}

@app.get('/hello')
def hello (name:Annotated[str, Query(min_length=3)]):
    return {'message': 'hello ' + name}

# 統一處理靜態檔案，擺在下方，才不會影響其他路由

app.mount('/', StaticFiles(directory='homepage', html=True))