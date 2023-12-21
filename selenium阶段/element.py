import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Edge()
driver.implicitly_wait(5)    #隐式等待10 秒方式页面加载太慢，运行报错
net=driver.get('https://baidu.com/')

# time.sleep(5)



# 元素定位方式
# 方法1 id    id唯一时
'''driver.find_element(By.ID,'kw').send_keys('元素定位')
driver.find_element(By.ID,'su').click()'''


'''attr=driver.find_element(By.ID,"footerUniversalFooter")
print(attr.text)
time.sleep(3)'''


# 方法2 name name唯一
'''code=(driver.find_element(By.NAME,'Conversation code:'))
code.send_keys('abcd')
print(code.get_attribute('value'))      # input 输入框的内容，想获取输入的文本，用 get_attribute('value')       不能直接是 code=(driver.find_element(By.NAME,'Conversation code:'))。send_keys('abcd')
print(code.get_attribute('placeholder'))        #得到某个属性值
print(code.get_attribute('outerHTML'))          #得到整个某对应HTML文本内容
print(code.get_attribute('innerHTML'))          #某个元素内部html文本内容'''
# get_attribute('innerText')  /get_attribute('textContent')
# input 输入框的内容，想获取输入的文本，用 get_attribute('value')

# 方法3 class_name  <div class='' />
'''a=driver.find_elements(By.CLASS_NAME,'dropdown')
for i in a:
    print(i.text)
print('******************************************************')'''
# 方法4 tag_name  <标签名  />   --- <option=''/>
'''var_tag=driver.find_elements(By.TAG_NAME,'option')
for ee in var_tag:
    print(ee.text)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')'''

# 以上是webdriver对象 选择元素   driver.    从整个页面定位元素。也可以用webelement对象选择元素，范围是元素内部。
'''webdriver1=driver.find_element(By.CLASS_NAME,'dropdown')
webelement=webdriver1.find_element(By.TAG_NAME,'label')
print(webelement.text)
time.sleep(5)'''
#   以上目前不适用，需要重新一个网页看 ***************************************************************************************************


# 方法5  link_text  a标签
# 方法6 partial_link_text a标签
# 方法7 xpath
# 方法8 css 选择元素
#  8.1 css-tag 标签名
'''se=driver.find_elements(By.CSS_SELECTOR,'img')
for details in se:
    print(details.get_attribute('outerHTML'))'''

# 8.2 css- id   #id
'''driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('hello')
time.sleep(10)'''

# 8.3 css-class .class
'''driver.find_element(By.CSS_SELECTOR,'.s_ipt').send_keys('Sigma')
time.sleep(10)'''

# 8.4 css-子元素 和 后代元素
# text=driver.find_elements(By.CSS_SELECTOR,'#s-hotsearch-wrapper>div')    #子元素  用 >
# text=driver.find_elements(By.CSS_SELECTOR,'#s-hotsearch-wrapper div a  i'  )  #后代元素用 空格，层级可以不用一级一级如下一行,li标签下还有很多子元素，我空格后 选了后代元素 span
# text=driver.find_elements(By.CSS_SELECTOR,'#s-hotsearch-wrapper ul li span')
'''text=driver.find_elements(By.CSS_SELECTOR,'#head_wrapper #lg map')
for attribute in text:
    print(attribute.get_attribute('innerHTML'))'''

# 8.5 css-任何属性元素，用[]
# text=driver.find_element(By.CSS_SELECTOR,'[href="https://www.baidu.com/s?wd=%E5%90%B4%E4%BA%A6%E5%87%A1%E6%A1%88%E4%BA%8C%E5%AE%A1%E7%BB%B4%E6%8C%8113%E5%B9%B4%E5%8E%9F%E5%88%A4&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1"]').click()
'''text=driver.find_elements(By.CSS_SELECTOR,'[href]')  #可以不用href后的值
for links in text:
    print(links.get_attribute('innerHTML'))
# print(text.get_attribute('innerHTML'))
time.sleep(5)'''

# 8.6 组合使用  css selecter 验证 统一属性，用，，如示例网页选择所有的植物和动物
'''text=driver.find_elements(By.CSS_SELECTOR,'#s-hotsearch-wrapper>ul>li>a[href="https://www.baidu.com/s?wd=%E6%99%AE%E4%BA%AC%EF%BC%9A%E5%BF%85%E9%A1%BB%E8%80%83%E8%99%91%E5%A6%82%E4%BD%95%E7%BB%93%E6%9D%9F%E8%BF%99%E5%9C%BA%E6%82%B2%E5%89%A7&sa=fyb_n_homepage&rsv_dl=fyb_n_homepage&from=super&cl=3&tn=baidutop10&fr=top1000&rsv_idx=2&hisfilter=1"]')
for link in text:
    print(link.get_attribute('innerHTML'))
    time.sleep(5)'''


#  CSS selecter验证