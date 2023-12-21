
'''
基类 逻辑代码部分，主要是生产一系列在页面对象中可以被调用的函数。本身作为一个工具库存在
'''

from selenium import webdriver
from time import sleep

class BasePage:
# driver=webdriver.Edge()
    # 构造函数
    def __init__(self,driver):
        self.driver=driver

    #访问url
# '''    def get_url(self,url):
#         self.driver.get(url) == '''
    def get_url(self):
        self.driver.get(self.url)
    #元素定位
    def element(self,act):
        return self.driver.find_element(*act)      #*act 元组  driver.find_element(locate way,value)

    # 输入
    def input1(self,act,text):
        self.element(act).send_keys(text)
    # 点击
    def click(self,act):
        self.element(act).click()

    # 等待
    def wait(self,timee):
        sleep(timee)

