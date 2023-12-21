import time
from pom阶段.POMWEB.basicclass.No1Basic import webSite
from selenium.webdriver.common.by import By
from selenium import webdriver
class JumpPage(webSite):
    # 核心元素
    url='https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%82%96%E6%88%98&fenlei=256&rsv_pq=0xc00e493300089679&rsv_t=dc3dXHd%2BQ5iyvLdSBy27hYwRi0icHEOIRxyaibJkZDfpxFTgbhwpGgCgT3ZK&rqlang=en&rsv_enter=1&rsv_dl=ih_0&rsv_sug3=2&rsv_sug1=2&rsv_sug7=001&rsv_sug2=1&rsv_btype=t&rsp=0&rsv_sug9=es_2_1&rsv_sug4=87388&rsv_sug=9'
    record1=(By.CSS_SELECTOR,'h3[class="t"]')

    # 核心业务
    def jump(self):
        self.startup()
        self.click1(self.record1)
        self.wait()
# if __name__=='__main__':
#     driver=webdriver.Edge()
#     dx=JumpPage(driver)
#     dx.jump()



