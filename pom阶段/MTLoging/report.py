import unittest
from HTMLTestRunner import HTMLTestRunner
from pom阶段.MTLoging.testcase import casess


suite=unittest.TestSuite()
name='关于点击测试报告1.html'
file=open(name,'wb')
path='./'
u=unittest.defaultTestLoader.discover(start_dir=path,pattern='testcase.py')

s=HTMLTestRunner(stream=file,title='oooo',description='ppppp')
s.run(u)