# Level 35 - Python Review (3 examples per topic)

# 1. Variables and Data Types
age = 15
height = 1.65
name = "Gabi"

# 2. Expressions and Operations
print(5 + 3)         # Addition
print(10 - 2)        # Subtraction
print(4 * 6)         # Multiplication

# 3. Conditional Statements (if, elif, else)
num = 7
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

grade = 85
if grade >= 90:
    print("Excellent!")
elif grade >= 75:
    print("Good job!")
else:
    print("Needs improvement")

# 4. Loops (for and while)
for i in range(3):
    print("Hello!")

numbers = [1, 2, 3]
for n in numbers:
    print(n)

count = 0
while count < 3:
    print("Count =", count)
    count += 1

# 5. Functions
def greet(name):
    print("Hi,", name)

greet("Gabi")
greet("Nika")
greet("Luka")

def square(x):
    return x * x

print(square(4))
print(square(9))
print(square(2))

# 6. List
fruits = ["apple", "pear", "banana"]
print(fruits[0])
fruits.append("peach")
print(len(fruits))

# 7. Tuple
colors = ("red", "blue", "green")
print(colors[1])
print(len(colors))
print("blue" in colors)

# 8. Input (user input)
# name = input("What is your name? ")
# print("Nice to meet you,", name)

# num = int(input("Enter a number: "))
# print("Double of the number is:", num * 2)

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# 9. Dictionary
student = {
    "name": "Gabi",
    "age": 15,
    "score": 98
}
print(student["name"])
student["age"] = 16
print(student)

# 10. Modules
import math
print(math.sqrt(16))
print(math.pi)
print(math.pow(2, 3))
