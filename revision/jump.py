import math
def jump(a, num):
    n = len(li)
    prev = 0
    step = math.sqrt(n)

    while a[int(min(step, n-1))] < num:
        prev = step
        step += math.sqrt(n)

        if prev >= n:
            return -1

    while a[int(prev)] < num:
        prev += 1

        if prev == min(step, n):
            return -1

    if a[int(prev)] == num:
        return prev

    return -1




li = [1, 2, 3, 4, 5, 6,7 , 8, 9, 10, 11, 12, 13, 14, 15, 16]
num = 15
index = jump(li, num)
if index == -1:
    print("not found")
else:
    print(int(index))