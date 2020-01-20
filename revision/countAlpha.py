def toList(s):
    li = []
    for i in s:
        li.append(i)
    return li

def num(s):
    li = toList(s)
    l1 = []

    for i in range(0, len(li)):

        count = 0
        if i not in l1:
            for j in range(0, len(li)):
                if li[i] == li[j]:
                    count += 1
                    l1.append(j)
            print(li[i], count)









num("aabbcddea")