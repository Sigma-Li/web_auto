'''页面对象类'''


from pom阶段.POM.basic.Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
CODE=input('Please input conversation code:')
username1=input('Please input youe name:')
# language=input('Choose your language:')
class loging(BasePage):
    #核心元素
    url='https://translator.microsoft.com/'
    conversation_code=(By.NAME,'Conversation code:')
    user=(By.NAME,'Username:')
    # 语言的选择暂时能力有限无法实现  11/29/2023
    '''Languages_button=(By.NAME,'Language')'''
    logging_button=(By.CSS_SELECTOR,'form button')
    time=10

    #核心业务流
    def logging(self,mma,code):
        # self.get_url(self.url) ==
        self.get_url()
        self.input1(self.user,mma)
        self.input1(self.conversation_code,code)
        self.click(self.logging_button)
        # lset=list()
        self.wait(self.time)

# 调试代码
'''if __name__=="__main__":
    #     unittest.main()
    driver=webdriver.Edge()
    mma=username1
    code=CODE
    nu=loging(driver)
    nu.logging(mma,code)'''


