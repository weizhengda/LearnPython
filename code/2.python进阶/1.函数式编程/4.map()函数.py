
# 假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，
# 请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list


def format_name(s):
    return s[0].upper() + s[1:].lower()

print map(format_name, ['adam', 'LISA', 'barT'])