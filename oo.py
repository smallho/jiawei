import random

length = 8#長度定義為8個字

num = []

for i in range(length):
    temp = random.randint(0,99)#定義數字從1至99隨機選8個字
    num.append(temp)

i = length

while i > 1:
    for j in range(i-1):
         if(num[j] > num[j+1]):#判別前後數字大小 以調整順序
            temp = num[j]
            num[j] = num[j+1]
            num[j+1] = temp
    i -= 1#因為最小的數字已排最後方 所以下一次可以少比較一個數
    num.sort(reverse=True)#上面的是從小排到大 這行是把它倒過來變成大到小

print(num)#印出最後的答案