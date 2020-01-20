

def insertion(num, x, pos):
    b = []
    if pos <= len(num):
        for i in range(0, len(num)):
            if i == pos:
                num[i] = x
            else:
                b = num
        return b












num = [4, 5,1, 3,8]
x=7
pos=3
res = insertion(num, x, pos)
print(res)