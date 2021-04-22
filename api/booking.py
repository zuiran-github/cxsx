import math
import requests
from bs4 import BeautifulSoup
import re

def getdata(city,checkin,checkout,start):
    url = 'https://www.booking.com/searchresults.zh-cn.html?'
    header ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        }
    param ={
        'ss': city,
        'checkin_monthday': checkin[8:10],
        'checkin_year_month': checkin[0:7],
        'checkout_monthday': checkout[8:10],
        'checkout_year_month': checkout[0:7],
        'group_adults': 2,
        'group_children': 0,
        'no_rooms': 1,
    }

    if start==0:
        res = requests.get(url=url, headers=header, params=param)
        total_item = "".join(re.findall(r'b\_available\_hotels\:(.*?)\,', res.text))
        print(total_item)
        page = math.ceil(int(total_item) / 25)
        return res.text,page
    else:
        param['offset'] =start
        res = requests.get(url=url, headers=header, params=param)
        return res.text

def getList(city,checkin,checkout):
    start = 0
    day = int(checkout[8:10])-int(checkin[8:10])
    list,page = getdata(city,checkin,checkout,start)
    #print(list)
    print("page1")
    printList(list,day)
    for i in range(1,2,1):
        print("page" + str(int(i+1)))
        list = getdata(city,checkin,checkout,i*25)
        printList(list,day)


def printList(list,day):
    soup = BeautifulSoup(list, 'html.parser')
    Hotels = soup.select('.sr_property_block')
    print('----------------------------------------')
    for name in Hotels:
        print()
        text = name.select('.sr-hotel__name')[0].get_text().strip() + name.select('.bui-review-score__badge')[
            0].get_text().strip()
        str = 'https://www.booking.com/' + name.select('.hotel_name_link')[0]['href'].strip()
        print(text)
        print(name.select('.hotel_image')[0]['data-highres'])
        print(str.rstrip(';highlight_room=#hotelTmpl').strip())
        #print(name.select('.bui-rating bui-rating')[0]['aria-label'].get_text())
        print(name.select('.bui-review-score__text')[0].get_text().strip())
        #price =int(int(name.select('.bui-price-display__value')[0].get_text().strip().strip('元').replace(',',''))/day)
        price = (name.select('.bui-price-display__value')[0].get_text().strip())
        print(price)

getList('上海','2021-04-22','2021-04-25')