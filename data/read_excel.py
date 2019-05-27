import xlrd

class ExcelUtil:

    def __init__(self):
        self.filepath='C:/Users/linda.li2/Desktop/millenniumhotels/data/email&password.xlsx'
    def open_excel(self,filepath):
        try:
            data=xlrd.open_workbook(filepath)
            return data
        except Exception as e:
            raise e

    def readExcel(self,filepath, SheetName):
        data = self.open_excel(filepath)
        table = data.sheet_by_name(SheetName)
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
