
# 利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121

print [100 * n1 + 10 * n2 + n3 for n1 in 
range(1, 10) for n2 in range(10) for n3 in range(10) if n1==n3]