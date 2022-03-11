import json,flask,re
import pymysql
class select_change():
    def select_db(self,sql,host,username,pwd,database,port=3306):
        self.conn = pymysql.connect(host=host, user=username, password=pwd, port=port, database=database,charset='utf8',autocommit=True)
        self.cur = self.conn.cursor(pymysql.cursors.SSDictCursor)#游标中不加括号中的内容，返回元祖，加了返回列表镶嵌字典的格式
        self.cur.execute(sql)
        rest = self.cur.fetchall()#查询结果  fetchmany(size)   fetchone
        self.cur.close()
        self.conn.close()#关闭连接和游标
        return rest

    def change(self,sql,host,username,pwd,database,port=3306):
        self.conn = pymysql.connect(host=host, user=username, password=pwd, port=port, database=database,charset='utf8',autocommit=True)
        self.cur = self.conn.cursor()
        rest = self.cur.execute(sql)
        self.conn.commit()#提交
        self.conn.close()
        self.cur.close()
        return rest
def dict_li(li_d,str):
    li = []
    for i in range(0,len(li_d)):
        li.append(li_d[i][str])
    return li
app = flask.Flask(__name__)
@app.route('/login',methods=['POST'])
def login():
    username = flask.request.values.get("username")
    password = flask.request.values.get("password")
    if username and password :#两个为真
        sql = f"select * from user where username='{username}' and password = '{password}';"
        result=select_change().select_db(sql=sql, host='localhost', username='root', pwd='', database='test')
        if result:#返回有结果
            return json.dumps({"code":200,"msg":"login success",'data':result})
        else:
            return json.dumps({"code":1000,"msg":"Wrong account or password input","user":f"{username}---{password}"})
    else:
        return json.dumps({"code": 2000, "msg": "Please enter the correct account and password"})
@app.route('/reg',methods=['POST'])
def reg():
    username= flask.request.values.get("username")
    password = flask.request.values.get("password")
    sex = flask.request.values.get("sex")
    age= flask.request.values.get("age")
    phone = flask.request.values.get("phone")
    if username and password  and age and phone:
        sql = f"select * from user;"
        result = select_change().select_db(sql=sql, host='localhost', username='root', pwd='', database='test')
        li_user,li_phone = dict_li(result,'username'),dict_li(result,'phone')
        if username in li_user :#姓名不能重复
            return json.dumps({"code":1000, "msg": "The user name already exists !"})
        elif len(username)>10:
            return json.dumps({"code":1001, "msg": "Name cannot exceed 10 characters !"})
        elif len(password) < 6:
            return json.dumps({"code":2000,"msg": "Password must be greater than six digits !"})
        elif password.isdigit():
            return json.dumps({"code":2001, "msg": "The password cannot be a pure number !"})
        elif password.isalpha():
            return json.dumps({"code":2002, "msg": "The password cannot be a pure letter !"})
        elif sex not in ['男','女']:
            return json.dumps({"code":3000, "msg": "Please enter the correct gender !"})
        elif not age.isdigit() or int(age) <= 0:
            return json.dumps({"code":4000, "msg": "Please enter the correct age !"})
        elif len(phone) != 11 or not phone.isdigit() or len(re.compile(r"1[356789]\d{9}").findall(phone))== 0 or phone in li_phone:#验证手机号码
            return json.dumps({"code":5000, "msg": "Mobile number already exists or is in the wrong format !"})
        else:
            sql1 = f"INSERT into user (username,password,sex,age,phone) VALUES ('{username}','{password}','{sex}',{age},{phone});"
            select_change().change(sql=sql1, host='localhost', username='root', pwd='', database='test')
            return json.dumps({"code": 200, "msg": "Register  Success !"})
    else:
        return  json.dumps({"code":6000, "msg":"Parameter cannot be empty !"})

if __name__ == '__main__':
    app.run(debug=True,host='10.0.0.75')