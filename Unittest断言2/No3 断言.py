import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import ddt
from ddt import file_data,ddt
@ddt
class assert_point(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @file_data('c.yml')
    def test_assert(self,**kwargs):
        key=kwargs.get('name')
        self.assertEqual(key,'sigma',msg='NONONONO!')
        print(key)
    def test_practice1(self):
        self.assertIn('sigma','sigmafewgewf',msg='Wrong')

    def test_practice2(self):
        self.assertEqual(6,6,msg='a is not b')



if __name__=='__main__':
    unittest.main()

