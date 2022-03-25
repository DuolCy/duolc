"""
清华镜像源地址：
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/win-64/
https://pypi.tuna.tsinghua.edu.cn/simple/
"""
#cookie和user_agen 的有限期为1天
import datetime,configparser
from datetime import date

import requests,re,time
class Wb:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read('config.ini', encoding='utf-8')
        self.user_agen= self.conf.get('XL','user_agen')
        self.cookie= self.conf.get('XL','cookie')
        self.update_time= self.conf.get('XL','update_time')



    def wb(self):
        url = ['https://s.weibo.com/top/summary?cate=realtimehot/','https://s.weibo.com/top/summary?cate=entrank']
        for i in range(len(url)):
            resp = requests.get(url[i], headers={'user-agent': self.user_agen, 'cookie': self.cookie})
            html = resp.text
            html_msg = 'target="_blank">(.*?)</a>'
            html_url = '<a href="(.*?)" target="_blank">'
            html_hot = '<span>(.*?)</span>'
            url_weibo= 'https://s.weibo.com'
            all_msg = re.findall(html_msg,html)
            # all_msg = []
            all_url = re.findall(html_url,html)
            all_hot = re.findall(html_hot,html)
            #删除all_hot和all_msg中的' '（脏数据）
            dirty_data = all_hot.count(' ')
            for i in range(len(all_hot)-dirty_data):
                if all_hot[i] == ' ':
                    del all_hot[i]
            #cookie24小时过期，当过期时，all_msg会返回一个空列表，会进行异常处理
            try:
                del all_msg[-1]
                del all_msg[-1]
            except IndexError as e:
                eorr_w =IndexError('list assignment index out of range')
                #不能直接将报错信息in e，e的类型是IndexError ，不是可迭代对象
                if type(e) == type(eorr_w):
                    self.conf.set('XL', 'update_time',(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
                    with open('./config.ini', mode='w', encoding='utf-8') as f:
                        self.conf.write(f)
                    return print(f'cookie到期了,请手动添加cookie，这是python提示{e}')
                elif type(e) != type(eorr_w):
                    print(f'出错了！原因是{e}')
            else:
                for i in range(len(all_hot)):
                    if '&nbsp;&nbsp;|&nbsp;&nbsp;' in  all_hot[i]:
                        all_hot[i]=all_hot[i].replace('&nbsp;&nbsp;|&nbsp;&nbsp;',',')
                li_msg = []
                with open('./weibo_msg.csv',mode='a',encoding='utf-8') as f:
                    for i in range(len(all_msg)):
                        if i == 0:
                            li_msg.append(f'\n时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) }'+'置顶新闻：' + all_msg[i]+',   ' )
                        else:
                            li_msg.append(all_msg[i]  + ',   ')
                            if "热度" in all_hot[i-1]:
                                li_msg.append(all_hot[i - 1] + ',   ')
                            else:
                                li_msg.append('热度：' + all_hot[i - 1] + ',   ')
                        li_msg.append(url_weibo + all_url[i] +'\n')
                    f.writelines(li_msg)
        print(f'下载成功,cookie过期时间为{self.update_time}')

def test():
    user_agen,cookie='Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400', 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894'
    url = 'https://s.weibo.com/realtime?q=%E8%8B%8F%E4%BF%84&rd=realtime&tw=realtime&Refer=weibo_realtime'
    a= requests.get(url,headers={'user-agent': user_agen, 'cookie': cookie})
    print(a.text)
if __name__ == '__main__':
    # # while 1:
    # #     if time.strftime("%Y-%m-%d %H:%M:%S") == '2022-02-19 16:59:55':
    # weibo =Wb()
    # weibo.wb()
    # # #         break
    # # print(type(time.strftime("%Y-%m-%d %H:%M:%S")))
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # test()
    # str = 'cupboard,junior,laptop,wool,battle,search,later,odor,certain,tobacco,matter,deposit'
    # str1= 'reward,heavy,window,pitch,addict,limit,clinic,know,exchange,come,bulk,breeze'
    # print(str1.replace(',',' '))
    # html = [['haha','123','http'],['1','jgdh gjsadfgjsdgf','httpxzjkf  zjkf ']]
    # print(max([len(html[0][0]),len(html[1][0])]))
    # for i in range(len(html)):
    #     html[i][0]=html[i][0]+(' '*(4-len(html[i][0])))
    # print(html)
    # print([len(html[0][0]), len(html[1][0])])
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))
    print(date.today()+datetime.timedelta(days=1))
    print(datetime.date.today()+datetime.timedelta(weeks=1))
    # from difflib import Differ
    # str1 = 'SINAGLOBAL=6629531056919.831.1644810640894; _s_tentry=-; Apache=936529738727.5939.1646701480611; ULV=1646701481368:3:1:1:936529738727.5939.1646701480611:1645238512100; WBtopGlobal_register_version=2022030913; SSOLoginState=1647931095; UOR=passport.weibo.com,s.weibo.com,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Iy_mdRCeoizCmPoe5kyFA5JpX5KMhUgL.FozcSK.4Shn71h-2dJLoIpqLxK-L1-zLB-BLxK-L1KeLBKHkSGWX; ALF=1679646990; SCF=AhsQ7CF1SN90-_C3PRos7K1FuOe2I--rUW1Nl3RKQ4FgVZr_Ux-XZE3zWpRDdoSUNUA3UGT42DGlma1ZkP_SSIA.; SUB=_2A25POF3fDeRhGeRI7lsY9CbMwzmIHXVsTMgXrDV8PUNbmtB-LUnbkW9NUrAJ15l3VJ5gjS1TbveZ3gMdjKtMi2Qp; WBStorage=f4f1148c|undefined'
    # str2=  'SINAGLOBAL=6629531056919.831.1644810640894; _s_tentry=-; Apache=936529738727.5939.1646701480611; ULV=1646701481368:3:1:1:936529738727.5939.1646701480611:1645238512100; WBtopGlobal_register_version=2022030913; SSOLoginState=1647931095; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Iy_mdRCeoizCmPoe5kyFA5JpX5KMhUgL.FozcSK.4Shn71h-2dJLoIpqLxK-L1-zLB-BLxK-L1KeLBKHkSGWX; ALF=1679560272; SCF=AhsQ7CF1SN90-_C3PRos7K1FuOe2I--rUW1Nl3RKQ4FgxYhLNvMGhJ6RhKnCV6Tt7qE_6kIYp6Ez7a2gosJ0r4M.; SUB=_2A25PPqqBDeRhGeRI7lsY9CbMwzmIHXVsTZtJrDV8PUNbmtANLXThkW9NUrAJ1yluHDuq04QyZ634zJ0ECAIM54aO; UOR=passport.weibo.com,s.weibo.com,login.sina.com.cn; WBStorage=f4f1148c|undefined'
    # d = Differ()
    # diff = d.compare(str1,str2)
    # print('\n'.join(list(diff)))