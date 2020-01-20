import os


file=open("/home/redintegro/Desktop/write.txt","w")             #write
file.write("Hi")

file=open("/home/redintegro/Desktop/write.txt","a")                #append
file.write("Hi")

file=open("/home/redintegro/Desktop/write.txt","r")                 #read
print(file.read())

os.mkdir("/home/redintegro/Desktop/folder")                         # create folder



file.close()


os.remove("/home/redintegro/Desktop/write.txt")                     #delete file
# os.removedirs("/home/redintegro/Desktop/textfile")                 
os.rmdir("/home/redintegro/Desktop/textfol")                         # delete directory