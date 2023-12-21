import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest

driver = webdriver.Edge()
driver.get('https://translator.microsoft.com/')
class MT_web(unittest.TestCase):
    def setUp(self):
        pass


    def tearDown(self):
        pass

    def test_logging(self):
        driver.implicitly_wait(10)
        # 对话代码
        driver.find_element(By.CSS_SELECTOR,'.mb-3>div>input[maxlength="5"]').send_keys(input('conversation code:'))
        # 用户名
        driver.find_element(By.CSS_SELECTOR,'.mb-3>div>input[aria-label="Username"]').send_keys(input('Username:'))
        #语言选择下拉框
        driver.find_element(By.CSS_SELECTOR,'div select[name="Language"]').click()
        # 选择语言
        language=str(input("What's your language:"))
        language_option=driver.find_elements(By.CSS_SELECTOR,'select optgroup option')

        liss=list()
        for language1 in language_option:
            var=language1.text
            liss.append(var.strip(' '))

        if language in liss:
            driver.find_element(By.CSS_SELECTOR,f'select optgroup option[aria-label="{language}"]').click()
            time.sleep(5)
            # lo=Select(self.driver.find_element(By,'Language'))
            # lo.select_by_visible_text(f'{language}')
            driver.find_element(By.CSS_SELECTOR,'div  button[type="submit"]').click()
        else:
            print('No such language!!!')

        time.sleep(5)






