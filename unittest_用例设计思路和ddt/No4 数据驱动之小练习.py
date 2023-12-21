import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack

def get_data():
    list=[]
    dat=open('data4','r',encoding='utf-8')
    content=dat.readlines()
    for elements in content:
        list.append(elements.strip('\n').split(' '))


    return list
get_data()
@ddt
class Details(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Edge()
        print('初始化')
    def tearDown(self):
        print('释放')

    @data(*get_data())

    @unpack

    def test_1(self,x,y):
        self.driver.get(x)
        self.driver.find_element(By.ID,'kw').send_keys(y)
        self.driver.find_element(By.ID,'su').click()

        print(x)
        print(y)
if __name__=='__main__':
    unittest.main()



