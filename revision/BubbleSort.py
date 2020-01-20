def bubbleSort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(0, i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums










nums = [2, 1, 9, 4, 3, 8]
num = bubbleSort(nums)
print(num)