
def toList(s):
    li = []
    for i in s:
        li.append(i)
    return li
def alphaList(s):
    li = []
    for i in s:
        if i.isalpha():
            li.append(i)
    return li
def reverseList(s):
    reversedList = ""
    for i in s:
        reversedList = i + reversedList
    return reversedList






def reverse(string):
    ORIGINAL_LIst = toList(string)
    ALPHA_LIST = alphaList(string)
    Reversed_LIST = reverseList(ALPHA_LIST)
    # print(Reversed_LIST)
    count = 0
    for i in range(0, len(ORIGINAL_LIst)):
        if ORIGINAL_LIst[i].isalpha():
            ORIGINAL_LIst[i] = Reversed_LIST[count]
            count += 1
    print("".join(ORIGINAL_LIst))

reverse("ABCD$_")