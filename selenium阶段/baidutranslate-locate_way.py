import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class baidu_translater(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_open(self):
        wb=webdriver.Edge()
        wb.implicitly_wait(5)
        wb.get('https://fanyi.baidu.com/')
        # 关闭弹窗
        wb.find_element(By.CLASS_NAME,'desktop-guide-close').click()
        inputc = wb.find_element(By.CLASS_NAME, 'textarea')
        inputc.send_keys(input('请输入翻译内容：'))
        tolanguage=input('你想翻译成什么语言：')

        # to 语言下拉框点击
        wb.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div[1]/a[3]/span').click()
        language_list=wb.find_element(By.CLASS_NAME,'lang-table')
        # 语言列表数据处理
        language_format=language_list.text.replace('语','语,')
        # print(language_format)

        if tolanguage in language_format:
            # 搜索框输入语言
            wb.find_element(By.CLASS_NAME,'search-input').send_keys(tolanguage)

            # 点击搜索出来第一个语言
            wb.find_element(By.CLASS_NAME, 'search-result').click()
            time.sleep(5)
            # 输出翻译的内容
            outputc = wb.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/p[2]')

            print(outputc.get_attribute('innerHTML'))

        else:
            print('No such language!!!')

if __name__ =='__main__':
    unittest.main()