# 不执行，直接跳过
import unittest


class Skip_learn(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 无条件跳过该用例
    @unittest.skip('dont want to test this ')
    def tes_1(self):
        print('hello world')

    def test_2(self):
        print(0)
    # 有条件跳过操作,即条件成立时跳过
    @unittest.skipIf(5<8,'Right ')
    def test_3(self):
        print('Not')
    # 有条件跳过操作,即条件不成立时跳过
    @unittest.skipUnless(5>8,'No!')
    def test_4(self):
        print('Yes')
    #如果用例执行失败，则不计入失败的case数量
    @unittest.expectedFailure
    def test_5(self,x,y):            #关于函数知识点还需要加强，这个函数有问题。但是能体现 @unittest.expectedFailure， 所以暂时留在这里
        x=5
        y=9
        return x>y
    def test_6(self,a,b):
        a = 5
        b = 9
        return a > b

if __name__ == '__main__':
    unittest.main()
