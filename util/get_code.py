#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from selenium import webdriver
import time


class GetCode(object):
    def __init__(self, driver):
        self.driver = driver

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']
        top = code_element.location['y']
        right = left + code_element.size['width']
        bottom = top + code_element.size['height']
        im = Image.open(file_name)
        img = im.crop((2 * left, 2 * top, 2 * right, 2 * bottom))  # mac系统上要*2，windows不用
        img.save(file_name)
        time.sleep(2)


    # 解析图片获取验证码
    def code_online(self, file_name):
        # self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/1274-2", "109836", "e622838346714a869fa3deaaee8850b1")
        r.addFilePara("imgFile", file_name)
        res = r.post()
        print(res)
        text = res.json()['showapi_res_body']['texts']
        return text

if __name__ == '__main__':
    register_url = r'http://www.5itest.cn/register'
    code_file_name = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/pic/code_pic.png'
    driver = webdriver.Chrome()
    driver.get(register_url)
    driver.maximize_window()
    get_code_text = GetCode(driver)
    text = get_code_text.code_online(code_file_name)
    print(text)
    driver.find_element_by_id('captcha_code').send_keys(text)
    time.sleep(4)
    driver.quit()