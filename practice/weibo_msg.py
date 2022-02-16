import requests,re,time
def WB():
    user_agen,cookie=  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3883.400 QQBrowser/10.8.4559.400', 'SUB=_2AkMVVV66f8NxqwJRmfoUym7ibYt0zQvEieKjCa9hJRMxHRl-yT9jqlQBtRB6PtVwVRQ0PX9Ys2ARwx84m4B3Y5rGQTXx; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5z8ha_.RPknZ3v3zrguDY_; _s_tentry=passport.weibo.com; UOR=passport.weibo.com,s.weibo.com,spr_wbprod_sougou_sgss_weibo_t001; Apache=6629531056919.831.1644810640894; SINAGLOBAL=6629531056919.831.1644810640894; ULV=1644810641010:1:1:1:6629531056919.831.1644810640894'
    url = 'https://s.weibo.com/top/summary?cate=realtimehot/'
    resp = requests.get(url, headers={'user-agent': user_agen, 'cookie': cookie})
    html = resp.text
    html_msg = 'target="_blank">(.*?)</a>'
    html_url = '<a href="(.*?)" target="_blank">'
    html_hot = '<span>(.*?)</span>'
    url_weibo= 'https://s.weibo.com'
    all_msg = re.findall(html_msg,html)
    all_url = re.findall(html_url,html)
    all_hot = re.findall(html_hot,html)
    #删除all_hot中的' '（脏数据）
    dirty_data = all_hot.count(' ')
    for i in range(len(all_hot)-dirty_data):
        if all_hot[i] == ' ':
            del all_hot[i]
    with open('./weibo_msg.csv',mode='a',encoding='utf-8') as f:
        for i in range(51):
            li_msg = []
            if i == 0:
                li_msg.append(f'时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) }\n'+'置顶新闻：' + all_msg[i]+',   ' )
            else:
                li_msg.append(all_msg[i]  + ',   ')
                li_msg.append('热度：'+all_hot[i - 1] + ',   ')
            li_msg.append(url_weibo + all_url[i] +'\n')
            f.writelines(li_msg)
if __name__ == '__main__':
    WB()
