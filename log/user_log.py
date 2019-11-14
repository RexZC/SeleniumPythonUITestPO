#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'ZengCheng'

import logging
import os
import datetime


class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        # 设置级别
        # self.logger.setLevel(logging.DEBUG)

        # 控制台输出日志
        # consle = logging.StreamHandler()
        # self.logger.addHandler(consle)

        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, 'logs')
        log_file = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
        log_name = os.path.join(log_dir, log_file)

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name)
        self.logger.addHandler(self.file_handle)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '%(asctime)s %(filename)s----> %(funcName)s %(levelno)s: %(levelname)s ---->%(message)s')
        self.file_handle.setFormatter(formatter)

    def get_log(self):
        return self.logger

    # 可以用装饰器，调用get_log后调用close_handle
    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)


if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.info('12343')
    user.close_handle()
