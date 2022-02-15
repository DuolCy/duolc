import json
import os,subprocess,re
# cmd = r'cd C:\Users\admin\Desktop\yue'
# os.popen(cmd,'r',1)
# a= 'y123456'
# print(re.compile(r'/[^\w\.\/]/ig').findall(a))

# str = 'qweqw964373975@qq.comwqewqe'
# # print(re.compile(r'^\d{2}?').findall(str))
# print(re.findall('[\d0-9]+@\w{2}.com',str))
# print(re.findall('qe$',str))
# str = re.sub('12','哈哈',str)
# print(str)
import urllib3,urllib,requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

from pip._vendor.packaging.version import parse

http = urllib3.PoolManager()  # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
# url = 'http://www.baidu.com/s'
# response = http.request('GET', url) # get方式请求
# response=http.request('GET',url,fields={'wd':'python'})
# print(response.status,response.data.decode('utf-8'))  # 获得状态码, html源码(utf-8解码)
# url_p = 'http://127.0.0.1:5000/login'
# url_m = urlencode({'username':'ceshi','password':'123456'})
# response=http.request(method='post',url=url_p,fields={'username':'ceshi','password':'123456'})
# print(response.status,response.data.decode('utf-8'))
# url = 'https://movie.douban.com/top250?start=25'
# resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})
# html = resp.text

# print(re.compile(r'<img width="100" alt="(.+?)" ').findall(html))
# print(re.findall(r'<img width="100" alt="(.+?)" ',html))
# print(re.findall(r'导演: (.*?)&nbsp;&nbsp;&nbsp;主演:',html))
# print(re.findall(r' <span>(.*?)人评价</span>',html))
# url = 'https://top.baidu.com/board?tab=realtime'
# resp = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'})
# html = resp.text
# # print(html)
# msg = re.findall(r'_nSuFU "> (.*?) <a href=',html)
# # print(re.findall('<a href="(.*?)" class="look-more_3oNWC" target="_blank">查看更多&gt;</a> </div> <!--/s-frag--> </div',html))
# msg_c = []
# with open('./test_prac.csv',mode='a',encoding='utf-8') as f :
#     for i in range(0,len(msg)):
#         msg_c.append(msg[i]+'\n')
#     f.writelines(msg_c)
url = 'https://s.weibo.com/top/summary?cate=realtimehot/'
resp = requests.get(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400','cookie': 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894:'})
html = resp.text
# resp.encoding('utf-8')
soup = BeautifulSoup(html)
print(soup.prettify())
# html_msg = 'target="_blank">(.*?)</a>'
# html_url = '<a href="(.*?)" target="_blank">'
# url_weibo= 'https://s.weibo.com'

