pos = 0
def search(l1, x):

    for i in range(0, len(l1)):
        if l1[i] == x:
            globals() ['pos'] = i + 1

    return pos











l1 = [4, 9, 2, 8, 1, 6, 5]
x = 5
res = search(l1, x)
print(res)