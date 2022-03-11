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
import smtplib
from functools import reduce

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
# #     f.writelines(msg_c)
# url = 'https://s.weibo.com/top/summary?cate=realtimehot/'
# resp = requests.get(url,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400','cookie': 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894:'})
# html = resp.text
# # resp.encoding('utf-8')
# soup = BeautifulSoup(html)
# print(soup.prettify())
# html_msg = 'target="_blank">(.*?)</a>'
# html_url = '<a href="(.*?)" target="_blank">'
# url_weibo= 'https://s.weibo.com'

# from bs4 import BeautifulSoup
# # soup = BeautifulSoup('<p class="Web site url"><b>c.biancheng.net</b></p>', 'html.parser')
# soup = BeautifulSoup(html)
# print(soup.prettify())
# #获取整个p标签的html代码
# print('获取整个p标签的html代码:',soup.p)
# #获取b标签
# print('获取b标签:',soup.p.b)
# #获取p标签内容，使用NavigableString类中的string、text、get_text()
# print('获取p标签内容:',soup.p.text)
# #返回一个字典，里面是多有属性和值
# print(soup.p.attrs)
# #查看返回的数据类型
# print(type(soup.p))
# #根据属性，获取标签的属性值，返回值为列表
# print(soup.p['class'])
# #给class属性赋值,此时属性值由列表转换为字符串
# soup.p['class']=['Web','Site']
# print(soup.p)

#
# #操作excel
# #1.导入包
# import xlwings as xw
#
# #2.打开空程序
# app = xw.App(visible = True, add_book = False)
#
# #3.操作工作簿
# #case1：生成一个新工作簿
# wb = app.books.add()
# wb.save(r'.\T.xlsx')
# #case2：打开已存在的工作簿
# wb = app.books.open(r'.\T.xlsx')
# #case3：也可以直接连接已打开的工作簿
# app = xw.apps.active
# wb = xw.books['test.xlsx']
#
# #4.添加表单
# ws = wb.sheets.add('Sheet_name')
# # add()为默认表单名，也可以修改表单名
# ws.name = 'Sheet_name1'
#
# #5.切换表单
# # 显示当前工作簿中所有表单
# wb.sheets
# # 获取工作簿中表单个数
# nSheets = wb.sheets.count
# # 引用第i个表单
# ws = wb.sheets[0]
# # 引用名为‘Sheet_name’的表单
# ws = wb.sheets('Sheet_name')
# # 将所引用的表单设为活动表单
# ws.activate()
# # 引用活动表单
# ws = wb.sheets.active
#
# # 6.删除表单
# wb.sheets('Sheet_name').delete()
#
# # 7.写入数据
# data = ['北京', '上海', '广州', '深圳', '香港', '澳门', '台湾']
# # 行：
# ws.range('A1').value = data
# # 列：
# ws.range('A1').options(transpose=True).value = data
#
# # 8.遍历表单内容
# # 获取表单使用信息：
# info = ws.used_range
# # 行数：
# nrows = info.last_cell.row
# # 列数：
# ncols = info.last_cell.column
#
# # 9.读取数据
# # 单元格读取：
# data = ws.range('A1')
# # 部分读取：
# data = ws.range('A1:D1').value
# data = ws.range('A1:D3').value
# # 整行读取：
# data = ws.range('A1').expand('right').value
# # 整列读取：
# data = ws.range('A1').expand('down').value
# # 全部读取
# data = ws.range('A1').expand().value
# # 可使用：
# data = ws.range('A1').expand().value.options(transpose = True)#进行转置
#
# #10.删除数据
# # 删除指定单元格内容
# ws.range('A1').clear()
# # 全部清除
# ws.clear()
#
# #11.关闭工作簿
# wb.close()
#
# #12. 退出当前活动excel程序
# app.quit()

