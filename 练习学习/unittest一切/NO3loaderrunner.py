
from 练习学习.unittest一切.NO1unittestddt import *
from NO1unittestddt import myself_learning1
import unittest
from NO2assertsip import assert1
from HTMLTestRunner import HTMLTestRunner
import os

the_suite=unittest.TestSuite()
# NO1 以下添加方式无法执行读取文件的用例
'''the_suite.addTest(myself_learning1('test6'))
the_suite.addTest(myself_learning1('test1_math'))
runner1=unittest.TextTestRunner()
runner1.run(the_suite)'''

#NO2  把所执行用例添加到一个列表，集中执行
'''vars=[myself_learning1('test6'),myself_learning1('test1_math')]
the_suite.addTests(vars)
runner=unittest.TextTestRunner()
runner.run(the_suite)'''


#NO3 批量运行多个测试用例文件     读取文件的用例可以被执行
test_path='./'   #./表示当前位置
dis=unittest.defaultTestLoader.discover(start_dir=test_path,pattern='NO1unittestddt.py')
# runner2=unittest.TextTestRunner()
# runner2.run(dis)


#NO4
'''the_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(assert1))

runnerr=unittest.TextTestRunner()
runnerr.run(the_suite)'''


#NO 5
# the_suite.addTests(unittest.TestLoader().loadTestsFromName('NO1unittestddt.myself_learning1.test6'))      #文件名.类名。用例名字
# runneer=unittest.TextTestRunner()
# runneer.run(the_suite)



#test result


#刚开始运行出错是因为把 path 引号
file='result.html'
path=open(file,'wb')

runner=HTMLTestRunner(stream=path,description='测试报告',title='李启盈')
runner.run(dis)
path.close()
