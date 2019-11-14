#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser


class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        self.cf = configparser.ConfigParser()
        if file_name is None:
            self.file_name = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/config/LocalElement.ini'
        else:
            self.file_name = file_name
        self.cf.read(self.file_name)
        if node is None:
            self.node = 'RegisterElement'
        else:
            self.node = node

    # 获取value
    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_init = ReadIni()
    print(read_init.get_value('pic'))
