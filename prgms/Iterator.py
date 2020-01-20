# Iterator vl done by using 2 methods
# 1. __iter__  -> It vl gv no of iterator obj 2. __next__ -> It vl giv next elem
# __next__() is there inside __iter__() - it knws the i value tha's y it gives next value

# inbuilt object  list doing iterator

nums=[7,8,9,5]
it = iter(nums)
print(it.__next__())
print(next(it))
for i in nums:
    print(i)

#
class TopTen:

    def __init__(self):
        self.num = 1        # counter

    def __iter__(self):
        return self

    def __next__(self):

        if self.num<=10:
            val =self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values=TopTen()

print(next(values))  # Once u got values here it vl not print values in for loop again
for i in values:
    print(i)