# 收集参数
def myfunc(*argparse):
    print("有{}个参数".format(len(argparse)))
    print("第1个参数是{}".format(argparse[0]))
    print("第2个参数是{}".format(argparse[1]))


print(myfunc(7, 8, 9, 4, 5, 6, 5, 8))
print("")


# 收集参数和参数
def myfunc1(*age, a, b):
    return print(age, a, b)


name = myfunc1(1, 2, 3, 4, 5, 6, a=520, b=1314)
print(name)
print("")


# 收集参数存储为字典
def myfunc2(**go):
    return print(go)


print(myfunc2(a=1, b=2, c=3))
print("")


# 收集参数：[位置参数，元组，字典]
def myfunc2(a, *b, **c):
    return print(a, b, c)


print(myfunc2(123, 1, 2, 3, 4, 5, 6, x=520, y=520))
print("")

# 解包[元组]：
tulp = (1, 2, 3, 4)


def myfunc3(a, b, c, d):
    return print(a, b, c, d)


print(myfunc3(*tulp))  # 在传递参数是前面加*表示解包.然后在传递.
print("")

# 解包[字典]：
syte = {"a": 1, "b": 2, "c": 3, "d": 4}


def myfunc4(a, b, c, d):
    return print(a, b, c, d)


print(myfunc4(**syte))
