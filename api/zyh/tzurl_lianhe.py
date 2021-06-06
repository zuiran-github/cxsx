from selenium import webdriver

def openChrome():

    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')

    # 打开谷歌浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

def operationAuth(driver):

    url = 'http://www.flycua.com/'
    driver.get(url)

    # 找到输入框并输入查询内容

    driver.find_element_by_id("_easyui_textbox_input1").click()
    driver.find_element_by_id("_easyui_textbox_input1").clear()
    elem1 = driver.find_element_by_id("_easyui_textbox_input1")
    elem1.send_keys("北京")
    driver.find_element_by_id("_easyui_combobox_i50_0").click()

    driver.find_element_by_id("_easyui_textbox_input2").click()
    driver.find_element_by_id("_easyui_textbox_input2").clear()
    elem2 = driver.find_element_by_id("_easyui_textbox_input2")
    elem2.send_keys("上海")
    # time.sleep(1)
    driver.find_element_by_class_name("cityname").click()

    elem3 = driver.find_element_by_id("deptDateShowGo")
    elem3.send_keys("2021-06-30")

    # 提交表单
    driver.find_element_by_id("portalBtn").click()

    print('over')


driver = openChrome()
operationAuth(driver)