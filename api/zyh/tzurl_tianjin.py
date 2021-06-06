from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):

    url = 'http://www.tianjin-air.com/'
    driver.get(url)


    elem1 = driver.find_element_by_class_name("trigger").find_element_by_tag_name("input")
    elem1.send_keys("天津")
    # driver.find_element_by_class_name("hover").click()


    elem2 = driver.find_element_by_class_name("field").find_element_by_tag_name("input")
    elem2.send_keys("成都")
    # driver.find_element_by_class_name("hover").click()







driver = openChrome()
operationAuth(driver)
