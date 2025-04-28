# შექმენით სია 10 სხვადასხვა მონაცემთა ტიპის მქონე მნიშვნელობით
my_list = [42, "hello", 3.14, True, None, [1, 2, 3], {"key": "value"}, (4, 5), {9, 10}, b"bytes"]

# პირველი 3 მნიშვნელობის ინდივიდუალურად გამოტანა ტერმინალში
print(my_list[0])  # 42
print(my_list[1])  # "hello"
print(my_list[2])  # 3.14

# მეორე სამი მნიშვნელობის შეცვლა სხვადასხვა მნიშვნელობებით
my_list[3] = "Python"
my_list[4] = "JavaScript"
my_list[5] = "C++"

# სიაში 5 ახალი მნიშვნელობის დამატება
my_list.extend(["Go", "Rust", "Kotlin", "Swift", "Ruby"])

# საბოლოო სიის გამოტანა
print(my_list)