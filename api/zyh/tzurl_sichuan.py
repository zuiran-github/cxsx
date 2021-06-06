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

    url = 'https://www.sichuanair.com/'
    driver.get(url)

    # 找到输入框并输入查询内容
    # driver.find_element_by_id("Search-OriginDestinationInformation-Origin-location_input_location").click()

    elem1 = driver.find_element_by_name("Search/OriginDestinationInformation/Origin/location_input")
    elem1.clear()
    driver.execute_script("arguments[0].click();", elem1)
    elem1.send_keys("北京")

    # driver.find_element_by_id("Search-OriginDestinationInformation-Destination-location_input_location").click()
    elem2 = driver.find_element_by_name("Search/OriginDestinationInformation/Destination/location_input")
    elem2.clear()
    driver.execute_script("arguments[0].click();", elem2)
    elem2.send_keys("上海")

    elem3 = driver.find_element_by_name("Search/DateInformation/departDate_display")
    elem3.clear()
    elem3.send_keys("2021-07-09")
    driver.execute_script("arguments[0].click();", elem3)


    # 提交表单
    btn = driver.find_element_by_class_name("item-b")
    driver.execute_script("arguments[0].click();", btn)

driver = openChrome()
operationAuth(driver)
