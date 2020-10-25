# 10-7. Addition Calculator:
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)
    except ValueError:
        print("Please provide a numeric input.")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")