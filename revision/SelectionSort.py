
def selection(s):
    for i in range(0, len(s)):
        min = i
        for j in range(i+1, len(s)):
            if s[min] > s[j]:
                temp = s[min]
                s[min] = s[j]
                s[j] = temp
    return s








s=[3,9,1,4,2,1,45,0,50,2]
res = selection(s)
print(res)