import math
re=[]
count=0
flag=False
for i in range(2,100000):
    for j in re:
        count +=1
        if i%j == 0:
            flag=True
            break
        if j >= math.ceil(i**0.5):
            flag=False
            break
    if not flag:
        re.append(i)
print(re)
print(count)