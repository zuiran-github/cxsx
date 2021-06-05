import menpiao.zwf_searchSpots
import time
# 如果大部分都是空就不继续查了，每个键值访问都包装在tryexcept里边,把携程改快点，途牛getCityUrl出错
p = 0
list = ['北京','青岛','上海','济南','深圳']
while p < 9:
    t1 = time.time()
    menpiao.zwf_searchSpots.getTicketInfo('方特',list[p%4])
    p = p+1
    t2 = time.time()
    print(t2-t1)


# n = input("111222:")
# city = input('222333:')
n = ''
# while n != 'n':
#     t1 = time.time()
#     print(menpiao.zwf_searchSpots.getTicketInfo(n,city))
#     t2 = time.time()
#     print(t2-t1)
#     n = input("111222:")
#     city = input('222333:')