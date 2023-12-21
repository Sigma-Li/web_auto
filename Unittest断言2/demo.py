# 取出data111文件中的前两列，并调换位置，然后写到新的文件里
import yaml
import unittest
from ddt import ddt,file_data
list1=open('data111','r',encoding='utf-8')
type(list1.readline())
l=list1.readlines()
# print(type(l))          readlines() 返回的是列表，需要将其转换成字符串
a=list()
for i in l:                 # i是字符串
    details=i.strip('\n ').split('\t')
    del details[2:7]   #删除列表第二位到最后的所有元素，只保留bug 和id

    ss=str(details)

    aa=ss.replace(',',':')
    a.append(aa)
print(a)

bug=open('bug.yml','w',encoding='utf-8')
bug.write(str(a))
class get_id(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


