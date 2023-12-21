import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class assert1(unittest.TestCase):
    def setUp(self):
        pass
    # @unittest.expectedFailure       #如果用例执行失败，不计入失败的用例数中   报错不是红色
    # def test1(self):   #条件成立时测试通过，不成立时输出msg
    #     self.assertEqual(int(input("输入数字A：")),1,msg="不成立，两值不一样")

    def test2(self):
        self.assertNotEqual(8,9,msg='错！一样')
    def common1(self):
        self.d=webdriver.Edge()
        self.y=self.d.get('https://www.baidu.com/')

    # @unittest.skipIf(1<2,'条件成立，跳过')     #有条件挑过执行  条件为True 跳过
    def test3(self):
        self.common1()

        search_button=self.d.find_element(By.ID,'su')
        self.assertIsNotNone(search_button,msg='按钮不存在')   #存在 pass,否则报错
        time.sleep(5)
    # @unittest.skipUnless(8<2,'不成立，跳过')    #有条件执行 条件为False 跳过
    def test4(self):
        self.common1()
        input_box=self.d.find_element(By.ID,'kw')  #不存在 pass
        self.assertIsNone(input_box,msg='输入框存在')
        time.sleep(5)







if __name__=='__main__':
    unittest.main()
