denominator = 0
if denominator == 0:
    print("Error: Division by zero")
else:
    x = 1 / denominator
  

  # მომხმარებელს შემოატანინეთ 2 რიცხვი 
num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

# იპოვეთ უმცირესი და უდიდესი რიცხვი
start = min(num1, num2)
end = max(num1, num2)

# იპოვეთ ჯამი for ციკლის გამოყენებით
total_sum = 0
for i in range(start, end + 1):
    total_sum += i

print(f"რიცხვებს {start} და {end} შორის არსებული ყველა რიცხვის ჯამი არის: {total_sum}")
 