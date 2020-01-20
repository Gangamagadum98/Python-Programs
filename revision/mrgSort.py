
def merge(num):
    if len(num) > 1:
        mid = len(num) // 2

        b = num[:mid]
        c = num[mid:]

        merge(b)
        merge(c)

        i = j = k = 0
        while i < len(b) and j < len(c):
            if b[i] > c[j]:
                num[k] = c[j]
                j += 1
            else:
                num[k] = b[i]
                i += 1
            k += 1

        while i < len(b):
            num[k] = b[i]
            i += 1
            k += 1
        while j < len(c):
            num[k] = c[j]
            j += 1
            k += 1

        return num










num = [4, 1, 9, 2, 5, 3, 8, 6]
res = merge(num)
print(res)