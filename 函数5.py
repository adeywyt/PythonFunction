def fun():
    x = 800

    def fun1():
        print(x)

    return fun1


print(fun())
print(fun()())  # 获取fun1的返回结果
name = fun()  # 将fun赋值给name
print(name())  # 输出name的数值
print("")


# 闭包
def fun2(exp):
    def fun3(base):
        return base ** exp

    return fun3


na_me1 = fun2(2)  # na_me1指向exp参数时exp是2
ch_ub1 = fun2(3)  # ch_ub1指向exp参数时exp是3
print(na_me1(5))  # 这里我们进行调用na_me时base为我们传过去的传输5，所以是5**2
print(ch_ub1(5))  # 这里我们进行调用ch_ub1时base为我们传过去的传输5,所以是5**3
print("")


# 装饰器
def myfunc():
    print("正在调用myfunc函数....")


def report(func):
    print("开始调用函数....")
    func()
    print("函数调用完成....")


print(report(myfunc))


