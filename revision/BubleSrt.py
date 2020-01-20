
def bubble_sort(num):
    for i in range (len(num)-1, 0, -1):
        for j in range(i):
            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

    return num







nums = [4, 8, 1, 9, 2, 5, 3]
res = bubble_sort(nums)
print(res)