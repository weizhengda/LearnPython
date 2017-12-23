# dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，
# 这样，我们迭代的就是 dict的每一个 value

# dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样

# 请计算所有同学的平均分。

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for v in d.itervalues():
    sum = sum + v
print sum / len(d)


