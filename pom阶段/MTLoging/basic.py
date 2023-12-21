import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
class Steady():
    def __init__(self,driver):
        self.driver=driver

    # 启动浏览器方法
    def start(self):
        self.driver.get(self.website)
    # 元素定位
    def location(self,way):
        return self.driver.find_element(*way)

    def inputt(self,way,txt):
        self.location(way).send_keys(txt)

    def click(self,way):
        self.location(way).click()

