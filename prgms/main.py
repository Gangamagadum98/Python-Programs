# import test
# print(__name__)
#If we r executing in the same file than (__name__) vl print as (__main__), but if we r import file from another module
# In that module is(__name__) is present then it vl display the file name not (__main__)


def func():
    print("Hello")
    print("Hi")

if __name__=="__main__":    # if you want to print only this file add this condition, if another file imports this file also it won't display msg from this file
    func()

