# 定义函数
def myfunc():  #这里定义了个myfunc函数
    for i in range(10):
        print("我是%s" % i)
        print("第%s次" % i)


myfunc()
print("")


# 函数参数
def print_time(name, password):
    print("你的用户是%s" % name)
    print("你的密码是%s" % password)


user = print_time("wyt", "123456")
print("")


# 返回结果
def div(x, y):
    return x / y


a = div(4, 2)
print(a)

print("")


# 返回return
def ho(x, y):
    if y == 0:
        return "除数不能为0"
    else:
        return x / y


print(ho(4, 0))
print(ho(4, 2))
