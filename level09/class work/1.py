# Input 3 different types of values
value1 = input("Enter a string value: ")
value2 = int(input("Enter an integer value: "))
value3 = float(input("Enter a float value: "))

# Check and print their data types
print("Type of value1:", type(value1))
print("Type of value2:", type(value2))
print("Type of value3:", type(value3))

# Concatenation examples
concat1 = value1 + " " + str(value2)
concat2 = str(value2) + " " + str(value3)
concat3 = value1 + " " + str(value3)

# Print concatenation results
print("Concatenation 1:", concat1)
print("Concatenation 2:", concat2)
print("Concatenation 3:", concat3)