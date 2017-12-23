
# 函数 move(n, a, b, c) 的定义是将 n 个圆盘从 a 借助 b 移动到 c。

def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')