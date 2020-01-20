import json

user='{"name":"xyz","job":["python","js","java"]}'
dict=json.loads(user)
test = dict['job']
# print(test[0])


users = '{"name":"Angular","rating":"5","languages" :[{"name":"python", "rating":"5"},{"name":"js","rating":"4"}]}'
dict = json.loads(users)
test = dict['languages']
print(type(test))
print(test)

#print(tests.name)
for key, value in dict.items():
    print((value.keys()))