import allure
class MyAllure():
    """attach方法：https://www.cnblogs.com/poloyy/p/12716659.html"""
    def __init__(self, case_id, case_title, case_severity, request_obj):
        self.__case_id = case_id
        self.__case_title = case_title
        self.__case_severity = case_severity
        self.__request_obj = request_obj

    def add_data(self):
        allure_case_title = f'case{self.__case_id}_{self.__case_title}'
        allure.dynamic.title(allure_case_title)  # 用例标题
        allure.dynamic.tag(allure_case_title)  # 用例id
        #allure对用例的等级划分成五个等级
        #   blocker　 阻塞缺陷（功能未实现，无法下一步）
        #   critical　　严重缺陷（功能点缺失）
        #   normal　　 一般缺陷（边界情况，格式错误）
        #   minor　 次要缺陷（界面错误与ui需求不符）
        #   trivial　　 轻微缺陷（必须项无提示，或者提示不规范）
        allure.dynamic.severity(self.__case_severity)  # 用例严重级别
        allure.attach(body=str(self.__request_obj.request.url), name="请求地址",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.request.method), name="请求方法",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.request.headers), name="请求头",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.request.body), name="请求body",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.status_code), name="响应状态码",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.headers), name="响应头", attachment_type=allure.attachment_type.TEXT)
        allure.attach(body=str(self.__request_obj.text), name="响应body", attachment_type=allure.attachment_type.TEXT)

