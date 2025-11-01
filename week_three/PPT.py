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
        t.append("' '")

time.sleep(random.uniform(0.5, 1))

# print(t)

result_page_one = []
for titlee, number, datee in zip(artile_name, num_good, t):
    result_page_one.append([titlee, number, datee])

# print(result_page_one)

def get_page (link_response):
    html_style_reader = bs4.BeautifulSoup(link_response, 'html.parser')
    next_line =html_style_reader.find('a', string='‹ 上頁')
    return next_line['href']

next_page = 'https://www.ptt.cc' + get_page(ppt_data)
# print(next_page)
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
# print(artile_name2)

# 第二頁按讚數
num_good2 = []
for good2 in num2:
    if good2.span != None:
        num_good2.append(good2.span.string)
    else: num_good2.append(0)
# print(num_good2)

# 第二頁的文章內文，發文時間
t2 = []
for h in range(len(titles2)):
    urll2 = get_data_time('https://www.ptt.cc' + titles2[h].a['href'])
    if urll2 is not None:
        t2.append(urll2)
    else:
        t2.append("' '")

time.sleep(random.uniform(0.5, 1))

# print(t2)
result_page_two = []
for titlee2, number2, datee2 in zip(artile_name2, num_good2, t2):
    result_page_two.append([titlee2, number2, datee2])

# print(result_page_two)

next_page2 = 'https://www.ptt.cc' + get_page(ppt_data2)

url_ppt3 = next_page2
request_page3 = rep.Request(url_ppt3, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'})
with rep.urlopen(request_page3) as ppt_reponse3:
    ppt_data3 = ppt_reponse3.read().decode('utf-8')

root3 = bs4.BeautifulSoup(ppt_data3, 'html.parser')
titles3 = root3.find_all('div', class_= 'title')
num3 = root3.find_all('div', class_='nrec')

# 第三頁文章標題
artile_name3 = []
for title3 in titles3:
    if title3.a != None:
        artile_name3.append (title3.a.string)
# print(artile_name3)

# 第三頁按讚數
num_good3 = []
for good3 in num3:
    if good3.span != None:
        num_good3.append(good3.span.string)
    else: num_good3.append(0)
# print(num_good3)

# 第三頁的文章內文，發文時間

t3 = []
for h in range(len(titles3)):
    urll3 = get_data_time('https://www.ptt.cc' + titles3[h].a['href'])
    if urll3 is not None:
        t3.append(urll3)
    else:
        t3.append("' '")

time.sleep(random.uniform(0.5, 1))

# print(t3)

result_page_three = []
for titlee3, number3, datee3 in zip(artile_name3, num_good3, t3):
    result_page_three.append([titlee3, number3, datee3])

# print(result_page_three)

the_final_result = []
the_final_result.extend(result_page_one)
the_final_result.extend(result_page_two)
the_final_result.extend(result_page_three)
print(the_final_result)

# csv檔案寫入
file = open('article.csv', mode='w', newline='', encoding='utf-8')
writer = csv.writer(file)
for i in the_final_result:
    writer.writerow(i)
file.close()