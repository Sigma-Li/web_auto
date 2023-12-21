# no5 中，无论用例顺序如何，执行顺序总是以用例名顺序开始执行，想要按照指定顺序运行们需要用到测试套件 test suite
# 测试套件suite
import unittest
from no5sometestcasesforno6 import *
from HTMLTestRunner import HTMLTestRunner
import os

# 创建一个测试套件 ==list
var=unittest.TestSuite()

# 方法1 和 2 可以更改用例执行顺序
# 添加测试用例（子元素）到测试套件（集合）
#添加测试用例方式1：一个一个添加
'''var.addTest(about_testsuite('test_2'))
var.addTest(about_testsuite('test_3'))
var.addTest(about_testsuite('test_4'))'''
# 套件通过TextTestRunner对象进行运行 相当于 unittest.main()
'''runner=unittest.TextTestRunner()
runner.run(var)'''
# 有知识点还不会: ===>已经解决，就是添加测试用例方法3
# var.addTest(about_testsuite('test_1'))

# 添加测试用例方式2
'''case_list=[about_testsuite('test_4'),about_testsuite('test_2'),about_testsuite('test_3')]
var.addTests(case_list)
run=unittest.TextTestRunner()
run.run(var)'''

#添加测试用例方法3 批量运行多个文件

'''test_dir='./'
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='no5*.py')
running=unittest.TextTestRunner()
running.run(discover)'''


# 添加测试用例方式4
var.addTest(unittest.TestLoader().loadTestsFromTestCase(about_testsuite))
ran=unittest.TextTestRunner()
file='report.html'
path=open('file','wb')
result=HTMLTestRunner(stream=path,description='Test case about Android',title='Reporttt')

result.run(var)
path.close()

# 添加测试用例方式5
'''var.addTest(unittest.TestLoader().loadTestsFromName('no5sometestcasesforno6.about_testsuite'))
runninga=unittest.TextTestRunner()
runninga.run(var)'''

