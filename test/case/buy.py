import pytest,requests,json
from test.common.myallure import *
from test.common.data_li import *
data_li = get_data(r'F:\Users\admin\PycharmProjects\untitled\test\data\buy.csv')
class  TestBuy():
    def setup(self):
        url = 'http://46.8.197.234:8975/home/passport/login'
        data = {'username': '173326303@test.com',
                'password': 'kupNvHoihOovjnt/b7e4hoI6b56tbClRCmuQvm7Hrx3ZR/YqKCv70KKuswy4wxjweqmgsN74BptdMs38LqaghQ4Jm4rYxZN4J/gU0M7YBMihxh4/hN4KhxhbZkxmn1ZHdL1jIeOqfDRUmHs8ACA2tWHr75povgGPTTnoY077U68=',
                'type': 'app'}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(url=url, data=data, headers=headers)
        resp_data = json.loads(resp.text)
        self.user_token = resp_data['data']['token']
    @pytest.mark.parametrize('case_id,case_title,url,power_id,buy_num,pay_password,expect,case_severity',data_li)
    def test_buy(self,case_id,case_title,url,power_id,buy_num,pay_password,expect,case_severity,type='app',language='zh'):
        url = url
        data = {'user_token':self.user_token,'power_id':power_id,'buy_num':buy_num,'pay_password':pay_password,'type':type,'language':language}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(url=url,data=data,headers=headers)
        MyAllure(case_id=case_id,case_title=case_title,case_severity=case_severity,request_obj=resp).add_data()
        # print(resp.text)
        # if expect in resp.text:
        #     print('111')
        assert expect in resp.text

if __name__ == '__main__':
    pytest.main(['-q',__file__])

    # TestBuy().test_buy('_00买1个云产品','http://46.8.197.234:8975home/ecology/doBuyPower','1','1','d1IIs+6m/p7IaUUQnCitImuNavnN5D8r03SFD2UwhEgkHCFO3nqDxpfzp7QO0/S9pWfN4YuuhFMLtnvqnCMe1VuD3z1AvtYqXm25JP5Ya62LFCcmXKXxRJClIirkn2PQLhZxXR1a7jDaD9mZ2zqE9oO+2fu1ATzAWBpbXMt5+TM=','购买成功','1')1','购