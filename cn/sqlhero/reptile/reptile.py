from selenium import webdriver
#爬取类
class reptile:
    #对网站进行连接
    def get_connect(url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=r'D:/apply/not_hear_Chrome/2.39/chromedriver.exe')
        driver.get(url)
        return driver

    #获取当前页面的所有a连接
    def get_page_alist(driver):
        return driver.find_elements_by_tag_name('a')

    #获取当前页面的所有图片
    def get_page_image(driver):
        return driver.find_elements_by_tag_name('img')



