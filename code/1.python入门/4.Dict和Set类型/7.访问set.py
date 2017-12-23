# 由于set存储的是无序集合，所以我们没法通过索引来访问。
# 访问 set中的某个元素实际上就是判断一个元素是否在set中。

s = set(['Adam', 'adam', 'Lisa', 'lisa', 'Bart', 'bart', 'Paul', 'paul'])
print 'adam' in s
print 'bart' in s