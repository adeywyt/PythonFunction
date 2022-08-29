# 局部变量:
def name_bl():
    a=520
    print(a)
print(name_bl())
print("")


# global语句
x=1314
def myfunc():
    global x
    x=520
    print("x等于%s"%x)
a=myfunc()
print(a)
print("")


# 函数的嵌套(重点)：
def name_age1():
    x=520
    def name_age2():
        x=800
        print("naem_age2 x is %s"%x)
    print(name_age2())
    print("name_age1 x is %s"%x)
print(name_age1())
print("")




def name_age1():
    x=520
    def name_age2():
        nonlocal x  # 在这里声明x为全局变量
        x=800   # 在这里修改了外部的x是数字.
        print("naem_age2 x is %s"%x)
    print(name_age2())
    print("name_age1 x is %s"%x)
print(name_age1())