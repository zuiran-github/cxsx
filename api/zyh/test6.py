def tri(A, B, C):

    a = min(A, B, C)                            # 1
    b = (A+B+C) - min(A,B,C) - max(A,B,C)       # 2
    c = max(A, B, C)                            # 3

    if (a+b) <= c:                              # 4
        print("error")                          # 5
    else:                                       # 6
        l = a+b+c                               # 7
        print("周长为{}".format(l))              # 8
        if a == b:                              # 9
            if b == c:                          # 10
                print("等边三角形")              # 11
            else:                               # 12
                print("等腰三角形")              # 13
        else:                                   # 14
            if b == c:                          # 15
                print("等腰三角形")              # 16


# tri(1,1,1)
# tri(1,1,2)
# tri(3,3,4)
# tri(3,4,4)
# tri(3,4,5)


import math
def week(year, month, day):
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]     # 1
    if year%4 == 0 :                                            # 2
        list[1] = 29                                            # 3

    count = 0                                                   # 4
    for i in range(month-1):                                    # 5
        count += list[i]                                        # 6

    count += day                                                # 7

    c = math.floor((year-1)/4)                                  # 8
    count += c*366 + (year-1-c)*365                             # 9
    r = count % 7                                               # 10

    if r==0:                                                    # 11
        # print("星期天")                                          # 12
        return "星期天"
    else:                                                       # 13
        # print("星期{}".format(r))                                # 14
        return "星期{}".format(r)

# week(1,1,1)
# week(1,1,31)
# week(1,2,1)
# week(1,2,28)
# week(1,3,1)
# week(1,4,1)
# week(2,1,1)
# week(3,1,1)
# week(4,1,1)
# week(5,1,1)
# week(1980,6,5)
# week(2001,1,1)
# week(2021,5,26)
# week(2021,1,1)
# d=week(2000,12,1)
# week(2021,4,28)
# print(d)


import unittest

class MyTests(unittest.TestCase):
    # def test_print(self):
    #     print("test1")
    #
    # def test_print2(self):
    #     print("test2")
    #
    # def atest_print3(self):
    #     print("test3")

    def test_week(self):
        self.assertEqual(week(2000,1,1), "星期天")
        self.assertEqual(week(2021,4,28), "星期4")
        self.assertEqual(week(1,1,1), "星期1")


if __name__ == "__main__":
    unittest.main()




