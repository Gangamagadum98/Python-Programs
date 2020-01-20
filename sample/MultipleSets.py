num1={1,2,4}
num2={4,5,6}

#union of two sets
unionSets=num1.union(num2)
print(unionSets)
#intersection

intersectionSet=num1.intersection(num2)
print(intersectionSet)

diffset=num1.difference(num2)
print(diffset)

diffset=num2.difference(num1)
print(diffset)

#find whether set is subset
issubset=num2.issubset(num1)
print(issubset)

isSuperset=num1.issuperset(num2)
print(isSuperset)

isDisjoint=num1.isdisjoint(num2)
print(isDisjoint)

#doesnt alters the original set
diff=num1.difference(num2)
print(num1)
print(num2)

#alters the original set
Diffset=num1.difference_update(num2)
print(num1)
print(num2)

cars={"Audi","BMW","Ford"}
#shallow copy
cars2=cars
cars2.remove("BMW")
print(cars)

#Deep copy
cars2=cars.copy()
cars2.remove("Audi")
print(cars)
print(cars2)


































































