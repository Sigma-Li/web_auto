'''
实现浏览器打开，输入后跳转到新页面
'''
import time

from pom阶段.POMWEB.basicclass.No1Basic import webSite
from selenium.webdriver.common.by import By
from selenium import webdriver
# search_content=input('搜索内容：')
class StartUp(webSite):
    #核心元素   网址 输入框内容 点击搜索
    url='https://www.baidu.com/index.htm'
    inputbox=(By.ID,'kw')
    search_button=(By.ID,'su')


    # 核心业务
    def start(self,content):
        self.startup()
        self.send1(self.inputbox,content)
        self.click1(self.search_button)
        self.wait()

# if __name__=='__main__':
#     driver=webdriver.Edge()
#     search1='肖战'
#     ldx=StartUp(driver)
#     ldx.start(search1)
#     time.sleep(10)



