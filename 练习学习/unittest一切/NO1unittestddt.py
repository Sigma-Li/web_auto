import time
import unittest
import yaml
from ddt import ddt,unpack,data,file_data

from selenium import webdriver
from selenium.webdriver.common.by import By

def read1():
    list=[]

    f=open('data1.txt', 'r', encoding='utf-8')
    ff=f.readlines()
    for i in ff:
        list.append(i.replace('\t',' ').strip('\n').split(' '))

    return list

def read2():
    datas=list()
    file1=open('data2.txt','r',encoding='utf-8')
    for data in file1.readlines():
        datas.append(data.replace('\t',' ').strip('\n').split(' '))
    return datas




@ddt
class myself_learning1(unittest.TestCase):
    # 测试夹具 清理释放资源
    def setUp(self):      #用例的释放
        pass
    def tearDown(self):

        pass

    def test6(self):
        print('this is the last test')

    # @unittest.skip('暂时跳过')
    def test1_math(self):
        sum=0
        for i in range(1,101):
            if i%2==0:
                sum+=i
        print(sum)

    #数据驱动 相关测试用例  使用之前在类前面声明

    #  导入数据(列表)
    # @unittest.skip('ffffff')
    @data(['微软翻译'],['软件测试','南通大学'],('helloaaaa'),'namess')
    def test3_1ddt1(self,names):
        print(names)

    # @unittest.skip('暂时跳过')
    @data(('微软翻译','软件件测试'),('nandon','hello'))
    @unpack
    def test3_1unpack(self,name,age):
        print(name)
        print(age)
    #
    # @unittest.skip('暂时跳过')
    @data(read1())
    def test3_2fileread(self,*info):
        print(info)

    @data(*read2())    #文件数据有多行，需要解析数据
    @unpack
    def test3_3filedread(self,*detail):
        print(detail)

    @data(read2())
    @unpack
    def test3_4fileread(self,*ddd):   #形参带* 不定长参数
        print(ddd)


    @data(*read2())
    @unpack
    def test3_5filedread(self,record,t,y):
        print(record)
        print(t)
        print(y)

    #只处理yml 文件
    @file_data('data3.yml')
    def test4_1yml(self,**value):
        # print(value.get('ID'))
        print(value.get('state'))

    @file_data('data4.yml')
    def test4_2yml(self,**value1):
        print(value1.get('name'))



if __name__=='__main__':
    unittest.main()