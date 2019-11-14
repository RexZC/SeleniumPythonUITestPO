#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from page.register_page import RegisterPage
from selenium import webdriver
from time import sleep
from util.get_code import GetCode


class RegisterHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.rp = RegisterPage(self.driver)

    # 输入注册邮箱
    def send_register_email(self, email):
        self.rp.get_register_email().send_keys(email)

    # 输入用户昵称
    def send_register_nickname(self, nickname):
        self.rp.get_register_nickname().send_keys(nickname)

    # 输入注册密码
    def send_register_password(self, password):
        self.rp.get_register_password().send_keys(password)

    # 输入验证码(自动识别验证码)
    # def send_register_captcha(self, file_name):
    #     get_code_text = GetCode(self.driver)
    #     code = get_code_text.code_online(file_name)
    #     self.rp.get_captcha_code().send_keys(code)

    # 输入验证码(手动输入)
    def send_register_captcha(self, code):
        self.rp.get_captcha_code().send_keys(code)

    # 获取错误信息
    def get_user_text(self, error_info, *args):
        text = None
        try:
            if error_info == "register_email_error":
                text = self.rp.get_register_email_error().text
            elif error_info == 'register_nickname_error':
                text = self.rp.get_register_nickname_error().text
            elif error_info == 'register_password_error':
                text = self.rp.get_register_password_error().text
            elif error_info == 'captcha_code_error':
                text = self.rp.get_captcha_code_error().text
            else:
                print("error element not found")
        except:
            text = None
        return text

    # 点击注册按钮
    def click_register_btn(self):
        self.rp.get_register_btn().send_keys()

    # 获取注册按钮元素
    def register_btn_exist(self):
        return self.rp.get_register_btn()


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rh = RegisterHandle(driver)
    rh.send_register_email('jjij@163.com')
    rh.send_register_nickname('MiFan')
    rh.send_register_password('123@123abc')
    rh.send_register_captcha('qwer')
    rh.click_register_btn()
    print(rh.get_user_text('register_password_error'))
    print(rh.get_user_text('captcha_code_error'))
    sleep(5)
    driver.close()
    driver.quit()
