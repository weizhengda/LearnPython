# 由于 set 也是一个集合，所以，遍历 set 和遍历 list 类似，都可以通过 for 循环实现。
# 直接使用 for 循环可以遍历 set 的元素

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ':', x[1]