# import random
#
# import requests
#
# from config.conf import API_URL
#
#
# def test_recharge(db):
#     #执行查询sql语句
#     res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS = 0 AND account_name IS NOT NULL;")
#     #从查询结果中随机获取一条，去第一个数据
#     account_name = random.choice(res)[0]
#     #准备请求数据
#     data = {
#   "accountName": account_name,
#   "changeMoney": 10000
# }
#     #使用requests框架发送http请求
#     r = requests.post(API_URL + "/acc/recharge",json=data)
#     print(r.text)
#     pass
#
import random

import allure

from config.conf import API_URL
import requests

@allure.feature("用户管理") # 一级分类
@allure.story("充值提现模块") # 二级分类
@allure.title("充值成功") # 修改用例标题
def test_acc_recharge(db):
    ##执行查询sql语句
    with allure.step("第一步、执行SQL语句"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE STATUS = 0 AND account_name IS NOT NULL;")
    # 从查询结果中随机获取一条，去第一个数据
    with allure.step("第二步、从查询结果中随机获取一条，取第一个数据"):
        account_Name= random.choice(res)[0]
    #准备请求数据
    with allure.step("第三步、准备请求数据"):
        data={
  "accountName": account_Name,
  "changeMoney": 99999
    }
    # 使用requests框架发送http请求
    with allure.step("第四步、发送请求"):
        r=requests.post(API_URL +"/acc/recharge",json=data )
    with allure.step("第五步、获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        """
        第一个参数：附件内容
        第一个参数：附件名称
        第三个参数：附件类型
        """
        allure.attach(r.request.url, "请求url", allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers), "请求头", allure.attachment_type.TEXT)
        allure.attach(r.request.body, "请正文", allure.attachment_type.TEXT)
    with allure.step("第六步、获取响应内容"):
        allure.attach(str(r.status_code), "响应状态码", allure.attachment_type.TEXT)
        allure.attach(str(r.headers), "响应头", allure.attachment_type.TEXT)
        allure.attach(r.text, "响应正文", allure.attachment_type.TEXT)
    with allure.step("第七步、断言"):
        allure.attach(r.text, "实际结果", allure.attachment_type.TEXT)
        allure.attach("充值成功", "预期结果", allure.attachment_type.TEXT)
        assert "充值成功" in r.text
