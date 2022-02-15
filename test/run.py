import subprocess
import pytest,os,shutil
allure_data=r"F:\Users\admin\PycharmProjects\untitled\test\report\allure_data" # allure结果数据存储目录
allure_report=r"F:\Users\admin\PycharmProjects\untitled\test\report\allure_report" #allure 报告数据存储目录
# os.remove(allure_data) #删除文件夹中的内容，文件在使用中时会报错
# os.remove(allure_report)
shutil.rmtree(allure_data)
shutil.rmtree(allure_report)#删除文件夹，文件在使用中时不会报错
os.mkdir(allure_data)
os.mkdir(allure_report)#新建同名文件夹
# 运行
pytest.main([ "-vs", f"--alluredir={allure_data}"])
# 生成报告
# os.system(rf'allure serve {allure_data}')
subprocess.check_call(f"allure generate {allure_data} --clean -o {allure_report}", shell=True, universal_newlines=True)
