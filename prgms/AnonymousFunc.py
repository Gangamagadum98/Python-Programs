from functools import reduce
# anonymous func dont have function name takes only args and one expression
f= lambda a,b:a+b
result = f(5,6)
print(result)

#finding even no's using lambda (filter() filters the unwanted value)

nums=[2,4,5,6,3,6,10]
evens = list(filter(lambda n:n%2==0, nums))
print(evens)

#doubles using map (use map when u want to change every val)

doubles = list(map(lambda n:n*2, evens))
print(doubles)

#reduce values by adding all values using reduce ()

sum = reduce(lambda a,b:a+b, doubles)
print(sum)

#list(filter) is used for i want result in list.