
def linearSearch(nums, x):
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

index = linearSearch([3, 5, 6, 9, 2], 9)
if index == -1:
    print("element is not foound in the array")
else:
    print("the index of element is ", index)



