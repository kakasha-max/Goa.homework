def check_driving_license_eligibility():
    try:
        age = int(input("გთხოვთ, შეიყვანეთ თქვენი ასაკი: "))
        driving_experience = int(input("გთხოვთ, შეიყვანეთ წლების რაოდენობა, რომელსაც მართავთ მანქანას: "))

        if age < 0 or driving_experience < 0:
            print("გთხოვთ, შეიყვანეთ დადებითი მთელი რიცხვები.")
            return

        if age < 18:
            print("თქვენ არ გაქვთ მართვის მოწმობის აღების უფლება, რადგან არ ხართ 18 წლის.")
        elif age >= 18 and driving_experience < 1:
            print("თქვენ არ გაქვთ მართვის მოწმობის აღების უფლება, რადგან არ გაქვთ საკმარისი მართვის გამოცდილება.")
        else:
            print("თქვენ გაქვთ მართვის მოწმობის აღების უფლება!")
    except ValueError:
        print("გთხოვთ, შეიყვანეთ მხოლოდ მთელი რიცხვები.")

check_driving_license_eligibility()