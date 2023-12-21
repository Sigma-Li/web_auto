import time
import unittest
from selenium import webdriver
from pom阶段.POMWEB.basicclass import No1Basic
from pom阶段.POMWEB.pageobject.jump2 import JumpPage
from pom阶段.POMWEB.pageobject.Open1 import StartUp


class webvtes(unittest.TestCase):

    def test_search(self):
        driver = webdriver.Edge()

        search='肖战'
        var = StartUp(driver)
        var.start(search)
        time.sleep(5)
        #多页面连接
        var2 = JumpPage(driver)
        var2.jump()


if __name__=='__main__':
    unittest.main()

