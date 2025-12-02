from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from bs4 import BeautifulSoup
# import requests

# url = 'https://lver76.pixnet.net/blog/post/35422107'
# data = requests.get(url)
# data.encoding = 'utf-8'
# soup = BeautifulSoup(data.text, 'html.parser')
# par = soup.find('div',{'id' : 'article-content-inner'})
# content = par.get_text()
# print(content)



# seperate1 = content.find('譯文：【始計第一】')
# seperate2 = content.find('作戰第二')
# seperate3 = content.find('譯文：【作戰第二】')
# first_para = content[:seperate1]
# first_para_trans = content[seperate1:seperate2]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['http://127.0.0.1:5000'],
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/')
def test_api():
    return {'test' : 'ok'}