
def selection_sort(n):
    for i in range(0, len(n)):
        for j in range(i+1, len(n)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums















nums = [3, 6, 1, 9, 2,8, 4]
selection_sort(nums)
print(nums)