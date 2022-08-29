# lambda表达式：
ano = lambda y: y * y
print(ano(5))

y = [lambda x: x * x, 2, 3, 4, 5, 6]
print(y[0](4))

mappend = map(lambda x: ord(x) + 10, "LoveWyt")
print(list(mappend))
# 这里会将"LoveWyt"的每个字符转换成数字并且加10.返回列表格式


filtero = list(filter(lambda x: x % 2, range(20)))
print(filtero)
