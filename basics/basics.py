# Java -> Python Practice Sheet Solutions (Flask-ready)
# Each section starts with the original question (as comment) followed by your solved code.
# I kept your explanatory comments intact and uncommented the actual code lines so this file is runnable.

# -----------------------------------------------------------------------------
#if you are having issue in understanding any q or its code , just paste to gpt and ask
# Q1. Python me 3 variables banao:
# - name = "Krishna"
# - age = 20
# - isActive = True
# Aur print karna hai:
# My name is Krishna, age is 20, active = True

# #how to print the string and othher variables .
name = 'Krishna'
age = 20
isActive = True
# unlike java , yahan pe directly concatenate karke print nhi kar sakte , ese f ke andar poori string daal ke uske vairbles ko daalna padta hai , flask main bhi ese hi use hota hai .
print(f"My name is {name}, age is {age}, active = {isActive}")

# -----------------------------------------------------------------------------
# Q2. Java ki tarah do variables swap karo BUT in one line.

# swap example (one-line swap)
a = 5
b = 10
# before swap
print("Before swap:", a, b)
# swap in one line (pythonic)
a, b = b, a
# after swap
print("After swap:", a, b)

# -----------------------------------------------------------------------------
# Q3. List banao: [10, 20, 30]
# Add -> 40
# Remove -> 20
# Print -> first element

# list ( java arraylist Equivalent)
nums = [10, 20, 30]
# putting the first elements already done above
nums.append(40)  # appending the element
# remove element by value
nums.remove(20)  # remove the element , takes the element to be removed
# accessing the element (first)
print("Q3 - first element:", nums[0])

# -----------------------------------------------------------------------------
# Q4. Loop through list and print every element.

# loop through list and print every element
# list index starts from the 0
nums = [1, 2, 3, 4, 5]
for i in nums:  # here i is not index , it is the value in the data structure
    print(i)

# -----------------------------------------------------------------------------
# Q5. List comprehension: nums=[1,2,3,4,5] se output banao [2,4,6,8,10]

nums = [1, 2, 3, 4, 5]
# using list comprehension to double each element
nums2 = [i * 2 for i in nums]
for i in nums2:
    print(i)

# -----------------------------------------------------------------------------
# Q6. Dict banao:
# user = {"name": "Krishna", "age": 20}
# - Add key "city": "Delhi"
# - Print "name"
# - Update "age": 21
# - Delete "city"

# Dictionaries (java hashmap equivalent)- MOST IMPORTANT
user = {'name': "krishna", 'age': 20}
# iterate keys
for i in user:
    print(i)  # i traverses over the keys only , not their values

# iterate values
for i in user.values():  # this prints the whole values only
    print(i)

# iterate key, value
for k, v in user.items():  # this prints both the keys and the values of dict
    print(k, v)

print(user['name'])  # print a particular key's value
user['age'] = 21  # update the value of a key
print(user['age'])

del user['age']  # delete a key by its key
print(user)  # print the whole dict

# -----------------------------------------------------------------------------
# Q7. JSON simulate:
# product = {'id':1, 'name':'Phone', 'price':1000}
# Print -> "Phone costs 1000"

# JSON simulate
product = {
    'id': 1,
    'name': "phone",
    'price': 1000
}

print(product['name'], 'costs', product['price'])  # this is how we print

# -----------------------------------------------------------------------------
# Q8. Nested dict:
# data = {"user": {"name":"Krishna","skills":["Java","Python"]}}
# Print "Python"

# nested list (flask main request.json isi format ka hota hai)
data = {
    "user": {
        "name": "k",
        "skills": ["j", "p"]
    }
}

print(data["user"]["skills"][1])  # data["user"] -> inner dict , ["skills"]->list , [1] -> second item of list ( 0 indexed)

# -----------------------------------------------------------------------------
# Q9. Function banao: def add(a, b): return a + b

# functions (java method ka python  version )
def add(a, b):
    # ese banta hai function , no return type
    return a + b

print("Q9 add(4,5)=", add(4, 5))  # calling the function

# -----------------------------------------------------------------------------
# Q10. Function that accepts a dict and prints "Krishna is 20"

