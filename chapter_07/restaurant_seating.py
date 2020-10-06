seats_required = input("How many people are in your dinner group? ")
seats_required = int(seats_required)

if seats_required > 8:
    print("\nYou have to wait for a table.")
else:
    print("\nYour table is ready!")