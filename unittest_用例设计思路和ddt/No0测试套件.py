import unittest
class auto(unittest.TestCase):
    # 类的初始化
    @classmethod
    def setUpClass(cls):
       print('类初始化')
    #  类的释放
    @classmethod
    def tearDownClass(cls):
        print('类释放')
    # 初始化
    def setUp(self):
        print('测试用例初始化')

    def tearDown(self):
        print('测试用例释放')
    # 测试用例
    def test_androd(self):
        print('我正在学习单元测试')

    def test_android(self):
        print('第一个测试用例')

    def function(self):                      #不以test开头为一个方法，以test开头在unittest中被称为测试用例
        print('hello world')
if __name__=='__main__':
     unittest.main()

