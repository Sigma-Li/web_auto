# 利用ddt数据驱动可以实现单元测试文件中代代码的功能。

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack


@ddt
class Tese_case(unittest.TestCase):
    def setUp(self):
        self.drive = webdriver.Edge()
        self.drive.get('http://www.baidu.com')
        print('初始化')
    def tearDown(self):
            print('释放')

    @unittest.skip('暂时不执行')
    @data('sigma','Mr rong','青海省')
    def test_1(self,name):                #一个参数 *********************************
        print(name)
        self.drive.find_element(By.ID,'kw').send_keys(name)
        self.drive.find_element(By.ID,'su').click()
        time.sleep(5)

    def test_2(self):
        # drive = webdriver.Edge()
        # var1=drive.get('http://www.baidu.com')
        # var1 = drive.find_element(By.ID, 'kw').send_keys('Mr rong')
        # var1 = drive.find_element(By.ID, 'su').click()
        self.drive.find_element(By.ID,'kw').send_keys('大学英语')
        time.sleep(5)

'''   @data(('Sigma',26,'male'),('Tom',25,'famle'))   # data用于设定参数
    @unpack          #解析数据
    def test_3(self,name,age,sex):                     #多个参数，用unpack
        print(name)
        print(age)
        print(sex)'''

if __name__=='__main__':
    unittest.main()

