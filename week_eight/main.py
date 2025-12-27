from fastapi import *
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests

url = 'https://lver76.pixnet.net/blog/posts/3035422107'
headers = {'user-agent': 'Mozilla/5.0'}
data = requests.get(url, headers=headers)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')
par = soup.find('div',{'id' : 'article-content-inner'})
content = par.get_text()
new_content = content.replace(',', '，')
final_content = new_content + '間隔第十四'
# print(final_content)


sub_title = ['作戰第二', '謀攻第三', '軍形第四', '兵勢第五', '虛實第六', '軍爭第七', '九變第八', '行軍第九', '地形第十', '九地第十一', '火攻地十二', '用間第十三', '間隔第十四']
# '始計第一原文'
sub_ans = []
def split_maker(str):
    for i in range(13):
        lis = str.split(str[str.index(sub_title[i]):str.index(sub_title[i])+4], maxsplit=1)
        sub_ans.append(lis[0])
        lis.remove(lis[0])
        str = lis[0]
    return sub_ans

a = split_maker(final_content)


sub_ans2 = []
for i in a:
    sub_lis = i.split('譯')
    sub_ans2.append(sub_lis)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins = ['http://127.0.0.1:5000'],
    allow_origins = ['*'],
    allow_methods = ['*'],
    allow_headers = ['*'],
)
# 'http://127.0.0.1:5000'


@app.get('/content')
def get_content():
    return sub_ans2



app.mount('/static', StaticFiles(directory='static'), name='static')
# Static Pages (Never Modify Code in this Block)
@app.get("/", include_in_schema=False)
async def index(request: Request):
	return FileResponse("./static/index.html", media_type="text/html")