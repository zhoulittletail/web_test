# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#            if i*100+j*10+k==i**3+j**3+k**3:
#                 print(i*100+j*10+k)
# max_num = int(input('请输入最大范围'))
# # 获取小于指定数的阿姆斯特朗数
# for num in range(0, max_num):
#     sum = 0
#     length = len(str(num))
#     temp = num
#     for i in range(length):
#         sum += (temp % 10) ** length
#         temp //= 10
#     if sum == num:
#         print(num)

# class Shop(object):
#     instance = None
#     isinit = None
#     def __init__(self):
#         if self.isinit == 0:
#             self.price = True
#     def __new__(cls, *args, **kwargs):
#         if cls.instance == None:
#             cls.instance = object.__new__(cls)
#         return cls.instance
# aa = Shop()
# aa.price = 199
# print(aa)
# print(aa.price)
# bb = Shop()
# print(bb)
# print(bb.price)



class Car(object):
    def back(self):
        print("999")
class Bus(Car):
    def back(self):
        print("333")
class Person(object):
    def select(self,obj):
        obj.back()
car = Car()
bus = Bus()
pp = Person()
pp.select(bus)