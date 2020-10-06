# 7-6. Three Exits:
prompt = "\nWhich topping would you like to add to your pizza:"
prompt += "\nEnter 'quit' to end the program. "

# Use a conditional test in the while statement to stop the loop.
# topping = ""
# while topping != "quit":
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"\nYou added {topping} to your pizza.")

# Use an active variable to control how long the loop runs.
# active = True
# while active:
#     topping = input(prompt)
#     if topping == "quit":
#         active = False
#     else:
#         print(topping)


# Use a break statement to exit the loop when the user enters a 'quit' value.
# topping = ""
# while True:
#     topping = input(prompt)
#     if topping == "quit":
#         break
#     print(f"\nYou added {topping} to your pizza.")