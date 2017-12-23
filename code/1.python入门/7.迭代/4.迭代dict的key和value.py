
# 请根据dict：打印出 name : score，最后再打印出平均分 average : score。

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k,":", v
print 'average', ':', sum / len(d)