def p(user):  # we can pass a dict too to the function
    print(user["name"], " is ", user["age"])

user = {"name": "krishna", "age": 20}
p(user)  # just pass the dict to the function

# -----------------------------------------------------------------------------
# Q11. Function that returns sum of all numbers in a list

def sum_list(user):
    summ = 0
    for i in user:
        summ += i
    return summ

user_nums = [1, 2, 3, 4, 5]
print(sum_list(user_nums))

# -----------------------------------------------------------------------------
# Q12. File handling: write 'Hello World' to data.txt, then read and print it.

# file handling
with open("data.txt", "w") as f:  # write mode
    f.write("Hello World")

with open("data.txt", "r") as f:  # "r" is read mode  , "with" file will be auto closed
    data = f.read()  # f.read poori file read kargea
    print(data)

# -----------------------------------------------------------------------------
# Q13. Try to access list index 10 and catch exception -> print "Index error"

user = [1, 2, 3, 4]
try:
    print(user[9])  # risky code
except IndexError:  # here this "IndexError" is the exact error that can by caused by that risky line
    # but how will you know , what exact name of excption is and put it at the place , best method is to first run your code and then get the error name and then put it here
    print("indx err")  # handle

# -----------------------------------------------------------------------------
# Q14. Given dict mp = {"a":1}, try to read mp["b"] and handle KeyError

mp = {"a": 1}
try:
    print(mp["b"])
except KeyError:
    print("key error")

# -----------------------------------------------------------------------------
# Q15. Classes: Write class User(name, age) with __init__ and an info() method returning "Name: Krishna, Age: 20"

# classes ( light - flask ke lie bs itna hi kafi hai)
class User:
    # constructor __init__ naam se banega , ye fix hai , hamesha isse hi banega
    def __init__(self, name, age):
        self.name = name  # that "self" keyword is just like the "this" in java
        self.age = age

    def info(self):
        return f"Name: {self.name} , age:{self.age}"

# creating the object of that class
s = User("Krishna", 20)  # passed our parameters #name of object is "s"
print(s.name)
print(s.age)
print(s.info())  # jis object ko banaya tha usi ki through class ke function ko call kie

# -----------------------------------------------------------------------------
# Q16. Imports & Modules: Create utility.py with greet(name) and import & call it.

# For demonstration, we'll create the utility function here and simulate importing it.
# (In real project put this in utility.py and use `from utility import greet`)

def greet(name):
    return f"Hello {name}"

result = greet("k")
print(result)

# -----------------------------------------------------------------------------
# Q17. Decorators: Create @debug decorator that prints "Function called" before calling target function.

# decorators ( flask route samajhne ke lie basics)

def debug(func):
    def wrapper(*args, **kwargs):
        print("Function called")  # decorator ka extra work
        return func(*args, **kwargs)
    return wrapper

@debug  # equivalent to "add=debug(add)" , add ko wrap kar dia
def add_decor(a, b):  # decorator lagne ke baad , add ko call karne pe actually wrapper call hoga
    return a + b

# test
ans = add_decor(5, 3)  # add actually calls the wrapper
print(ans)

# -----------------------------------------------------------------------------
# Q18. Mini project GET logic: Given users list, write get_user(id) returning user dict or 'user not found'

users = [
    {"id": 1, "name": "krishna"},
    {"id": 2, "name": "kris"}
]

def get_user(uid):
    for user in users:
        if user["id"] == uid:
            return user
    return "user not found"

print(get_user(1))

# -----------------------------------------------------------------------------
# Q19. Function that accepts JSON-like dict: input {"a":10,"b":5,"op":"add"}
# If op=="add" -> 15, if op=="mul" -> 50

def calculate(data):  # function takes input data as "data" , data will be a dictionary , just like JSON
    a = data["a"]  # extracting the "a" key's value from the dictionary
    b = data["b"]
    op = data["op"]

    if op == "add":
        return a + b
    elif op == "mul":
        return a * b
    else:
        return "invalid operation"

print(calculate({"a": 10, "b": 5, "op": "add"}))

# -----------------------------------------------------------------------------
# End of solutions. Run this file to see outputs for each question's solution.
