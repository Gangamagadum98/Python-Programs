# In iterator to fetch one by one value bt here v should use 2 method
# Generator vl give iterator
# if u r fetching 1000 of record from db .bt u want only one by one record to work that time generator vl use.


def topten():

    n=1
    while n<=10:
        sq=n*n
        yield sq        # yield is same as return, bt return terminate immediately yield not
        n=n+1





values = topten()
# print(values.__next__())

for i in values:
    print(i)
