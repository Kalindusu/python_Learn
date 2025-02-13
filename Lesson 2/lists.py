users=['Kalindu','Kasun','Kamal','Kasuni']

data=['kalindu',42,True]

emptylist=[]

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Kasun'))

print(users[0:2])
print(users[1:])


print(len(data))

users.append('Kasuni')
print(users)

users+=['Nimal']
print(users)

users.extend(['Sunil','Kamal'])
print(users)

# users.extend(data)
# print(users)

users.insert(2,'Bob')
print(users)

users[3:4]=['Anna','sarawan','sudaraka','saman']
print(users)

users[1:3]=['Robe','jpa']
print(users)

users.remove('Kalindu')
print(users)

users.pop()
print(users)

del users[0]
print(users)

#del data
data.clear()
print(data)
