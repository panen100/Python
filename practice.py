name = 'coral'
age = 20
score = 99.8

print("个人信息:",name,age,score)

# 格式化输出
print("个人信息：%s %d %.2f" % (name,age,score))
print("个人信息：{} {} {}".format(name,age,score)) # format函数
print(f"个人信息：{name} {age} {score}")  # f-string输出

# .py源代码 ---> 自动编译 ---> .pyc字节码 ---> 解释器（PVM） ---> 逐行执行
