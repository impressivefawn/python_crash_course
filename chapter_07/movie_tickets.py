# 7-5. Movie Tickets:
prompt = "\nWe charge different ticket prices depending on person's age. Please, enter your age: "
prompt += "\nEnter 'quit' to end the program. "

age = ""

while True:
    age = input(prompt)
    if age == "quit":
        break
    elif int(age) < 3:
        print("The ticket is free.")
    elif int(age) <= 12:
        print("The ticket costs $10.")
    else:
        print("The ticket costs $15.")
