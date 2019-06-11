import random
def double_value(*nums):
    print(nums)
    return max(nums), min(nums)
print(*double_value(*[random.randint(10,20) for  i in range(10)]))

def show(n):
    tail = " ".join([str(i)for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n):
        print("{:>{}}".format(" ".join([str(j)for j in range(i,0,-1)]),width))
    print(tail)
show(12)
def show(n):
    tail = " ".join([str(i)for i in range(n,0,-1)])
    print(tail)
    width = len(tail)
    for i in range(n-1,0,-1):
        print("{:>{}}".format(" ".join([str(j)for j in range(i,0,-1)]),width))
show(12)

def showtail(n):
    tail = " ".join([str(i)for i in range(n,0,-1)])
    print(tail)
    for i in range(len(tail)):
        if tail[i] == " ":
            print(' '*i,tail[i+1:])
    print(len(tail))
showtail(12)