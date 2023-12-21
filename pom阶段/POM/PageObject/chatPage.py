from pom阶段.POM.basic.Base_page import BasePage
from  selenium.webdriver.common.by import By
from selenium import webdriver
'''
打开auto speak: 设置-> 打开
输入内容
发送消息

'''
content=input('Enter text and press the arrow to send a message:')
class chat(BasePage):
    # 核心元素
    url='https://translator.microsoft.com/Conversation'
    set_button=(By.CSS_SELECTOR,'button[aria-label="Settings"]')
    auto_speak=(By.ID,'autoTtsSwitch')
    set_close_button=(By.ID,'sidebarFocusable')
    inputbox = (By.CSS_SELECTOR, 'sendMessageTextBox form-control')
    send_button = (By.CSS_SELECTOR, 'button:nth-last-child(2)')
    def chate(self,cont):
        self.get_url()
        #打开 auto speak
        self.click(self.set_button)
        self.click(self.auto_speak)
        self.click(self.set_close_button)
        # 输入消息
        self.input1(self.inputbox,cont)
        self.click(self.send_button)
'''if __name__=='__main__':
    driver=webdriver.Edge()'''





