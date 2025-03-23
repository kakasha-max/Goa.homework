Read input values
weight = float(input())  # Weight in kg
height = float(input())  # Height in meters

Calculate  
bmi = weight / (height ** 2)

Determine BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")
    