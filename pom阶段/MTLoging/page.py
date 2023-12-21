'''
启动浏览器
登录
查看各个按钮功能
'''
import time
import unittest
from pom阶段.MTLoging import basic
from pom阶段.MTLoging.basic import Steady
from selenium import webdriver
from selenium.webdriver.common.by import By
class log_in(Steady):

    # 核心元素
    website='https://translator.microsoft.com/'

    code=(By.NAME,'Conversation code:')
    name=(By.NAME,'Username:')
    join=(By.CSS_SELECTOR,'button[class="submit btn btn-secondary"]')
    # 对话页面内
    setting=(By.CSS_SELECTOR,'button[aria-label="Settings"] img:nth-child(1)')
    auto_speak=(By.ID,'autoTtsSwitch')
    set_close=(By.ID,'sidebarFocusable')
    participant=(By.CSS_SELECTOR,'button div img:nth-child(1)')
    log=(By.XPATH,'/html/body/div[1]/header/nav/div/div/ul/li[5]/button')
    no=(By.CSS_SELECTOR,'div[class="modal-footer"] button:nth-child(2)')
    exit=(By.CSS_SELECTOR,'li[class="navbar-item exitConversation"]')
    leave=(By.CSS_SELECTOR,'div [class="modalButton btn btn-primary"]')


    def page(self,code1,name1):

        self.start()
        self.inputt(self.code,code1)
        self.inputt(self.name,name1)
        self.click(self.join)
        time.sleep(5)
        self.click(self.setting)

        time.sleep(2)
        self.click(self.auto_speak)
        time.sleep(2)
        self.click(self.set_close)
        time.sleep(2)
        self.click(self.participant)
        time.sleep(2)
        self.click(self.log)
        time.sleep(2)
        self.click(self.no)
        time.sleep(2)
        self.click(self.exit)
        time.sleep(2)
        self.click(self.leave)


# if __name__=='__main__':
#     driver=webdriver.Edge()
#     driver.implicitly_wait(5)
#     code1 = input('输入对话码：')
#     name1 = input('输入用户名：')
#     ldx=log_in(driver)
#     ldx.page(code1,name1)



