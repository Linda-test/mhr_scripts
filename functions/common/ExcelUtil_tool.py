""" ================================================================================================================
Description: This module defines the business functions about retail booking flow.Use these function and update if
necessary.
Last Update Date + Update by Whom: 5/7/2019 by TinaZ
====================================================================================================================="""

import xlrd

class ExcelUtil():
    def readExcel(fileName, SheetName="Sheet1"):
        data_exl = xlrd.open_workbook(fileName)
        table = data_exl.sheet_by_name(SheetName)
        nrows = table.nrows
        ncols = table.ncols
        if nrows > 1:
            keys = table.row_values(0)
            listApiData = []
            for col in range(1, nrows):
                values = table.row_values(col)
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格未填写数据")
            return None


# d = ExcelUtil()
# ExcelUtil.readExcel('../data/email&password.xlsx','Sheet1')