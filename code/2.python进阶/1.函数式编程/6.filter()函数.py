
# 请利用filter()过滤出1~100中平方根是整数的数，
# 即结果应该是：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

import math

def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x
print filter(is_sqr, range(1, 101))