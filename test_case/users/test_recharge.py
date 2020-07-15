import os
import pytest

from tools import data
from tools.api import request_tool
import pytest
from tools.data import excel_tool
data = excel_tool.get_test_case("test_case/users/充值用例.xlsx")
@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])

def test_recharge(pub_data,account_name,money,expect):
    pub_data["account_name"] = account_name
    pub_data["money"] = money
    headers = {"token": pub_data["token"]}
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类
    #title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/acc/recharge"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": ${money}
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method, url=uri, pub_data=pub_data, status_code=status_code, headers=headers, expect=expect, feature=feature, story=story, json_data=json_data)
