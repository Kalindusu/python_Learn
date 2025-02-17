# def hello():
#     print("Hello, World!")

# hello()
# def add_numbers(num1, num2):
#     print(num1 + num2)

# add_numbers(2, 3)  # Output: 5


# def multiple_items(*args):
#     print(args)
    

# multiple_items(1, 2, 3, 4, 5)  # Output: (1, 2, 3, 4, 5)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first=1, second=2, third=3)  # Output: {'first': 1, 'second': 2, 'third': 3}