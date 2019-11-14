#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd


class ExcilUtil:
    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            excel_path = '/Users/zengcheng/软件/PycharmProjects/WebUITest-PO/config/case_data.xls'
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        # 行数
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result


if __name__ == '__main__':
    ex = ExcilUtil()
    print(ex.get_data())
