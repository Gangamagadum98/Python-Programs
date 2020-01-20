
file = open("/home/redintegro/Desktop/test.txt")                        # (or use \\)
# print(file.read())              # it reads entire file
# print(file.readline())            # it reads one line  
# print(file.readlines())             # it reads all lines in file

# for i in range(4):
#     print(file.readline())  
# print(file.read(22))                  # to read half of the line

# file.seek(38)
# print(file.read(24))
file.seek(67)
print(file.read(3))
file.close()