responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = location

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
    
print("\n--- Poll Results ---")
for name, location in responses.items():
    print(f"{name.title()} would like to go to {location.title()}.")

