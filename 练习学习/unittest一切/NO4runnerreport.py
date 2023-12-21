from HTMLTestRunner import HTMLTestRunner
import unittest
from NO2assertsip import assert1
from NO1unittestddt import myself_learning1
suite=unittest.TestSuite()
# suite.addTest(assert1('test3'))
# suite.addTest(assert1('test2'))
# runner=unittest.TextTestRunner()
# runner.run(suite)
# *************************************************************************************************
# cases=[assert1('test2'),assert1('test4'),assert1('test3')]
# suite.addTests(cases)
#
# file_name='练习测试报告.html'
# file=open(file_name,'wb')
# runner3=HTMLTestRunner(stream=file,title='Li',description='这是一个简单的测试报告')
# runner3.run(suite)


# location='./'
# name='离婚报告.html'
# f=open(name,'wb')
# runnerdiscover=unittest.defaultTestLoader.discover(start_dir=location,pattern='NO2assertsip.py')
# # runner=unittest.TextTestRunner()
# # runner.run(runnerdiscover)
# runne=HTMLTestRunner(stream=f,title='啦啦啦啦啦')
# runne.run(runnerdiscover)

# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(myself_learning1))
# # runner=unittest.TextTestRunner()
# # runner.run(suite)
# name1='第三种方法测试.html'
# fil=open(name1,'wb')
# report=HTMLTestRunner(stream=fil,title='liqiying',description='我i正在学习unittest')
# report.run(suite)

suite.addTest(unittest.TestLoader().loadTestsFromName('NO1unittestddt'))
# runner=unittest.TextTestRunner()
# runner.run(suite)
name='关于名字测试报告.html'
filer=open(name,'wb')
u=HTMLTestRunner(stream=filer,title='你好吗',description='这是关于名字的测试报告')
u.run(suite)
