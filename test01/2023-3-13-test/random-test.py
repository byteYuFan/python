# this file is make some random num
# 生成一个1000-9999的num
# random.randint(a,b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

import math
import random
# reserve_1
def reserve_1(num):
    q_num = num // 1000
    b_num = num // 100 % 10
    s_num = num // 10 % 10
    g_num = num % 10
    reserve_num = g_num * 1000 + s_num * 100 + b_num * 10 + g_num
    return reserve_num
# reserve_2
def reserve_2(num):
    num=str(num)
    reserve_num=""
    for i in num:
        reserve_num = reserve_num=i+reserve_num

    reserve_num=int(reserve_num)
    return reserve_num

num = random.randint(1000, 9000)

print("反转前",num)
print("reserve_1反转后",reserve_1(num))
print("reserve_2反转后",reserve_2(num))
