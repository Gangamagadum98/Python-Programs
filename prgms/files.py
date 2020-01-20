f1 = open('mydata.txt')
# print(f1.read())
# print(f1.readline())

f2 =open('message.txt','w')
for data in f1:
    print(data)
    f2.write(data)


#image
f3 = open('sample.jpg','rb')

f4 = open('mypic.jpg','wb')
for i in f3:
    f4.write(i)