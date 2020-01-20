samosa=5

while samosa!=0:
    print("eating samosa")
    samosa=samosa-1

petrol=10

while petrol!=0:
    print("reduced")
    petrol=petrol-1

number=10
while number!=0:

    if number%2==0:
         print("even number",number)
    else:
        print("odd number",number)
    number=number-1

fruits=["Mango","Apple","Banana","Orange","Grapes"]
for fruit in fruits:
     print(fruit)

numbers=[10,20,30,40,50,60]
for num in range(2,5):
    print(numbers[num])

person=[{"name":"Manasa","id":1},{"name":"Anusha","id":2}]
for persons in person:
    print(persons.get("name"))

users=[{"name":"s","id":1,"Tshirts":["Levis","Adidas","Ucb"]},{"name":"n","id":2,"Tshirts":["wrogn","allensooly","Puma"]}]
for user in users:
    print(user.get("Tshirts"))







