
# yml 文件操作
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from ddt import ddt, file_data


@ddt
class auto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        # self.driver.get('https://www.baidu.com/')
        pass

    def tearDown(self):
        pass

    # @file_data('b.yml')
    @file_data('c.yml')
    def test_1(self,**kwargs):
        print(kwargs.get('name'))
        # self.driver.find_element(By.ID,'kw').send_keys(kwargs.get('name'))
        # self.driver.find_element(By.ID,'su').click()

        time.sleep(5)
    @unittest.skip('no')
    @file_data('c.yml')
    def test_2(self,**kwargs):
        self.driver.find_element(By.ID, 'kw').send_keys(kwargs.get('age'))
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(3)

  # '''      print(kwargs.get('name'))
  #       print(kwargs.get('age'))'''


if __name__ =='__main__':
    unittest.main()


