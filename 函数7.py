# import time
# def func(group,s):
#     print("欢迎来到王者荣耀")
#     print(f"你出身在{group}方阵营")
#     print(f"德军还有{s}达到战场")
#     time.sleep(s)
#     print("全军出击")
# def func1():
#     start=time.time()
#     func("蓝色",s=5)
#     stop=time.time()
#     print(start-stop)
# func1()

# import time
# def func(group,s,z):
#     print("欢迎来到王者荣耀")
#     print(f"你出身在{group}方阵营")
#     print(f"德军还有{s}达到战场")
#     time.sleep(s)
#     print(f"{z}全军出击")
# def func1(*x,**y):
#     start=time.time()
#     func(*x,**y)
#     stop=time.time()
#     print(start-stop)
# func1("蓝","4","双方出击")




# import time
# def func0(group,s,z):
#     print("欢迎来到王者荣耀")
#     print(f"你出身在{group}方阵营")
#     print(f"德军还有{s}达到战场")
#     time.sleep(s)
#     print(f"{z}全军出击")
#
#
# def func2(func):
#     def func1(*x,**y):
#         start=time.time()
#         func(*x,**y)
#         stop=time.time()
#         print(start-stop)
#     return func1
#
# res=func2(func0)
# res("蓝色",s=3,z="双方")


import time
def phone(num):
    for i in range(101):
        time.sleep(0.05)
        print(f"\r当前电量：{'▊'*i} {i}%",end=" ")
    print("电量已充满！")
phone(20)









































