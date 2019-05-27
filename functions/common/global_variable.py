from functions.common.ExcelUtil_tool import ExcelUtil


# env = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet2')
env = ExcelUtil.readExcel('C:\\MLP\\Automation\\Project\data\\acc&env_info.xlsx','Sheet2')
# login_data = LOGIN_DATA = ExcelUtil.readExcel('../data/acc&env_info.xlsx','Sheet1')
logindata = ExcelUtil.readExcel('C:\\MLP\\Automation\\Project\data\\acc&env_info.xlsx','Sheet1')

class GlobalVariable(object):
    def __init__(self):
        self.evn_rownb = 2   #Row number is from 2~5
        # open UAT3 on chrome browser('0'-Live, '1'-UAT, '2'-UAT2, '3'-UAT3)
        self.ENV = env[self.evn_rownb-2]['envrionment']
        self.ENV_LINK = env[self.evn_rownb-2]['link']

