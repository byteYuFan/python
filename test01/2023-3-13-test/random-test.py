# this file is make some random num
#生成一个1000-9999的num
#random.randint(a,b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

import math
import random
print(math.e)
num=random.randint(1000,9000)
q_num=num//1000
b_num=num//100%10
s_num=num//10%10
g_num=num%10
reserve_num=g_num*1000+s_num*100+b_num*10+g_num
print(num)
print(reserve_num)
