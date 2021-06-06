from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# 前台开启浏览器模式
from selenium.webdriver import ActionChains


def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):

    url = 'https://www.hnair.com'
    driver.get(url)

    driver.find_element_by_id("from_city1").click()

    # 找到输入框并输入查询内容
    elem1 = driver.find_element_by_id("from_city1")
    elem1.send_keys("北京大兴")

    elem2 = driver.find_element_by_id("to_city1")
    elem2.send_keys("上海虹桥")

    elem3 = driver.find_element_by_id("flightBeginDate1")
    elem3.clear()
    elem3.send_keys("2021-07-05")

    elem3.click()

    time.sleep(3)

    # 提交表单
    # print(driver.find_element_by_class_name("fr").text)
    # driver.find_element_by_class_name("fr").click()
    ActionChains(driver).move_to_element(driver.find_element_by_class_name("fr")).perform()
    # driver.find_element_by_link_text("搜索航班").click()

driver = openChrome()
operationAuth(driver)

