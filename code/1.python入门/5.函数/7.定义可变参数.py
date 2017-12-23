
# 如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数
# 可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数

# 请编写接受可变参数的 average() 函数。

def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
