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
if __name__ == '__main__':
    # sql='select * from user ;'
    # a = select_change().select_db(sql=sql, host='localhost', username='root', pwd='', database='test')
    # print(a,type(a),len(a))
    # if "ceshi2" in a:
    #     print(11)
    # elif "ceshi2" not in a:
    #     print(222)
    # username,password,sex,age,phone=1,2,3,4,5
    # sql1= f"INSERT into user (username,password,sex,age,phone) VALUES ({username},{password},{sex},{age},{phone});"
    # select_change().change(sql=sql1, host='localhost', username='root', pwd='', database='test')
    import re
    str = '122811865291'
    print(re.compile(r"1[356789]\d{9}").findall(str))


