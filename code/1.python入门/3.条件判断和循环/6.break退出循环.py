# 利用 while True 无限循环配合 break 语句，计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。

sum = 0
x = 1
n = 1
while True:
    sum = sum + x
    x = x * 2
    n = n + 1
    if n > 20:
        break
print sum