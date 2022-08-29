def func():
    print("I am Func")

#没有加（）的func指向的是内存地址，而加了（）的func指向的是返回值
l=[func]
l[0]()

g={"naem":func}
g["naem"]()