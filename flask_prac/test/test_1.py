from flask import Flask
from flask import render_template
from test.common.sql_database import *
app = Flask(__name__)
@app.route('/index/<string:user>',methods=['get'])
def query(user):
    sql = 'select * from user;'
    a=select_change().select_db(sql=sql,host='localhost',username='root',pwd='',database='test')
    user_li = []
    if user:
        for i in range(len(a)):
            user_li.append(a[i]['username'])
        if user in user_li:
            index = user_li.index(user)
            if a[index]['leader'] == None:
                return f"账号是{user}，密码是{a[index]['password']},无上级用户, 邀请码是{a[index]['code']}"
            else:
                return f"账号是{user}，密码是{a[index]['password']},上级用户是{a[index]['leader']}, 邀请码是{a[index]['code']}"
        else:
            return "账号不存在！"
    else:
        return "输入有误！"


    # return {
    #     'msg':'success',
    #     'data':'reg success'
    # }
    # return render_template('index.html')
if __name__ == '__main__':

    app.run()