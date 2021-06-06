import requests
from bs4 import BeautifulSoup
import json
import socket
import random


class GetIp(object):
    """抓取代理IP"""

    def __init__(self):
        """初始化变量"""
        self.url = 'http://www.ip3366.net/?stype=1&page=7'
        self.check_url = 'https://www.baidu.com'
        self.ip_list = []



    @staticmethod
    def get_html(url):
        """请求html页面信息"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        try:
            request = requests.get(url=url, headers=header)
            request.encoding = 'utf-8'
            html = request.text
            return html
        except Exception as e:
            return ''



    def get_available_ip(self, ip_address, ip_port):
        """检测IP地址是否可用"""
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
        ip_url_next = '://' + ip_address + ':' + ip_port
        proxies = {'http': 'http' + ip_url_next, 'https': 'https' + ip_url_next}
        print(proxies)
        try:
            r = requests.get(self.check_url, headers=header, proxies=proxies, timeout=3)
            html = r.text
            print(html)
        except:
            print('fail-%s' % ip_address)
        else:
            print('success-%s' % ip_address)
            soup = BeautifulSoup(html, 'lxml')
            div = soup.find(class_='well')
            if div:
                print(div.text)
            ip_info = {'address': ip_address, 'port': ip_port}
            self.ip_list.append(ip_info)



    def main(self):
        """主方法"""
        web_html = self.get_html(self.url)
        soup = BeautifulSoup(web_html, 'lxml')
        ip_list = soup.find('tbody').find_all('tr')
        for ip_info in ip_list:
            td_list = ip_info.find_all('td')
            if len(td_list) > 0:
                ip_address = td_list[0].text
                ip_port = td_list[1].text
                print(ip_address, ip_port)
            # 检测IP地址是否有效
            self.get_available_ip(ip_address, ip_port)
        # 写入有效文件
        with open('ip.txt', 'w') as file:
            json.dump(self.ip_list, file)
        print(self.ip_list)


def get_proxy():
    socket.setdefaulttimeout(3)
    f = open("ip.txt")
    lines = f.readlines()
    proxys = []
    for i in range(0, len(lines)):
        ip = lines[i].strip("\n").split("\t")
        proxy_host = "http://" + ip[0] + ":" + ip[1]
        proxy_temp = {"http": proxy_host}
        proxys.append(proxy_temp)

    count = random.randint(0,len(proxys))

    return proxys[count]



# 程序主入口
if __name__ == '__main__':
    get_ip = GetIp()
    get_ip.main()