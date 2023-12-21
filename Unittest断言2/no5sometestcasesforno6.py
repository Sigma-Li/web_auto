import time
import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import file_data, ddt, unpack, data


def read_data():
    list1 = []
    dataq = open('datainfo.txt', 'r', encoding='utf-8')
    details = dataq.readlines()
    for elements in details:
        list1.append(elements.strip('\n').split(','))
    return list1


@ddt
class about_testsuite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        pass

    def tearDown(self):
        pass

    def test_4(self):
        print('this is test4')

    def test_2(self):
        self.assertEqual(4, 4, msg='NotEqual!')
        print('Test_2 Pass')

    @ddt
    @file_data('c.yml')
    def test_3(self, **kwargs):
        value1 = kwargs.get('name')
        self.assertIn(value1, 'hufrife', msg='Not contain')
        print('The value you need is contained!')
        print('test_3')

    @data(*read_data())
    @unpack
    def test_1(self, x, y):
        self.driver.get(x)
        self.driver.find_element(By.ID, 'kw').send_keys(y)
        self.driver.find_element(By.ID, 'su').click()


if __name__ == '__main__':
    unittest.main()