# #类
# class Person():
#     def __init__(self,age,name):
#
#         self.age=age
#         self.name=name
#     def eat(self):
#         print(f'{self.name} 有{self.age}岁了')
#     def play(self,who,where):
#         print(f'{who}在{where}玩游戏')
#     @classmethod
#     def drink(cls):
#         print('这个是类方法')
# # p = Person(100,'李')
# # print(p.name)
# # p.eat()
# # # p.drink()
# # p.play('张三','游乐园')
# # Person.drink()
#
# """输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']："""
# from functools import reduce
# def name(s):
#     str = s.lower()
#     str1 = str.capitalize()
#     return str1
# a= map(name,['adam', 'LISA', 'barT'])
# print(list(a))
# """Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积："""
# li = [3, 5, 7, 9]
# a = reduce(lambda x,y:x+y,li)
# b = reduce(lambda x,y:x*y,li)
# print(a,b)
# """利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456："""
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
# st = '123.456'
# #去掉小数点
# st1 = st.replace('.','')
# print(st1)
# #将str转为int
# def num(q):
#     return DIGITS[q]
# def num1(x,y):
#     return x*10 +y
# #小数点位数
# do = len(st)-st.index('.')
# #结果是惰性序列，需要list转
# print(list(map(num,st)))
# print(1111111,list(map(lambda q:DIGITS[q],st)))
# print(reduce(num1,map(num,st1))/10**(do-1))
#
# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(lambda x:x%2==1, [1, 2, 4, 5, 6, 9, 10, 15])))
# import os
# print(os.path.abspath('.'))#当前目录

#多进程
# import threading,time
# def eat(food):
#     for i in range(5):
#         print(f'正在吃{food}哦')
#         time.sleep(0.5)
# def drink(drinks):
#     # for i in range(5):
#     while 1:
#         print(f'小米正在喝{drinks}')
#         time.sleep(0.5)
# t1 = threading.Thread(target=eat,args=('面条',))#参数通过元祖传递
# t2 = threading.Thread(target=drink,args=('牛奶',))
# #线程的守护，守护线程随着被守护的线程结束而结束;需要放在启动之前
# t2.setDaemon(True)
# t1.start()
# t2.start()
#线程的阻塞
# t1.join(timeout=1)
# t2.join(timeout=1)

# print('当前进程的运行情况',threading.enumerate())
#邮件
# import yagmail
# def send_email():
#     sender = '15281186529@163.com'  # 发送邮箱
#     receivers = '964373975@qq.com'  # 接收邮箱
#     subject = 'test'
#     try:
#         smtp = yagmail.SMTP(user=sender, password='MAWMMMJZMGIERQBU', host='smtp.163.com')#不要加端口，加了会报错
#         smtp.send(to=receivers, subject=subject, contents='test11111111111111111111111')
#         # sbuject = 标题，contents = 正文,attachments= 附件
#         print('邮件发送成功')
#     except Exception as e:
#         print(f'发送失败,原因是{e}')
#     finally:
#         print(111)
# # send_email()
# str = 'TYYZWBD8AySrJVcm8yo8KnsqJJrbfXKNNM'
#
# print(len(str))

'''
        mock挡板
'''
from mock import mock
'''test 1'''

class Test1():
    def add(self,a,b):
       pass
def test_add():
    test = Test1()
    test.add = mock.Mock(return_value=3)
    print(test.add(1,64))
#  返回的是设置的3

'''test 2'''
class Test2():
    def add(self,a,b):
       return a+b
def test_add_2():
    test = Test2()
    test.add = mock.Mock(return_value=3,side_effect=test.add)
    print(test.add(1,64))
test_add_2()



# def add_and_multiply(x, y):
#     addition = x + y
#     multiple = multiply(x, y)
#     return (addition, multiple)
#
#
# def multiply(x, y):
#     return x * y
# print(add_and_multiply(1,2))
'''test 3'''

from unittest.mock import patch
def add_3(a,b):
    return a*b

class Add_and_proxy():
    def add_and_p(self,a,b):
        az = a+b
        add_3 = mock.Mock(return_value=10,side_effect=lambda a,b:a-b )#这两个都在时以return_value 为主
        # side_effect  这可以是调用mock时要调用的函数、iterable或要引发的异常（类或实例）,可以调用函数，可迭代对象，报错信息
        # return_value 替代函数的值
        print (az,add_3(a,b))
        # print (az,add_3(a,b))
        # print (az,add_3(a,b))

        # print(add_3.called)#返回TURE 或者FLASE mock是否被调用
        print(add_3.call_args)        #替代的内容
        print(add_3.return_value) #替代输出的值
# Add_and_proxy().add_and_p(3,4)
li = [1,2,3,4,5,6]
def addd(a):
    return a*a
# print(list(map(addd,li)))
print(list(map(lambda x:x*2 if x%2==0 else x*1,li)))
print(reduce(lambda x,y:x+y ,li))
