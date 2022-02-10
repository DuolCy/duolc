import requests
def login(url,name,pwd,type='app'):
    url = url
    data = {'username': name ,'password': pwd,'type': type}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        resp = requests.post(url=url, data=data, headers=headers)
        if 'token' in resp.text:
            print('测试通过')
        else:
            print('测试失败')
    except Exception as e:
        print(f'测试报错，原因是------>{e}')
if __name__ == '__main__':
    login('http://46.8.197.234:8975/home/passport/login','173326303@test.com','kupNvHoihOovjnt/b7e4hoI6b56tbClRCmuQvm7Hrx3ZR/YqKCv70KKuswy4wxjweqmgsN74BptdMs38LqaghQ4Jm4rYxZN4J/gU0M7YBMihxh4/hN4KhxhbZkxmn1ZHdL1jIeOqfDRUmHs8ACA2tWHr75povgGPTTnoY077U68=')
