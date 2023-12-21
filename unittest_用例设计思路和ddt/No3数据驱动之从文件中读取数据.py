import unittest
from ddt import ddt, unpack, data

# 知识点：文件的打开读取
#  字符串格式处理，切片，追加到列表
def Readfile():
    list = []
    dataf = open('data3', 'r', encoding='utf-8')
    for elements in dataf.readlines():
        list.append(elements.strip('\n').split(' '))
        print(elements)
    return list

# print(list)
@ddt
class Stuinfo(unittest.TestCase):
    def setUp(self):
        print('初始化')
    def tearDown(self):
        print('释放')

    @data(*Readfile())
    @unpack
    def test_1(self,name,age):
        print(name)
        print(age)

if __name__=='__main__':
    unittest.main()



