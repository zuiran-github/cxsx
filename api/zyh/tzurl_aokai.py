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

    url = 'https://www.okair.net/welcome.html#/'
    driver.get(url)

    # driver.find_element_by_id("ticketDepCitypicker").click()

    # 找到输入框并输入查询内容
    elem1 = driver.find_element_by_id("from_city1")
    elem1.send_keys("北京大兴")

    elem2 = driver.find_element_by_id("to_city1")
    elem2.send_keys("上海虹桥")

    elem3 = driver.find_element_by_id("flightBeginDate1")
    elem3.clear()
    elem3.send_keys("2021-07-05")

    elem3.click()

    # 提交表单
    # driver.find_element_by_class_name("clearfix display-none row-5").click()


driver = openChrome()
operationAuth(driver)

