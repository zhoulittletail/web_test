# 提示输入三角形三条边,进行判断三角形类型(等边、等腰、普通)并进行提示，否则提示不是三角形；
#
# 提示：
# 三角形：两边之和大于第三边；
# 等腰三角形：两条边相等
# 等边三角形：三条边相等
a = int(input("请输入第一条边长度："))
b = int(input("请输入第二条边长度："))
c = int(input("请输入第三条边长度："))
if a+b >c and a+c > b and b+c >a :
    if a == b and b ==c:
        print("是等边三角形")
    elif a ==b or b ==c or a==c :
        print("是等腰三角形")
    else:
        print("是普通三角形")
else :
    print("不是三角形")