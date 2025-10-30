import time
import random
import csv
# 第一頁
import urllib.request as rep
url_ppt = 'https://www.ptt.cc/bbs/Steam/index.html'
request = rep.Request(url_ppt, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
with rep.urlopen(request) as ppt_response: # 打開需求
    ppt_data = ppt_response.read().decode('utf-8') # 讀取需求

import bs4
root = bs4.BeautifulSoup(ppt_data, 'html.parser')
titles = root.find_all('div', class_= 'title')
num = root.find_all ('div', class_= 'nrec')

# 第一頁文章標題
artile_name = []
for title in titles:
    if title.a != None:
        artile_name.append (title.a.string)
# print(artile_name)

# 第一頁按讚數
num_good = []
for good in num:
    if good.span != None:
        num_good.append(good.span.string)
    else: num_good.append(0)
# print(num_good)

# 第一頁的文章內文，發文時間
def get_data_time(url_publish):
    request_pub = rep.Request(url_publish, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
    with rep.urlopen(request_pub) as publish_time:
        publish_data = publish_time.read().decode('utf-8')
    
    root_publish = bs4.BeautifulSoup(publish_data, 'html.parser')
    time_div = root_publish.find_all('div', class_='article-metaline')
    publish = None
    for time in time_div:
        tag = time.find('span', class_= 'article-meta-tag')
        value = time.find('span', class_= 'article-meta-value')
        if tag and tag.string.strip() == '時間' and value:
            publish = value.get_text(strip=True)
            break
    return(publish)

t = []
for i in range(len(titles)):
    urll = get_data_time('https://www.ptt.cc' + titles[i].a['href'])
    if urll is not None:
        t.append(urll)
    else:
        t.append('blank')

time.sleep(random.uniform(0.5, 1))

# print(t)

result_page_one = []
for titlee, number, datee in zip(artile_name, num_good, t):
    result_page_one.append([titlee, number, datee])

print(result_page_one)

def get_page (link_response):
    html_style_reader = bs4.BeautifulSoup(link_response, 'html.parser')
    next_line =html_style_reader.find('a', string='‹ 上頁')
    return next_line['href']

next_page = 'https://www.ptt.cc' + get_page(ppt_data)
print(next_page)
# 第二頁

url_ppt2 = next_page
request_page2 = rep.Request(url_ppt2, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
with rep.urlopen(request_page2) as ppt_response2:
    ppt_data2 = ppt_response2.read().decode('utf-8')

root2 = bs4.BeautifulSoup(ppt_data2, 'html.parser')
titles2 = root2.find_all('div', class_= 'title')
num2 = root2.find_all('div', class_='nrec')

# 第二頁文章標題
artile_name2 = []
for title2 in titles2:
    if title2.a != None:
        artile_name2.append (title2.a.string)
print(artile_name2)

# 第二頁按讚數
num_good2 = []
for good2 in num2:
    if good2.span != None:
        num_good2.append(good2.span.string)
    else: num_good2.append(0)
print(num_good2)