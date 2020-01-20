marks=int(input("enter your marks"))
if marks>=85 and marks<=100:
    print("Congrats you scored grade A")
elif marks>=60 and marks<85:
    print("congrats you scored grade B")
elif marks>=35 and marks<60:
    print("You are just pass")
else:
    print("Sorry! you are failed")