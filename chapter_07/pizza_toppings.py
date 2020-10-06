# 7-4. Pizza Toppings:
prompt = "\nWhich topping would you like to add to your pizza:"
prompt += "\nEnter 'quit' to end the program. "

topping = ''
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"\nYou added {topping} to your pizza.")
