
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            print(i)
            print(j)
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp




nums = [5,3, 8,6,7,2]       # [5,3,8,6,2,7] j=4

sort(nums)
print(nums)