# 1
def make_negative(number):
    # Return the number as negative if it's positive, otherwise return it unchanged
    return -abs(number) if number > 0 else number

# 2
def say_hello(name):
    return f"Hello, {name}"

# 3
def switch_it_up(number):
    words = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    return words.get(number, "")


# 4
def between(a, b):
    return list(range(a, b + 1))