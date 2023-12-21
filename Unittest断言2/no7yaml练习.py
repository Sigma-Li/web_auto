'''import unittest

import yaml
import ddt
from ddt import ddt,file_data
# f=open('bugdata.yml',encoding='utf-8')
# content=yaml.load(f,Loader=yaml.FullLoader)
# # print(type(content))

@ddt
class demo_yaml(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @file_data('bugdata.yml')
    def test_1(self,**kwargs):
        print(kwargs.get('id'))


if __name__=='__main__':
    unittest.main()
'''

import yaml
f=open('bug.yml',encoding='utf-8')
a=yaml.load(f,Loader=yaml.FullLoader)
print(a)
