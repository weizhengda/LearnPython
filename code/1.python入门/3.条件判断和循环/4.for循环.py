# 班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：
# L = [75, 92, 59, 68]
# 请利用for循环计算出平均成绩。

L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum = sum + score
print sum / 4