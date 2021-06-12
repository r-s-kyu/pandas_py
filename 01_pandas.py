# %%

#-*- using:utf-8 -*-
import time
import pandas as pd
import numpy as np
from sympy import sieve


# 素数を含めたある範囲の数の1以外の最小の約数を列挙
start = time.time()
def make_divisors(n):
    i = 2
    num = 0
    while i <= n:
        if n % i == 0:
            num = i
            break
        i += 1
        if i*i > n:
            num = n
            break
    return num

a = []
for i in range(2,1000001):
    # print(make_divisors(i))
    a.append(make_divisors(i))   
 


rest = time.time() -start
print(rest)
s = pd.DataFrame({
    "Num":np.arange(2,1000001),
    "yakusu":np.array(a)
})


df_s=s.sort_values(["yakusu","Num"], ascending=False)
# df_s=s.sort_values(["Num","yakusu"], ascending=False)
df_s


print(list(df_s["yakusu"])[210000])
print(list(df_s["yakusu"])[210001])
print(list(df_s["Num"])[210000])
print(list(df_s["Num"])[210001])


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# %%

# 素数を除外して判定
#-*- using:utf-8 -*-
import time
import pandas as pd
import numpy as np
from sympy import sieve

start = time.time()

def makeMinDiv(n):
    i = 2
    if n in sieve:
        minDev = n
    else:
        while i <= n:
            if n % i == 0:
                minDev = i
                break
            i += 1
    return minDev    

minArr = np.array([],dtype=np.int)
for i in range(2,1000001):
    # print(makeMinDiv(i))
    np.append(minArr,[makeMinDiv(i)])
print("finish!")

rest = time.time() -start
print(rest)

s = pd.DataFrame({
    "Num":np.arange(2,1000001),
    "yakusu":np.array(a)
})


df_s=s.sort_values(["yakusu","Num"], ascending=False)
# df_s=s.sort_values(["Num","yakusu"], ascending=False)
df_s


print(list(df_s["yakusu"])[210000])
print(list(df_s["yakusu"])[210001])
print(list(df_s["Num"])[210000])
print(list(df_s["Num"])[210001])


elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")































