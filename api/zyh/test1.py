from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'geckodriver')
url = "https://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=BJS&c2=SHA&d1=2021-04-20&at=1&ct=0&it=0&b1=PEK-PKX&b2=SHA-PVG"
driver.get(url)

print(driver.page_source)
comment = driver.find_element_by_css_selector('div.zls-flplace')
content = comment.find_element_by_class_name('zls-flplace')
print(content.text)