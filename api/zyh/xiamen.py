# coding:utf
import multiprocessing
from multiprocessing import Process
import time
import datetime
import pymysql
from lxml import etree
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

# 机场代码列表，这里只是添加了几个做案例
list = ["CGO,DLC", "CGO,FOC", "CGO,HAK", "CGO,HET", "CGO,HRB", "CGO,INC", "CGO,JJN"]

# 现在的时间
now = datetime.datetime.now()
# 递增的时间
delta = datetime.timedelta(days=1)
# 30天后的时间
endnow = now + datetime.timedelta(days=2)
# 六天后的时间转换成字符串
endnow = str(endnow.strftime('%Y-%m-%d'))

# 链接数据库----------------------------------------------
# connect = pymysql.connect(
#     user="root",
#     password="520134",
#     port=3306,
#     host="127.0.0.1",
#     db="mysql",
#     charset="utf8"
# )
# con = connect.cursor()  # 获取游标
# con.execute("use mysql")  # 使用数据库


def func(url):
    urlc = url  # 传进来的url是"CGO,FOC"这样，所以完整的url需要拼接
    global now  # 用全局变量把当天日期导进来
    # now 是当天的日期，一般抓取都是从当天开始抓，所以每次运行都可以不用管，这是根据代码开始运行的日期自动生成，每天跑一次，然后存到数据库。
    urls = 'https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo' \
           'https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=SHA&dstCodeArr%5B0%5D=PKX&orgDateArr%5B0%5D=2021-05-12&dstDate=&isInter=false&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false' \
           '=' + str(
        url) + ',' + str(now)
    global endnow  # 用全局变量把30天后的日期导进来

    driver = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}  # 不加载图片
    driver.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=driver)
    driver.get(urls)

    while True:
        # 找到加载更多舱位的xpath节点，
        qqq = driver.find_elements_by_xpath(
            "//div[@class='segment-mess']/div[@class='form-mess']/div[@class='spe-line']/a[@class='right show-more webtrends-findFlights-showMore']/span")
        # 遍历每一个节点，挨个点击加载
        for i in qqq:
            try:
                ActionChains(driver).click(i).perform()  # 对定位到的元素执行鼠标左键操作
                print(u'正在加载当前航班所有机票价格...')
                time.sleep(2)
            except Exception as e:
                print(u'加载失败', e)

        # 加载完的界面
        html = driver.page_source
        response = etree.HTML(html)
        print(u'全部加载完成')

        # 通过xpath把加载完的页面数据全部取出来，做一一对应
        for each in response.xpath("//div[@class='form-mess']"):
            hangci = each.xpath(".//span[@class='form-flt-num']/text()")[0]
            starttime = each.xpath(".//div[@class='col-lg-2 col-md-2 col-sm-2 col-xs-2']/h2[@class='bold']/text()")[0]
            endtime = each.xpath(".//div[@class='col-lg-2 col-md-2 col-sm-2 col-xs-1']/h2[@class='bold']/text()")[0]
            lists = each.xpath(".//div[@class='form-mess-inner hide-mess cabin-info spe-height lh30 clear']")
            for i in lists:
                item1 = urlc  # 出发城市，到达城市，将他们做字符串切割
                dep = item1[:3]
                arr = item1[4:]
                flightNo = 'MF' + hangci  # 航次
                official_price = i.xpath(".//span[@class='flight-price']/text()")[0]  # 价格
                cabin = i.xpath(".//span[@class='form-cabin']/text()")[0]  # 座位等级 例如 F 表示头等舱
                flightTime = starttime  # 出发时间
                # item6= endtime      #到达时间
                flightDate = response.xpath("//div[@class='nav-outer low-price-nav']//li[@class='this-tab']//h3/@date")[
                    0]  # 出发日期
                uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 爬取时间

                # 尝试传入数据库，根据你们自身mysql表的设计，酌情修改；或者不传数据库做写入文本也可以
                try:
                    # con.execute(
                    #     "insert into ceshi(dep,arr,flightNo,official_price,cabin,flightTime,flightDate,uptime)values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    #     [dep, arr, flightNo, official_price, cabin, flightTime, flightDate, uptime])
                    # connect.commit()  # 我们需要提交数据库，否则数据还是不能上传的
                    print(dep, arr, flightNo, official_price, cabin, flightTime, flightDate, uptime)
                    print('数据正在上传...')
                except Exception as e:
                    print('数据上传失败...', e)
                    pass

        # 定位下一日期
        date = response.xpath('//*[@id="load-mess"]/div[1]/div[1]/div[2]/div[1]/ul/li[5]/a/h3/@date')[0]

        # 当下一日期等于指定日期，就停止循环
        if str(date) == endnow:
            time.sleep(5)
            driver.quit()
            break
        # 一直点击下一页
        qq = driver.find_element_by_xpath('//*[@id="load-mess"]/div[1]/div[1]/div[2]/div[1]/ul/li[5]')
        ActionChains(driver).click(qq).perform()
        time.sleep(2)


if __name__ == "__main__":
    # 开启两个进程，即同时打开两个谷歌浏览器爬取
    pool = multiprocessing.Pool(processes=2)
    for i in list:
        pool.apply_async(func, (i,))
    pool.close()
    pool.join()
    print("done")

# 如果是大规模爬取，建议添加随机userAgent和ip代理，不然可能被封





