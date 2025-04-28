def simple_calculator(a, b, operation):
	if operation == "დამატება":
		return a + b
	elif operation == "გამოკლება":
		return a - b
	elif operation == "გამრავლება":
		return a * b
	elif operation == "გაყოფა":
		if b == 0:
			return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
		return a / b
	else:
		return "შეცდომა: უცნობი ოპერაცია"

# დამატება
print(simple_calculator(10, 5, "დამატება"))     # 15

# გამოკლება
print(simple_calculator(10, 5, "გამოკლება"))    # 5

# გამრავლება
print(simple_calculator(10, 5, "გამრავლება"))   # 50

# გაყოფა
print(simple_calculator(10, 5, "გაყოფა"))       # 2.0

# გაყოფა ნულზე
print(simple_calculator(10, 0, "გაყოფა"))       # შეცდომა: ნულზე გაყოფა შეუძლებელია

# უცნობი ოპერაცია
print(simple_calculator(10, 5, "ჯამი"))         # შეცდომა: უცნობი ოპერაცია
