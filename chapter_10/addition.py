# 10-6. Addition:
try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Please provide a numeric input.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")