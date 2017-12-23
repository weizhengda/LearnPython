
# 在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。
# 请用for循环迭代数列 1-100 并打印出7的倍数。

for i in range(1,101):
    if i % 7 == 0:
        print i