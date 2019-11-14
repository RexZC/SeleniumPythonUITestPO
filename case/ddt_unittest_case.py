#coding=utf-8

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import ddt
import unittest
from business.register_bisiness import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
from util.excel_util import ExcilUtil

ex = ExcilUtil()
data = ex.get_data()


@ddt.ddt
class DdtTest(unittest.TestCase):
    def setUp(self):
        self.register_url = r'http://www.5itest.cn/register'
        self.driver = webdriver.Chrome()
        self.driver.get(self.register_url)
        self.driver.maximize_window()
        self.rb = RegisterBusiness(self.driver)

        # 每个case执行之后的后置

    def tearDown(self):
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                case_name = self._testMethodName
                # error_path = os.path.join(os.getcwd() + '/..' + '/report' + case_name + '.png')
                error_path = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/report/' + case_name + '.png'
                self.driver.save_screenshot(error_path)
        self.driver.close()

    # 邮箱，用户名，密码，验证码，错误信息定位元素，错误提示信息
    # @ddt.data(
    #     ['12.com', 'zengcheng', '111111', 'code', 'register_email_error', '请输入有效的电子邮件'],
    #     ['@qq.com', 'zengcheng', '111111', 'code', 'register_email_error', '请输入有效的电子邮件'],
    #     ['zcadwef@qq.com', 'zengcheng', '111111', 'code', 'register_email_error', '请输入有效的电子邮件']
    # )
    # @ddt.unpack
    # def test_register_case(self, data):
    #     email, username, password, code, assetCode, assertText = data
    #     email_error = self.rb.register_function(email, username, password, code, assetCode, assertText)
    #     self.assertTrue(email_error, '测试失败')

    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assetCode, assertText = data
        email_error = self.rb.register_function(email, username, password, code, assetCode, assertText)
        self.assertTrue(email_error, '测试失败')

if __name__ == '__main__':
    unittest.main()
