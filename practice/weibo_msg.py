"""
清华镜像源地址：
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/win-64/"""
import datetime
import requests,re,time
class Wb:
    def __init__(self,user_agen,cookie):
        self.user_agen,self.cookie=user_agen,cookie
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
            all_url = re.findall(html_url,html)
            all_hot = re.findall(html_hot,html)
            #删除all_hot和all_msg中的' '（脏数据）
            dirty_data = all_hot.count(' ')
            for i in range(len(all_hot)-dirty_data):
                if all_hot[i] == ' ':
                    del all_hot[i]
            del all_msg[-1]
            del all_msg[-1]
            for i in range(len(all_hot)):
                if '&nbsp;&nbsp;|&nbsp;&nbsp;' in  all_hot[i]:
                    all_hot[i]=all_hot[i].replace('&nbsp;&nbsp;|&nbsp;&nbsp;',',')
            with open('./weibo_msg.csv',mode='a',encoding='utf-8') as f:
                for i in range(len(all_msg)):
                    li_msg = []
                    if i == 0:
                        li_msg.append(f'时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) }\n'+'置顶新闻：' + all_msg[i]+',   ' )
                    else:
                        li_msg.append(all_msg[i]  + ',   ')
                        if "热度" in all_hot[i-1]:
                            li_msg.append(all_hot[i - 1] + ',   ')
                        else:
                            li_msg.append('热度：' + all_hot[i - 1] + ',   ')
                    li_msg.append(url_weibo + all_url[i] +'\n')
                    f.writelines(li_msg)
        print('下载成功')

def test():
    user_agen,cookie='Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400', 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894'
    url = 'https://s.weibo.com/realtime?q=%E8%8B%8F%E4%BF%84&rd=realtime&tw=realtime&Refer=weibo_realtime'
    a= requests.get(url,headers={'user-agent': user_agen, 'cookie': cookie})
    print(a.text)
if __name__ == '__main__':
    # # while 1:
    # #     if time.strftime("%Y-%m-%d %H:%M:%S") == '2022-02-19 16:59:55':
    weibo = Wb('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400', 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894')
    weibo.wb()
    # #         break
    # # print(type(time.strftime("%Y-%m-%d %H:%M:%S")))
    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    # test()
