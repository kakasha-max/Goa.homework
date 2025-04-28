# Step 1: Initialize an empty list to store user numbers
user_numbers = []

# Step 2: Prompt the user to input numbers
while True:
    user_input = input("შეიყვანეთ რიცხვი (ან დააჭირეთ Enter-ს შეყვანის დასასრულებლად): ")
    if user_input == "":  # Stop if the input is empty
        break
    try:
        number = float(user_input)  # Convert input to a number
        user_numbers.append(number)
    except ValueError:
        print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი.")

# Step 3: Check if there is a number greater than 10 in the list
if any(num > 10 for num in user_numbers):
    print("სიაში არის 10-ზე მეტი რიცხვი")
else:
    print("სიაში 10-ზე მეტი რიცხვი არ არის")

# Step 4: Print the list and the sum of its elements
print("შექმნილი სია:", user_numbers)
print("სიის ელემენტების ჯამი:", sum(user_numbers))
