from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests
import re


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'], #'http://127.0.0.1:5000'
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# @app.get('/')
# def test_api():
#     return {'test' : 'ok'}

url = 'https://lver76.pixnet.net/blog/post/35422107'
data = requests.get(url)
data.encoding = 'utf-8'
soup = BeautifulSoup(data.text, 'html.parser')
par = soup.find('div',{'id' : 'article-content-inner'})
content = par.get_text()
final_content = content + '間隔第十四'
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


@app.get('/content')
def get_content():
    return sub_ans2