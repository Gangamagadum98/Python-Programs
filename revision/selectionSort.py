
def sort(nums):
    for i in range(len(nums)):

        minpos = i
        for j in range(i, len(nums)):
            print(j)
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp







nums = [4,1,9,3,2]
sort(nums)
print(nums)