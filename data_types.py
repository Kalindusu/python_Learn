#string data type
# literal asssignment

first = "hello"
last = "world"

# print(type(first))
# print(first + last)
# print(type(first)==str)
# print(isinstance(first,str))

#constructor function

# pizza = str("pepperoni")
# print(pizza)

fullname=first + " " + last
print(fullname)

fullname+="!"
print(fullname)

#casting a number to a string

age = 20
age = str(age)
print(type(age))

print(age)

#multiple lines

multiline= '''
This is a multiline string
with multiple lines
'''

print(multiline)\

#escaping special characters
sentence='I\'m a programmer\nI\'m learning python\\I\'m enjoying it'
print(sentence)

#string methods

print(fullname.upper())
print(fullname.lower())
print(fullname.title())
print(fullname.strip())

print(fullname.replace('hello','hi'))

