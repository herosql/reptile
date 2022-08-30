import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://www.baidu.com"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

chrome_path = r'/home/liliang/Documents/apply/chromeNoHead/chromedriver_linux64'

chrome_service = Service(chrome_path)

driver = webdriver.Chrome(options=chrome_options,service=chrome_service)
driver.get(url)
print(driver.get_cookies())

savedCookies = driver.get_cookies()


from selenium import webdriver
#测试类
# class Test:
# from Reptile import Reptile

# 通过改变请求头伪装成一个正常用户访问页面
# import requests
# from bs4 import BeautifulSoup
# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac Os X 10_9_5)AppleWebKit 557.36 "
#                         "(KHTML,like Gecko) Chrome","Accept":"text/html,application/xhtml+xml,application/xml;"
#                                                              "q=0.9,image/webp,*/*;q=0.8"
#            }
# # 将请求头设置为移动端访问（可以减少广告和flash）
# headers = {
#     "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53",
#     "Accept":"*/*",
#     "Accept-Language":"zh-CN,zh;q=0.9"
# }
# url = "https://www.whatismybrowser.com/" \
#       "developers/what-http-headers-is-my-browser-sending"
# req = session.get(url,headers=headers)
# bsObj = BeautifulSoup(req.text)
# print(bsObj.find("table",{"class":"table-striped"}).get_text)


# 通过保存cookie伪装成一个用户
# driver = webdriver.Chrome(executable_path='')
# driver.get("http://pythonscraping.com")
# driver.implicitly_wait(1)
# print(driver.get_cookies())


#
# driver2.get(url)
# driver.implicitly_wait(1)
# print(driver2.get_cookies())

#selenium爬取网站标签
# import urllib.request
# import uuid
# # from selenium import webdriver
# # url = 'http://www.xiuzhen123.com'
# #
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
# # driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:/apply/not_hear_Chrome/chromedriver.exe')
# # driver.get(url)
#
## # links = driver.find_elements_by_tag_name("a")
# #
# # for link in links:
# #     print(link.get_attribute('herf'))
# #     if not link.is_displayed():
# #         print("The link :",link.get_attribute("herf"))
# #     else:
# #         print("The link :", link.get_attribute("herf"))
#
# #获取当前页面中的input标签集合
# # fields = driver.find_elements_by_tag_name("input")
# # for field in fields:
# # #校验是否是隐藏标签
# #     if not field.is_displayed():
# #         print("Do not change value of ",field.get_attribute("name"))
#
# #获取img标签中的图片
# # imgs = driver.find_elements_by_tag_name("img")
# # imgList = []
# # for img in imgs:
# #     imgList.append(img.get_attribute("src"))
## 使用selenium和谷歌无头模式自动化工具进行信息爬取


# #获取当前页面中的a标签集合

#     # 获取字符串中特定字符最后出现的位置
#
#
# # def find_last(string, str):
# #     last_position = -1
# #     while True:
# #         position = string.find(str, last_position + 1)
# #         if position == -1:
# #             return last_position
# #         last_position = position
# #
# #
# # print('完成。。。。。。。。')
#
#
#


# time.sleep(3 +  random.seed(10))
#
# driver2 = webdriver.Chrome(options=chrome_options,service=chrome_service)
# driver2.get(url)
# driver2.delete_all_cookies()
#
# for cookie in savedCookies:
#     driver2.add_cookie(cookie)