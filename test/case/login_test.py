import pytest,requests,allure,os
from test.common.data_li import *
from test.common.myallure import *
class Test_Login():
    li = get_data(r'F:\Users\admin\PycharmProjects\untitled\test\data\login.csv')
    @pytest.mark.parametrize('case_id,case_title,url,name,pwd,expect,case_severity',li)
    def test_login(self,case_id,case_title,url,name,pwd,expect,case_severity,type='app'):
        url = url
        data = {'username': name,'password': pwd,'type': type}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(url=url, data=data, headers=headers)
        MyAllure(case_id=case_id, case_title=case_title,case_severity=case_severity, request_obj=resp).add_data()
        assert expect in resp.text

if __name__ == '__main__':
    # pytest.main([__file__,'--alluredir', './report'])
    # os.system('allure serve F:\Users\admin\PycharmProjects\untitled\test\report')
    pytest.main(["-s",__file__])


