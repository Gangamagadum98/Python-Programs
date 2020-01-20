
def selectn(num, x, pos):
    b = []
    if pos <= len(num):

        for i in range(0, len(num)):
            if pos == i:
                num[i] = x
            else:
                b = num
        return b








num = [5, 1, 9, 4, 1, 2, 7]
x = 6
pos = 4
res = selectn(num, x, pos)
print(res)