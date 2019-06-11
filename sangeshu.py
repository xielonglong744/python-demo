numlist = [[2, 5, 6, 3, 6, 9, 8, 4, 1,], [1, 2, 3, 4, 9, 6, 7, 8, 5]]
nums = numlist[1]
lenth = len(nums)
count = 0
count_swap = 0
for i in range(lenth):
    count +=1
    for j in range(lenth-i-1):
        flag = False
        if nums[j] > nums[j+1]:
            tem = nums [j]
            nums[j] = nums[j+1]
            nums[j+1] = tem
            flag = True
            count_swap +=1
    if not flag:
       break
print(nums,count,count_swap)