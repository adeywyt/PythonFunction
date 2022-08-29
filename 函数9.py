def func(i):
    if i > 0:
        print("I am Wyt")
        i -= 1
        func(i)


func(10)


def func1(n):
    if n == 1:
        return 1
    else:
        return n * func1(n - 1)


print(func1(10))


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(fib(12))

def hanoi(n,x,y,z):
    if n == 1:
        print(x,"==>",z)
    else:
        hanoi(n-1,x,z,y)
        print(x,"==>",z)
        hanoi(n-1,y,x,z)

n=int(input("请输入汉诺塔的层数字:"))
hanoi(n,"A","B","C")