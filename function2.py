m_list = [1, 9, 8, 5, 6, 7, 4, 3, 2]
nums = [0] + m_list
for i in range(2,len(nums)):
    nums[0] = nums[i]
    j = i - 1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = nums[0]
del nums[0]
print(nums)

lst = [2, 5, 6, 9, 86, 3, 25, 6, 3, 21, 4, 2]
def sort(lst,fn=lambda a,b :a < b):

    newlst = []
    for x in lst:
        for i,y in enumerate(newlst):
            if fn(x, y):
                newlst.insert(i,x)
                break
        else:
            newlst.append(x)
    return newlst
print(sort(lst))

print(list(map(lambda x :x + 1, lst)))
print(list(filter(lambda x:x>3 ,lst)))
