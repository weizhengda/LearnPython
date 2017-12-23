# L = ['Adam', 'Lisa', 'Bart']
# 但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。
# 请通过对list的索引赋值，生成新的排名。

L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
L[-1] = 'Adam'
print L