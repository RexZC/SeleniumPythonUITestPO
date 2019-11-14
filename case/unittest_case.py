#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from business.register_bisiness import RegisterBusiness
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
from log.user_log import UserLog


class RegisterCase(unittest.TestCase):
    # 所有case执行之前的前置
    @classmethod
    def setUpClass(cls):
        cls.code_file_name = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/pic/code_pic.png'
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    # 所有case执行之后的后置
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    # 每个case执行之前的前置
    def setUp(self):
        self.register_url = r'http://www.5itest.cn/register'
        self.driver = webdriver.Chrome()
        self.driver.get(self.register_url)
        self.driver.maximize_window()
        self.logger.info('this is Chrome')

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

    # 注册邮箱错误，但用例执行成功
    def test_register_email_error(self):
        register_email_error = self.rb.register_email_error('23', 'test01', 'test01abc', self.code_file_name)
        # if register_email_error is True:
        #     print("账号注册失败，该用例执行成功01")
        # else:
        #     print("账号注册成功，该用例执行失败01")
        self.assertTrue(register_email_error, '账号注册成功，该用例执行失败01')
        print("账号注册失败，该用例执行成功01")
        time.sleep(2)

    # 用户名错误，但用例执行成功
    def test_register_nickname_error(self):
        register_nickname_error = self.rb.register_nickname_error('1243589@163.com', 'p', 'test@123',
                                                                  self.code_file_name)
        # if captcha_code_error is True:
        #     print("账号注册失败，该用例执行成功02")
        # else:
        #     print("账号注册成功，该用例执行失败02")
        self.assertTrue(register_nickname_error, '账号注册成功，该用例执行失败02')
        print("账号注册失败，该用例执行成功02")
        time.sleep(2)

    # 密码错误，但用例执行成功
    def test_register_password_error(self):
        register_password_error = self.rb.register_password_error('1243589@163.com', 'pass123', '111111',
                                                                  self.code_file_name)
        # if register_password_error is True:
        #     print("账号注册失败，该用例执行成功03")
        # else:
        #     print("账号注册成功，该用例执行失败03")
        self.assertTrue(register_password_error, '账号注册成功，该用例执行失败03')
        print("账号注册失败，该用例执行成功03")
        time.sleep(2)


if __name__ == "__main__":
    # unittest.main()
    # report_path = os.path.join(os.getcwd() + '/..' + '/report' + '/first_case.html')
    report_path = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/report/first_case.html'
    suite = unittest.TestSuite()
    suite.addTest(RegisterCase("test_register_email_error"))
    suite.addTest(RegisterCase("test_register_password_error"))

    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='first report', description='第一次测试报告')
        runner.run(suite)
