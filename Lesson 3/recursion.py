def add_one(num):

    if(num >= 9):
        return num +1
    
    total = num +1
    print(total)

    add_one(total)

mynewnum = add_one(0)

print(mynewnum) # Output: 10

# Compare this snippet from Lesson%203/conditionals.py:
# value=5
#
# if value == 5:
#     print("Value is 5")
