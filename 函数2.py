# 位置参数
def myfunc(s, vt, o):
    return " ".join((o, vt, s))


print(myfunc("You", "Love", "Python"))
print("")


# 关键字参数
def myfunc1(a, b, c):
    return a + b + c


print(myfunc1(a=3, b=3, c=5))
print("")


# 位置参数必须在关键字参数之前：
def myfunc2(a, b, c):
    return a + b + c


print(myfunc2(5, b=14, c=16))
print("")


# 默认参数
def myfunc3(a, b, c=2):
    return a + b + c


print(myfunc3(1, 2))  # 没有传递c的参数，则使用默认参数
print(myfunc3(1, 1, 1))  # 进行传递c的参数，c=1

# 冷知识:
# [限制位置参数]可以使用/进行位置参数的限制
# /的左边只能说位置参数
try:
    def abs(a, /, b, c):
        print(a, b, c)


    print(abs(1, 2, 3))
    # print(abs(a=2,b=3,c=4))  #这个则会报错.
except:
    print("a只能是位置参数，不可以是关键字参数")

# [限制关键字参数]可以使用*进行关键字参数的限制
# *的右边只能是关键字参数

try:
    def abs(a, *, b, c):
        print(a, b, c)


    print(abs(1, b=121, c=14))
except:
    print("a的右边只能说关键字参数，不可以是位置参数")
