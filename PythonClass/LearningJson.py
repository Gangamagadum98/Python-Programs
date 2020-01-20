import json

# converting json to dictionary

user = '{"email":"sneha@gmail.com", "password":"pass"}'

dict=json.loads(user)

print(type(dict))
print(type(user))


# converting dictionary to json

dictionary = {'name':'Ganga','mob':'9067787678'}
json1 = json.dumps(dictionary)
print(json1)
print(type(json1))

# converting list to json

list= ['harish',78,'chaitra']

lists = json.dumps(list)
print(lists)

num=67
print(json.dumps(num))

t=('23','34','12',90)
print(json.dumps(t))