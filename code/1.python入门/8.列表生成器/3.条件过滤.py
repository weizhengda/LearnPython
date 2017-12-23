
# 利用 if 剔除掉非字符串的元素。

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello', 'world', 101])