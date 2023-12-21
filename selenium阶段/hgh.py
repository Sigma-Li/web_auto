import time

import selenium
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

dd=webdriver.Edge()
dd.implicitly_wait(10)
dd.get('https://translator.microsoft.com/')

language=input('Language:')
language1=dd.find_element(By.NAME,'Language').click()
lla=dd.find_elements(By.CSS_SELECTOR,'select optgroup option')
nu=list()
for q in lla:
    li=q.text
    nu.append(li.strip(''))
print(nu)


if language in nu:
        dd.find_element(By.CSS_SELECTOR,f'select optgroup [aria-label="{language}"]' ).click()
time.sleep(10)
lan=Select(dd.find_element(By.NAME,'Language'))
print(lan.select_by_visible_text('French'))