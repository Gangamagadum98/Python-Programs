sports={"cricket","chess"}
#add one elem
sports.add("kabaddi")

for sport in sports:
    print(sport)

#add multiple ele
sports.update(["hockey","boxing"])
print(sports)

#sports.remove("kabaddi")
#sports.remove("shuttle")
#sports.discard("boxing")
print(sports)

sports.pop()
print(sports)

sports1={"cricket","football","chess"}
print(sports1)

#remove
sports1.remove("football")
print(sports1)

#add
sports1.add("Tennies")
print(sports1)

sports1.clear()
print(sports1)

del sports1
print(sports1)

