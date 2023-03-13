# 这个函数是将给输入的三个字符串通过函数的方式连接起来
# 例如eg:
# 系统将提示你依次输入三个字符串
#该程序会先打印一个字符串列表
#然后打印连起来的字符串
def solve_it(L):
    a=''
    for i in L:
        a=a+i

    return a
# list1 是测试数据
list1=["hello","world","python"]
e1=input('please input e1:')
e2=input('please input e2:')
e3=input('please input e3:')
list2=[e1,e2,e3]
print(list2)
print(solve_it(list2))
