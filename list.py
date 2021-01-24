import random
pop = 8
num=[]
for i in range(pop):
    temp = random.randint(0,99)
    num.append(temp)

i = pop
num.sort(reverse=True)
print(num)
