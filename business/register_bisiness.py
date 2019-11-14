#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from handle.register_handle import RegisterHandle
from selenium import webdriver
from time import sleep


class RegisterBusiness(object):
    def __init__(self, driver):
        self.rh = RegisterHandle(driver)

    # 正常注册
    def common_register(self, register_email, nickname, password, captcha):
        self.rh.send_register_email(register_email)
        self.rh.send_register_nickname(nickname)
        self.rh.send_register_password(password)
        self.rh.send_register_captcha(captcha)
        self.rh.click_register_btn()

    # 判断是否注册成功
    def success_or_fail(self):
        if self.rh.register_btn_exist() is None:
            return True
        else:
            return False

    def register_function(self, email, username, password, code, assetCode, assertText):
        self.common_register(email, username, password, code)
        if self.rh.get_user_text(assetCode, assertText) is not None:
            return True
        else:
            return False

    # 邮箱错误
    def register_email_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_email_error') is not None:
            print("注册邮箱输入错误")
            return True
        else:
            return False

    # 用户昵称错误
    def register_nickname_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_nickname_error') is not None:
            print("用户昵称错误")
            return True
        else:
            return False

    # 用户密码错误
    def register_password_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('register_password_error') is not None:
            print("用户密码错误")
            return True
        else:
            return False

    # 验证码错误
    def captcha_code_error(self, register_email, nickname, password, captcha):
        self.common_register(register_email, nickname, password, captcha)
        if self.rh.get_user_text('captcha_code_error') is not None:
            print("验证码错误")
            return True
        else:
            return False


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rb = RegisterBusiness(driver)
    # rb.captcha_code_error('1243589@163.com', 'pass123', 'test@123', 'sds')
    rb.register_email_error('23', 'test01', 'test01abc', 'abc4')
    sleep(3)
    driver.close()
    driver.quit()
