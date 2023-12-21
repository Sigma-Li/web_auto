'''测试用例类'''
import unittest
from selenium import webdriver

from pom阶段.POM.PageObject.chatPage import content,chat
from pom阶段.POM.PageObject.loggingPage import username1, CODE, loging


class Tesecase(unittest.TestCase):
    def test1_logging(self):
        driver = webdriver.Edge()
        mma = username1
        code = CODE
        nu = loging(driver)
        nu.logging(mma, code)
        # 多页面连结。 登录界面，登录进去的聊天界面
'''        cont = content
        sub_page=chat(driver)
        sub_page.chate(cont)'''

    # def test2_chat(self):
    #
    #     self.mma=username1
    #     driver1=webdriver.Edge()
    #     cont=content
    #     num1=chat(driver1)
    #     num1.chate(cont)

if __name__=='__main__':
    unittest.main()