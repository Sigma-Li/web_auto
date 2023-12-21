import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class second(unittest.TestCase):
    def setUp(self):

        print('初始化')
    def tearDown(self):
        print('释放')
    def test_1(self):
        var1=webdriver.Edge()
        wb=var1.get('http://www.baidu.com')
        wb=var1.find_element(By.ID,'kw').send_keys('sigma')
        wb=var1.find_element(By.ID,'su').click()
        time.sleep(3)
        wb=var1.find_element(By.ID,'kw').clear()
        wb=var1.find_element(By.ID,'kw').send_keys('荣蓉荣')
        time.sleep(5)
    def test_2(self):
        var1=webdriver.Edge()
        wb=var1.get('http://www.baidu.com')
        wb=var1.find_element(By.ID,'kw').send_keys('容文浩 大庆')
        wb=var1.find_element(By.ID,'su').click()
        time.sleep(5)


if __name__=='__main__':
    unittest.main()




