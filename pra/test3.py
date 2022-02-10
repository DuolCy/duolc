
import pytest,requests,allure,os
li = [('http://46.8.197.234:8975/home/passport/login','173326303@test.com','kupNvHoihOovjnt/b7e4hoI6b56tbClRCmuQvm7Hrx3ZR/YqKCv70KKuswy4wxjweqmgsN74BptdMs38LqaghQ4Jm4rYxZN4J/gU0M7YBMihxh4/hN4KhxhbZkxmn1ZHdL1jIeOqfDRUmHs8ACA2tWHr75povgGPTTnoY077U68=','token')]
report_t = r'F:\Users\admin\PycharmProjects\untitled\test\report\a'
class Test_Login():
        # 1、如果需要以模块维度查找用例，则模块名需要以test开头或者_test结束；
        # 2、类名必须以Test开头：
        # 3、函数名、方法名必须以test开头；
        # 4、在类里面不能有构造方法；
        # 5、断言必须是用 python内置关键字 assert（assert bool类型:bool表达式）；
    def setup(self):
        print("第一个运行")
    def teardown(self):
        print("最后运行")
    # setup_module：在所有的测试用运行之前执行该方法
    # teardown_module：在所有的测试用运行之后执行该方法
    # setup_function：在每个测试用例函数运行之前执行该方法
    # teardown_function：在每个测试用例函数运行之后执行该方法
    # setup_method/setup：每个测试方法运行之前执行
    # teardown_method/teardown：每个测试方法运行之后执行
    # setup_class：所有的测试方法运行之前执行
    # teardown_class：所有的测试方法运行之后执行
    @pytest.mark.parametrize('url,name,pwd,expect',li)
    def test_login(self,url,name,pwd,expect,type='app'):
        url = url
        data = {'username': name,'password': pwd,'type': type}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = requests.post(url=url, data=data, headers=headers)
        assert expect in resp.text
if __name__ == '__main__':
    # pytest.main(["-s", __file__])
    pytest.main(['-s',__file__,f'--alluredir={report_t}'])
    os.system(f'allure serve {report_t}')

    # -s 展示测试用例里面的打印输出日志信息
    # -q：以极简的方式执行；
    # -v：展示详情日志信息
    # -x：出现1条用例执行失败则退出测试
    # --maxfail=n：执行用例时有n条失败时，停止测试
    # -n=数字：以多进程运行当前测试用例,用例足够多