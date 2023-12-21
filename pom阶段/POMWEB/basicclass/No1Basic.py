'''
尝试创建:
启动浏览器
输入
点击
'''
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class webSite:
    def __init__(self,driver):
        self.driver=driver
    # 启动浏览器
    # driver = webdriver.Edge()
    def startup(self):
        self.driver.get(self.url)
    # 元素定位
    def locate(self,way):
        return self.driver.find_element(*way)

    def send1(self,way,text):
        self.locate(way).send_keys(text)

    def click1(self,way):
        self.locate(way).click()
    def wait(self):
        self.driver.implicitly_wait(5)


