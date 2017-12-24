
# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。

def calc_prod(lst):
    def lazy_prod():
        def f(x,y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod

f = calc_prod([1, 2, 3, 4])
print f()