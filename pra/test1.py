import requests
import json
url = 'http://46.8.197.234:8975/home/passport/login'
data = {'username':'173326303@test.com',
        'password':'kupNvHoihOovjnt/b7e4hoI6b56tbClRCmuQvm7Hrx3ZR/YqKCv70KKuswy4wxjweqmgsN74BptdMs38LqaghQ4Jm4rYxZN4J/gU0M7YBMihxh4/hN4KhxhbZkxmn1ZHdL1jIeOqfDRUmHs8ACA2tWHr75povgGPTTnoY077U68=',
        'type':'app'}
headers = {"Content-Type":"application/x-www-form-urlencoded"}
resp = requests.post(url=url,data=data,headers=headers)

if __name__ == '__main__':
        # print(resp.text, resp.status_code, resp.headers, sep='\n')
        data = resp.text
        print(type(data))
        # str = json.dumps(data)#转为json格式
        str = json.loads(data)#转为python格式
        print(type(str),str['data']['token'])

