# trying to without altering numeric

def isAlphabate(x):
    return x.isalpha()

def tolist(s):
    li = []
    for i in s:
        li.append(i)
    print(li)
    return li
def alphaList(s):
    li = []
    for i in s:
        if i.isalpha():
            li.append(i)
    print(li)
    return li
def reverseAlphabates(ALPHA_LIST):
    revstr = ""
    for i in range(0, len(ALPHA_LIST)):
        revstr = ALPHA_LIST[i] + revstr
    return revstr

def reverse(string):
    ORIGINAL_LIST = tolist(string)
    ALPHA_LIST = alphaList(string)
    REVERSEDSTRING = reverseAlphabates(ALPHA_LIST)
    print(REVERSEDSTRING)
    REVERSEDLIST = tolist(REVERSEDSTRING)
    count = 0
    for i in range(0, len(ORIGINAL_LIST)):
        if ORIGINAL_LIST[i].isalpha():
            ORIGINAL_LIST[i] = REVERSEDLIST[count]
            count+=1
    print("". join(ORIGINAL_LIST))
reverse("ASD#2")

