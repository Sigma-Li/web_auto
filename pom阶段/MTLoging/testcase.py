import unittest
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from pom阶段.MTLoging.page import log_in
class casess(unittest.TestCase):
    def setUp(self):
        pass
    def test_click(self):
        driver = webdriver.Edge()
        driver.implicitly_wait(5)
        code1 = input('输入对话码：')
        name1 = input('输入用户名：')
        ldx = log_in(driver)
        ldx.page(code1, name1)


