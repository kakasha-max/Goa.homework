  # რიგი არის სია, რომელიც შეიცავს სახელებს
queue = ["john", "amy", "bob", "adam"]

  # ფუნქცია რომელიც ამატებს ახალ ელემენტს რიგში
def enqueue():
      # მომხმარებელს სთხოვს შეიყვანოს ახალი ელემენტი
      item = input("შეიყვანეთ ელემენტი რიგში დასამატებლად: ")
      # ამატებს ახალ ელემენტს რიგის ბოლოში
      queue.append(item)
      # ბეჭდავს განახლებულ რიგს
      print("რიგი ელემენტის დამატების შემდეგ:", queue)

  # იძახებს ფუნქციას
enqueue()