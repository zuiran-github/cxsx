from selenium import webdriver
import time

def openChrome():

    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')

    # 打开谷歌浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

def operationAuth(driver):

    url = 'http://et.airchina.com.cn'
    driver.get(url)

    # 找到输入框并输入查询内容
    elem1 = driver.find_element_by_id("0")
    driver.find_element_by_id("0").click()
    elem1.send_keys("北京首都国际机场")
    print(driver.find_element_by_class_name("cityname").text)
    driver.find_element_by_class_name("cityname").click()

    # time.sleep(3)

    elem2 = driver.find_element_by_id("1")
    driver.find_element_by_id("1").click()
    elem2.send_keys("上海浦东机场")
    # time.sleep(3)
    print(driver.find_element_by_class_name("cityname").text)
    driver.find_element_by_class_name("cityname").click()
    # print(driver.find_element_by_xpath("//*[@class=\"citySelector\"]/ul/li/b").text)#.click()


    elem3 = driver.find_element_by_id("deptDateShowGo")
    elem3.send_keys("2021-06-30")

    # 提交表单
    # driver.find_element_by_id("portalBtn").click()

    print('over')


driver = openChrome()
operationAuth(driver)
