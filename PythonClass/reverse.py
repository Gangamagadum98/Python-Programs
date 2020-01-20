# from collections import Counter
# s1 = "abcdaeabdcez"
# print(Counter(s1))
# s2 = s1.split(',')
# print(s2)
# print(len(s2))
# count = 0
# # for i in range(0, len(s2)):
# #     for j in range(i+1, len(s2)):
# #         if s2[i] == s2[j]:
# #             print(s2[i])
# for i in range(0, len(s2)):
#     for j in range(i+1, len(s2)):
#
#         if s2[i] == s2[j]:
#             count+=1
#
#             print(s3,':',count)
            # b=[]
            # b.append(s2[i])
            # print(b)






    # for j in range(i+1, len(s2)):
    #     print(i)
    #     print(j)
    #     if s1[i] == s1[j]:
    #         print(s1[i])
    #         count += 1
    # print(s1[i], ":", count)

#

stri = 'abcdaeabdcez'
l1 = list(stri)
a = []
for i in range(0, (len(l1))):
    count = 0
    if i not in a:
        for j in range(0, len(l1)):
            if l1[i] == l1[j]:
                count = count + 1
                a.append(j)
        print(l1[i], ':', count)
