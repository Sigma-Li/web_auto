# 案例1
# 设计一个简单的测试用例 用来打开Microsoft translator Web
# step1 导入相关包
'''import time
import unittest
from selenium import webdriver
# step 2创建类
class demo1(unittest.TestCase):
    # 测试准备 清理释放缓存
    def setUp(self):
        pass
    def tearDown(self):
        pass
    # 设计测试用例
    def test_open(self):
        var1=webdriver.Edge()
        var1.get('https://translator.microsoft.com/')
        time.sleep(3)

if __name__=='__main__':
    unittest.main()'''
import time

# 案例二 设计一个用例验证 加入microsoft translator web 对话

from selenium import webdriver
from  selenium.webdriver.common.by import By
import unittest

class demo2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_inout(self):
        var2=webdriver.Edge()
        var3=var2.get('https://translator.microsoft.com/')
        var3 = var2.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/form/div/div[1]/input').send_keys('eqldp')
        time.sleep(2)
        var3=var2.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/form/div/div[2]/input').send_keys('容文浩')
        time.sleep(2)
        var3=var2.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div[1]/div/div[2]/form/button').click()
        time.sleep(4)




